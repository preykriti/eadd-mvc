class Todo:
    def __init__(self,title):
        self.title = title

todo = [
    Todo("Water plants"),
    Todo("Read a book"),
    Todo("Wake up early")
]

def getTodo():
    return todo