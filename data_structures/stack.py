class Stack(object):
    def __init__(self, limit=50):
        self.stack = []
        self.limit = limit

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)

    def push(self, data):
        if len(self.stack) >= self.limit:
            raise Exception('StackOverflowError')

        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from empty stack')

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()

    for i in range(20):
        stack.push(i)

    print('Stack:\n' + str(stack))
    print('pop(): ' + str(stack.pop()))
    print('After pop(): ' + str(stack))
    print('peek(): ' + str(stack.peek()))
    stack.push(20)
    print('After push(20), the stack is now: ' + str(stack))
    print('is_empty(): ' + str(stack.is_empty()))
    print('size(): ' + str(stack.size()))
