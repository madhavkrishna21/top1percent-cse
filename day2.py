# day2.py - Top 1% To-Do List (JSON Save)
import json
from datetime import datetime

class Todo:
    def __init__(self):
        self.file = "tasks.json"
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    def save_tasks(self):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=2)
        print("Tasks saved to tasks.json!")

    def add(self, task):
        self.tasks.append({
            "task": task,
            "done": False,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        self.save_tasks()

    def show(self):
        if not self.tasks:
            print("No tasks! Add one.")
            return
        for i, t in enumerate(self.tasks):
            status = "✓" if t["done"] else "○"
            print(f"{i+1}. {status} {t['task']} [{t['date']}]")

    def done(self, num):
        if 1 <= num <= len(self.tasks):
            self.tasks[num-1]["done"] = True
            self.save_tasks()
        else:
            print("Invalid number!")

todo = Todo()
print("=== TOP 1% TO-DO ===")
while True:
    cmd = input("\n[add / list / done / quit]: ").strip().lower()
    if cmd == "add":
        task = input("Task: ")
        todo.add(task)
    elif cmd == "list":
        todo.show()
    elif cmd == "done":
        num = int(input("Done #: "))
        todo.done(num)
    elif cmd == "quit":
        print("See you on Day 3!")
        break
    else:
        print("Invalid command!")
