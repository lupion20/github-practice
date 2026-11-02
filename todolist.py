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

if __name__ == "__main__":
    t = Todo("買い物")
    print(t.to_dict())

    t.complete()
    print(t.to_dict())

    t2 = Todo.from_dict({"title": "掃除", "done": True})
    print(t2.title, t2.done)