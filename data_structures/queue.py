class Queue():
    def __init__(self, entries=[]):
        self.entries = entries
        self.length = len(entries)
        self.front = 0

    def __str__(self):
        printed = '<' + str(self.entries)[1:-1] + '>'

        return printed

    def put(self, item):
        self.entries.append(item)
        self.length = self.length + 1

    def get(self):
        self.length = self.length - 1
        dequeued = self.entries[self.front]
        self.front -= 1
        self.entries = self.entries[self.front:]

        return dequeued

    def front(self):
        return self.entries[0]

    def size(self):
        return self.length


queue = Queue([5, 4, 3])
queue.put(5)
print(queue.length)
print(queue)
