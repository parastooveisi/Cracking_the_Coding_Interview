# Write a program to sort a stack such that the smallest items are on the top

from stack import Stack


def sort_stack(input_stack):
    temp_stack = Stack()
    while not input_stack == []:

        temp_value = input_stack.pop()

        while not temp_stack.isEmpty() and temp_value < temp_stack.peek():
            input_stack.append(temp_stack.pop())

        temp_stack.push(temp_value)

    return temp_stack.getStack()


print(sort_stack([34, 3, 31, 98, 92, 23]))
