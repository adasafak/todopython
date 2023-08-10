class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added:", task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print("Task removed:", removed_task)
        else:
            print("Invalid task index.")

    def show_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index}: {task}")
        else:
            print("No tasks in the list.")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()