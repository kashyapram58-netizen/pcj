// Copyright (c) 2026, Ram and contributors
// For license information, please see license.txt

frappe.ui.form.on("Task Tracker", {
    refresh(frm) {

        // Read-only calculated fields
        frm.set_df_property("extension_count", "read_only", 1);

        // Original due date should not change after creation
        if (!frm.is_new()) {
            frm.set_df_property("original_due_date", "read_only", 1);
        }

        // Visual indicator based on score
        if (!frm.is_new()) {

            if (frm.doc.score == 100) {
                frm.dashboard.set_headline_alert(
                    __("Excellent Performance (100%)"),
                    "green"
                );
            }

            else if (frm.doc.score >= 50) {
                frm.dashboard.set_headline_alert(
                    __("Performance Dropped Due to Extensions"),
                    "orange"
                );
            }

            else if (frm.doc.score > 0) {
                frm.dashboard.set_headline_alert(
                    __("Task is at High Risk"),
                    "red"
                );
            }

            else if (frm.doc.score == 0) {
                frm.dashboard.set_headline_alert(
                    __("Task Failed (Maximum Extensions Reached)"),
                    "red"
                );
            }
        }
    }
});
