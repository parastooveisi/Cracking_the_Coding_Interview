# https://medium.com/better-programming/how-to-implement-a-queue-using-two-stacks-80772242b88c

from stack import Stack


class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        return self.stack2.peek()

    def size(self):
        return len(self.stack1.getStack()) + len(self.stack2.getStack())


q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print(q.peek())

print(q.size())
