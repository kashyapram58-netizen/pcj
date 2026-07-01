# Copyright (c) 2026, Ram and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today


class TaskTracker(Document):

    def validate(self):
        self.validate_revised_due_date_permission()
        self.validate_dates()
        self.track_extension()
        self.calculate_score()
        self.update_status()
        self.send_extension_email()

    # ---------------------------------------------------------
    # Validations
    # ---------------------------------------------------------

    def validate_dates(self):
        """Basic date validations."""

        if self.start_date and self.original_due_date:
            if self.start_date > self.original_due_date:
                frappe.throw("Original Due Date cannot be before Start Date.")

        if self.original_due_date and self.revised_due_date:
            if self.revised_due_date < self.original_due_date:
                frappe.throw("Revised Due Date cannot be before Original Due Date.")

    # ---------------------------------------------------------
    # Extension Tracking
    # ---------------------------------------------------------

    def track_extension(self):
        """
        Increase extension count only when Revised Due Date changes.
        """

        # New document
        if self.is_new():
            self.extension_count = 0
            return

        previous_doc = self.get_doc_before_save()

        if not previous_doc:
            return

        previous_date = previous_doc.revised_due_date
        current_date = self.revised_due_date

        if previous_date != current_date:
            self.extension_count = (previous_doc.extension_count or 0) + 1

    # ---------------------------------------------------------
    # Score Calculation
    # ---------------------------------------------------------

    def calculate_score(self):

        score_map = {
            0: 100,
            1: 75,
            2: 50,
            3: 25
        }

        count = self.extension_count or 0

        self.score = score_map.get(count, 0)

    # ---------------------------------------------------------
    # Status Logic
    # ---------------------------------------------------------

    def update_status(self):

        if self.score == 0:
            self.status = "Failed"

    # ---------------------------------------------------------
    # Email Notification
    # ---------------------------------------------------------

    def send_extension_email(self):

        if (self.extension_count or 0) <= 2:
            return

        # Prevent duplicate emails while editing
        previous_doc = None

        if not self.is_new():
            previous_doc = self.get_doc_before_save()

        previous_count = (
            previous_doc.extension_count
            if previous_doc else 0
        )

        if previous_count > 2:
            return

        if not self.assigned_to:
            return

        frappe.sendmail(
            recipients=[self.assigned_to],
            subject=f"Task '{self.task_name}' Extended Multiple Times",
            message=f"""
                <p>Hello,</p>

                <p>Your task <b>{self.task_name}</b> has now been extended
                <b>{self.extension_count}</b> times.</p>

                <p>Current Score : <b>{self.score}</b></p>

                <p>Please complete the task as soon as possible.</p>

                <br>

                <p>ERPNext</p>
            """
        )
    def validate_revised_due_date_permission(self):
					"""
					Only authorized roles can change the Revised Due Date.
					"""

					# New document creation is allowed
					if self.is_new():
						return

					previous_doc = self.get_doc_before_save()
					if not previous_doc:
						return

					# Nothing changed
					if previous_doc.revised_due_date == self.revised_due_date:
						return

					allowed_roles = ["System Manager", "Task Manager"]

					if not any(role in frappe.get_roles() for role in allowed_roles):
						frappe.throw(
							"You are not permitted to modify the Revised Due Date."
						)
