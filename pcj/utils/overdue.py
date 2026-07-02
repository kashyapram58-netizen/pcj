import frappe
from frappe.utils import today


def send_overdue_task_reminders():
    """
    Send reminder emails for overdue tasks that are not completed.
    """

    overdue_tasks = frappe.get_all(
        "Task Tracker",
        filters={
            "status": ["!=", "Completed"],
            "revised_due_date": ["<", today()]
        },
        fields=[
            "name",
            "task_name",
            "assigned_to",
            "revised_due_date"
        ]
    )

    for task in overdue_tasks:

        if not task.assigned_to:
            continue

        frappe.sendmail(
            recipients=[task.assigned_to],
            subject=f"Overdue Task: {task.task_name}",
            message=f"""
                <p>Hello,</p>

                <p>The following task is overdue.</p>

                <ul>
                    <li><b>Task:</b> {task.task_name}</li>
                    <li><b>Due Date:</b> {task.revised_due_date}</li>
                </ul>

                <p>Please complete it as soon as possible.</p>
            """
        )