class Queue:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        self.queue.pop(0)

    def queue_size(self):
        return len(self.queue)
