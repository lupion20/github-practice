import json
import os

class Todo:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def complete(self):
        self.done = True

    def to_dict(self):
        return {"title": self.title,
                "done": self.done
                }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["done"])


class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, title):
        t = Todo(title)
        self.todos.append(t)

    def complete(self, index):
        self.todos[index].complete()

    def delete(self, index):
        return self.todos.pop(index)

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.todos], f, ensure_ascii=False, indent=2)

    def load(self, path):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.todos = [Todo.from_dict(d) for d in data]

if __name__ == "__main__":
    tl = TodoList()
    tl.add("買い物")
    tl.add("掃除")
    tl.complete(0)
    removed = tl.delete(1)
    print("削除:", removed.title)

    tl.save("check.json")

    tl2 = TodoList()
    tl2.load("check.json")
    for t in tl2.todos:
        print(t.to_dict())