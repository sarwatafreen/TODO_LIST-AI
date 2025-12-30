# Todo Console Application

A simple in-memory console-based todo application that allows users to manage their tasks through a menu-driven interface.

## Features

- Add new tasks
- View task list
- Update task descriptions
- Delete tasks
- Mark tasks as complete/incomplete
- All data stored in memory only (lost on exit)

## Requirements

- Python 3.10 or higher

## Setup

1. Clone or download the repository
2. Navigate to the project directory containing the `src` folder

## Usage

To run the application, execute the following command from the project root:

```bash
python -m src.main
```

Alternatively, you can run:

```bash
python src/main.py
```

## Application Flow

1. The application presents a numbered menu with 7 options:
   1. Add Task
   2. View Task List
   3. Update Task
   4. Delete Task
   5. Mark Task Complete
   6. Mark Task Incomplete
   7. Exit

2. Select an option by entering the corresponding number
3. Follow the prompts to complete your desired action
4. The application will return to the main menu after each operation
5. Select option 7 to exit the application

## Error Handling

- Invalid menu choices will display an error message and return to the main menu
- Invalid task IDs will display an error message
- Empty task descriptions will be rejected
- Operations on non-existent tasks will display an error message
- Empty task lists will display appropriate messages

## Project Structure

```
src/
├── main.py              # Application entry point
├── __init__.py          # Package marker
├── cli/
│   ├── __init__.py      # Package marker
│   └── interface.py     # Menu rendering & user input handling
├── models/
│   ├── __init__.py      # Package marker
│   └── task.py          # Task data model
└── services/
    ├── __init__.py      # Package marker
    └── task_manager.py  # In-memory task logic (add, update, delete, toggle completion)
```

## Limitations

- Data is stored only in memory and will be lost when the application exits
- Single user only
- No persistence beyond runtime
- Maximum recommended task count: 1000 tasks (for optimal performance)