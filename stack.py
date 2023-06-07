class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self, value):
        if self.is_empty():
            return None
        elif self.items[-1] < value:
            value -= self.items[-1]
            self.items.pop()
            return self.pop(value)
        elif self.items[-1] == value:
            self.items.pop(0)
        else:
            self.items[-1] -= value

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def total(self):
        total = 0
        for i in self.items:
            total += i
        return total


# s = Stack()
# s.push(5)
# s.push(12)
# s.push(52)


# print(s.items)
# print(s.peek())
# print(s.items)
