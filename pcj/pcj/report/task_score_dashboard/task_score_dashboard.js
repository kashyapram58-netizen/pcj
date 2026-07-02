frappe.query_reports["Task Score Dashboard"] = {

    filters: [

        {
            fieldname: "assigned_to",
            label: __("Assigned To"),
            fieldtype: "Link",
            options: "User"
        },

        {
            fieldname: "from_date",
            label: __("From Date"),
            fieldtype: "Date"
        },

        {
            fieldname: "to_date",
            label: __("To Date"),
            fieldtype: "Date"
        }

    ]

};