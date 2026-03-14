# 🎯 Task Management App

A simple and interactive task manager built with **Streamlit**. Manage your personal to-do list directly in the browser — no database required.

---

## Features

- **Add tasks** with duplicate detection
- **View all tasks** in a numbered list
- **Update existing tasks** by selecting and replacing them
- **Delete individual tasks** or clear the entire list at once
- Task count displayed live in the sidebar
- Session-based persistence (tasks are retained during the active browser session)

---

## Requirements

- Python 3.7+
- Streamlit

Install dependencies:

```bash
pip install streamlit
```

---

## How to Run

```bash
streamlit run code.py
```

Then open your browser to `http://localhost:8501`.

---

## Usage

Use the **sidebar** to navigate between operations:

| Operation | Description |
|---|---|
| Add Task | Type a task and click **Add Task** to append it to your list |
| View Tasks | See all current tasks in a numbered list |
| Update Task | Select an existing task and replace it with a new value |
| Delete Task | Select a task to remove it individually |
| Clear All Tasks | One-click button in the sidebar to wipe the entire list |

---

## Project Structure

```
code.py       # Main application file
README.md
```

---

## Notes

- Tasks are stored in **Streamlit session state**, meaning they are lost when the browser tab is closed or the app is restarted.
- Duplicate tasks are not allowed — the app will warn you if you try to add one that already exists.
- For persistent storage across sessions, the task list could be extended to use a database or a local file (e.g., JSON or SQLite).
