# # Describe how you could use a single array to implement three stacks
# # https://medium.com/@emmabostian/creating-3-stacks-with-1-array-in-javascript-e1171d661e89


class MultiStack:
    def __init__(self, stack_size, number_of_stacks):
        self.stack_size = stack_size
        self.number_of_stacks = number_of_stacks
        self.array = [None] * number_of_stacks * stack_size
        self.sizes = [0] * stack_size

    def top_index(self, stack_number):
        offset = stack_number * self.stack_size
        top_index_stack = self.sizes[stack_number]
        return offset + top_index_stack - 1

    def push(self, stack_number, value):
        self.sizes[stack_number] += 1
        index = self.top_index(stack_number)
        self.array[index] = value

    def pop(self, stack_number):
        index = self.top_index(stack_number)
        value = self.array[index]
        self.array[index] = None
        self.sizes[stack_number] -= 1
        return value

    def peek(self, stack_number):
        index = self.top_index(stack_number)
        return self.array[index]

    def print_stack(self, stack_number=None):
        start = stack_number * self.stack_size
        for i in range(self.sizes[stack_number]):
            print(self.array[i + start], " ", end="")
        print()

    def is_empty(self, stack_number):
        return self.sizes[stack_number] == 0

    def is_full(self, stack_number):
        return self.sizes[stack_number] == self.stack_size

        # print(self.array)


s = MultiStack(5, 3)
s.push(0, 1)
s.push(0, 12)
s.push(1, 3)
s.push(1, 4)
s.print_stack(1)
# print(s.peek(0))
