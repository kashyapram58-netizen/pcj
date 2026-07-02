import frappe


def execute(filters=None):

    columns = get_columns()

    data = get_data(filters)

    return columns, data

def get_columns():

    return [

        {
            "label":"Employee",
            "fieldname":"assigned_to",
            "fieldtype":"Link",
            "options":"User",
            "width":220
        },

        {
            "label":"Total Tasks",
            "fieldname":"total_tasks",
            "fieldtype":"Int",
            "width":120
        },

        {
            "label":"Average Score",
            "fieldname":"average_score",
            "fieldtype":"Float",
            "precision":2,
            "width":130
        },

        {
            "label":"Completed",
            "fieldname":"completed",
            "fieldtype":"Int",
            "width":110
        },

        {
            "label":"Failed",
            "fieldname":"failed",
            "fieldtype":"Int",
            "width":100
        },

        {
            "label":"Overdue",
            "fieldname":"overdue",
            "fieldtype":"Int",
            "width":100
        }

    ]

import frappe

def get_data(filters):

    conditions = ""
    values = {}

    if filters.get("assigned_to"):
        conditions += " AND assigned_to = %(assigned_to)s"
        values["assigned_to"] = filters.get("assigned_to")

    if filters.get("from_date"):
        conditions += " AND start_date >= %(from_date)s"
        values["from_date"] = filters.get("from_date")

    if filters.get("to_date"):
        conditions += " AND start_date <= %(to_date)s"
        values["to_date"] = filters.get("to_date")

    return frappe.db.sql(
        f"""
        SELECT
            assigned_to,
            COUNT(*) AS total_tasks,
            AVG(score) AS average_score,
            SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) AS completed,
            SUM(CASE WHEN status = 'Failed' THEN 1 ELSE 0 END) AS failed,
            SUM(
                CASE
                    WHEN status != 'Completed'
                     AND revised_due_date < CURDATE()
                    THEN 1
                    ELSE 0
                END
            ) AS overdue
        FROM `tabTask Tracker`
        WHERE 1 = 1
        {conditions}
        GROUP BY assigned_to
        ORDER BY average_score DESC
        """,
        values=values,
        as_dict=True,
    )