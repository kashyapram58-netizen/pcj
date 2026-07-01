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