# PCJ

A custom ERPNext/Frappe application for FMCG solutions.

---

# Project 1 - Task Assignment & Score Tracker

A lightweight task delegation and performance scoring system built using the Frappe Framework.

The system automatically tracks deadline extensions and evaluates employee performance based on punctuality.

---

# Features

- Assign tasks to users
- Track Original & Revised Due Dates
- Automatic Extension Counter
- Automatic Score Calculation
- Auto Status Update
- Person-wise Performance Dashboard
- Failed Task Tracking
- Overdue Task Identification
- Permission Controlled Due Date Modification
- Auto-generated Task IDs

---

# Mind Map

```mermaid
mindmap
  root((Task Tracker))

    Task Assignment
      Task Name
      Assigned To
      Start Date
      Original Due Date
      Revised Due Date

    Extension Tracking
      Detect Due Date Change
      Increase Extension Count

    Score Calculation
      0 -> 100
      1 -> 75
      2 -> 50
      3 -> 25
      4+ -> 0

    Status
      Open
      Completed
      Failed

    Dashboard
      Average Score
      Completed Tasks
      Failed Tasks
      Overdue Tasks

    Security
      Task Manager
      System Manager
      Revised Due Date Permission

    Automation
      Auto Naming
      Email Notification
      Scheduled Reminder
```

---

# Workflow

```mermaid
flowchart TD

A[Create Task]
--> B[Assign User]

B --> C[Enter Start Date]

C --> D[Original Due Date]

D --> E[Save]

E --> F[Task Created]

F --> G{Need Extension?}

G -- No --> H[Score = 100]

G -- Yes --> I[Change Revised Due Date]

I --> J[Extension Count +1]

J --> K[Recalculate Score]

K --> L{Score = 0?}

L -- Yes --> M[Status = Failed]

L -- No --> N[Continue Task]

N --> O[Complete Task]

M --> O
```

---

# Score Calculation Logic

```mermaid
flowchart LR

A[Extension Count]

A -->|0| B[100]

A -->|1| C[75]

A -->|2| D[50]

A -->|3| E[25]

A -->|4+| F[0]
```

---

# Task Lifecycle

```mermaid
stateDiagram-v2

[*] --> Draft

Draft --> Assigned

Assigned --> InProgress

InProgress --> Completed

InProgress --> Failed

Failed --> [*]

Completed --> [*]
```

---

# Extension Tracking

```mermaid
sequenceDiagram

User->>Task Tracker: Update Revised Due Date

Task Tracker->>Database: Fetch Previous Document

Database-->>Task Tracker: Previous Due Date

Task Tracker->>Task Tracker: Compare Dates

alt Changed

Task Tracker->>Task Tracker: Extension Count +1

Task Tracker->>Task Tracker: Recalculate Score

end
```

---

# Permission Logic

```mermaid
flowchart TD

User

--> CheckRole

CheckRole -->|Task Manager| Allow

CheckRole -->|System Manager| Allow

CheckRole -->|Other Users| Reject
```

---

# Dashboard Logic

```mermaid
flowchart LR

Task Tracker

--> Average Score

Task Tracker

--> Completed Count

Task Tracker

--> Failed Count

Task Tracker

--> Overdue Tasks
```

---

# Report Query Flow

```mermaid
flowchart TD

Task Tracker Table

--> SQL Query

SQL Query

--> Group By Assigned User

Group By Assigned User

--> Average Score

Group By Assigned User

--> Completed

Group By Assigned User

--> Failed

Group By Assigned User

--> Overdue
```

---

# Project Structure

```
pcj/

│

├── pcj/

│   ├── doctype/

│   │

│   └── task_tracker/

│       ├── task_tracker.py

│       ├── task_tracker.js

│       ├── task_tracker.json

│

├── report/

│   └── task_score_dashboard/

│       ├── task_score_dashboard.py

│       ├── task_score_dashboard.js

│       └── task_score_dashboard.json

│

├── utils.py

├── hooks.py

└── README.md
```

---

# Auto Naming

```
TT-Ram-2026-00001

TT-Ram-2026-00002

TT-John-2026-00001
```

---

# Business Rules

| Rule | Description |
|------|-------------|
| Extension Count | Increased only when Revised Due Date changes |
| Score | Calculated automatically |
| Original Due Date | Cannot be modified after creation |
| Revised Due Date | Editable only by authorized roles |
| Failed | Score = 0 |
| Overdue | Revised Due Date < Today & Status != Completed |
| Completed On | Must lie between Start Date and Due Date |

---

# Tech Stack

- Frappe Framework v15
- ERPNext
- Python
- JavaScript
- MariaDB
- Script Reports

---

# Future Enhancements

- Email escalation to managers
- Employee Leaderboard
- KPI Dashboard
- Charts using Dashboard Charts
- SLA Tracking
- Task Categories
- Priority Levels
- Notifications
- REST API Integration

---

# License

MIT