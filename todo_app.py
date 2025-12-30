"""
Todo Console Application - Phase I Implementation

A simple in-memory console-based todo application that allows users to:
- Add tasks
- View task list
- Update tasks
- Delete tasks
- Mark tasks as complete/incomplete

All data is stored in memory only and is lost when the application exits.
"""

class Task:
    """
    Represents a single todo task with ID, description, and completion status.
    """
    def __init__(self, task_id, description):
        self.id = task_id
        self.description = description
        self.completed = False  # Default to incomplete

    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"{self.id}. [{status}] {self.description}"


class TaskManager:
    """
    Manages the collection of tasks in memory.
    Handles all data operations for tasks.
    """
    def __init__(self):
        self.tasks = []  # In-memory storage for tasks
        self.next_id = 1  # Sequential ID generator starting from 1

    def add_task(self, description):
        """Add a new task with a unique ID."""
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task_by_id(self, task_id):
        """Find and return a task by its ID, or None if not found."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self):
        """Return all tasks."""
        return self.tasks

    def update_task(self, task_id, new_description):
        """Update the description of a task by its ID."""
        task = self.get_task_by_id(task_id)
        if task:
            task.description = new_description
            return True
        return False

    def delete_task(self, task_id):
        """Delete a task by its ID."""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_task_complete(self, task_id):
        """Mark a task as complete by its ID."""
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
            return True
        return False

    def mark_task_incomplete(self, task_id):
        """Mark a task as incomplete by its ID."""
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            return True
        return False


def display_menu():
    """Display the main menu options to the user."""
    print("\n" + "="*40)
    print("TODO APPLICATION - MAIN MENU")
    print("="*40)
    print("1. Add Task")
    print("2. View Task List")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Mark Task Incomplete")
    print("7. Exit")
    print("="*40)
    print("Choose an option (1-7): ", end="")


def main():
    """Main application loop that controls the flow of the application."""
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = input().strip()

        if is_valid_menu_choice(choice):
            if choice == "1":
                handle_add_task(task_manager)
            elif choice == "2":
                handle_view_tasks(task_manager)
            elif choice == "3":
                handle_update_task(task_manager)
            elif choice == "4":
                handle_delete_task(task_manager)
            elif choice == "5":
                handle_mark_complete(task_manager)
            elif choice == "6":
                handle_mark_incomplete(task_manager)
            elif choice == "7":
                print("\nThank you for using the Todo Application. Goodbye!")
                break
        else:
            print("\nInvalid choice. Please select a number between 1 and 7.")


def handle_add_task(task_manager):
    """Handle the Add Task functionality."""
    print("\n--- ADD TASK ---")
    description = input("Enter task description: ").strip()

    if not is_valid_task_description(description):
        print("Error: Task description cannot be empty.")
        return

    task = task_manager.add_task(description)
    print(f"Task added successfully with ID {task.id}: {task.description}")


def handle_view_tasks(task_manager):
    """Handle the View Task List functionality."""
    print("\n--- VIEW TASK LIST ---")
    tasks = task_manager.get_all_tasks()

    if not tasks:
        print("Your task list is empty.")
        return

    print(f"Total tasks: {len(tasks)}")
    for task in tasks:
        print(task)


def handle_update_task(task_manager):
    """Handle the Update Task functionality."""
    print("\n--- UPDATE TASK ---")

    if not task_manager.get_all_tasks():
        print("Your task list is empty. Cannot update any tasks.")
        return

    try:
        task_id_input = input("Enter task ID to update: ").strip()
        task_id = int(task_id_input)

        # Check if the task ID exists
        if not task_manager.get_task_by_id(task_id):
            print(f"Error: Task with ID {task_id} not found.")
            return
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    task = task_manager.get_task_by_id(task_id)
    print(f"Current task: {task}")
    new_description = input("Enter new task description: ").strip()

    if not is_valid_task_description(new_description):
        print("Error: Task description cannot be empty.")
        return

    success = task_manager.update_task(task_id, new_description)
    if success:
        print(f"Task {task_id} updated successfully: {new_description}")
    else:
        print(f"Error: Could not update task {task_id}.")


def handle_delete_task(task_manager):
    """Handle the Delete Task functionality."""
    print("\n--- DELETE TASK ---")

    if not task_manager.get_all_tasks():
        print("Your task list is empty. Cannot delete any tasks.")
        return

    task_id_input = input("Enter task ID to delete: ").strip()

    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    # Check if the task ID exists
    if not task_manager.get_task_by_id(task_id):
        print(f"Error: Task with ID {task_id} not found.")
        return

    task = task_manager.get_task_by_id(task_id)
    print(f"Task to delete: {task}")
    confirm = input("Are you sure you want to delete this task? (y/N): ").strip().lower()

    if confirm in ['y', 'yes']:
        success = task_manager.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Error: Could not delete task {task_id}.")
    else:
        print("Task deletion cancelled.")


def handle_mark_complete(task_manager):
    """Handle the Mark Complete functionality."""
    print("\n--- MARK TASK COMPLETE ---")

    if not task_manager.get_all_tasks():
        print("Your task list is empty. No tasks to mark as complete.")
        return

    task_id_input = input("Enter task ID to mark as complete: ").strip()

    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    # Check if the task ID exists
    if not task_manager.get_task_by_id(task_id):
        print(f"Error: Task with ID {task_id} not found.")
        return

    task = task_manager.get_task_by_id(task_id)
    if task.completed:
        print(f"Task {task_id} is already marked as complete.")
        return

    success = task_manager.mark_task_complete(task_id)
    if success:
        print(f"Task {task_id} marked as complete: {task.description}")
    else:
        print(f"Error: Could not mark task {task_id} as complete.")


def handle_mark_incomplete(task_manager):
    """Handle the Mark Incomplete functionality."""
    print("\n--- MARK TASK INCOMPLETE ---")

    if not task_manager.get_all_tasks():
        print("Your task list is empty. No tasks to mark as incomplete.")
        return

    task_id_input = input("Enter task ID to mark as incomplete: ").strip()

    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    # Check if the task ID exists
    if not task_manager.get_task_by_id(task_id):
        print(f"Error: Task with ID {task_id} not found.")
        return

    task = task_manager.get_task_by_id(task_id)
    if not task.completed:
        print(f"Task {task_id} is already marked as incomplete.")
        return

    success = task_manager.mark_task_incomplete(task_id)
    if success:
        print(f"Task {task_id} marked as incomplete: {task.description}")
    else:
        print(f"Error: Could not mark task {task_id} as incomplete.")


def is_valid_menu_choice(choice):
    """Validate if the menu choice is a valid option (1-7)."""
    try:
        choice_num = int(choice)
        return 1 <= choice_num <= 7
    except ValueError:
        return False


def is_valid_task_id(task_manager, task_id):
    """Validate if the task ID exists in the task manager."""
    try:
        task_id_num = int(task_id)
        return task_manager.get_task_by_id(task_id_num) is not None
    except ValueError:
        return False


def is_valid_task_description(description):
    """Validate if the task description is not empty."""
    return description.strip() != ""


# Main execution guard
if __name__ == "__main__":
    main()