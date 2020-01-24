class Empty(Exception):
    pass


#   适配器设计模式
class ArrayStack:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()


def reverse_file(filename):
    S = ArrayStack()
    with open(filename, "r+") as fp:
        for line in fp:
            S.push(line.strip("\n"))
        fp.write("\n----------------------\n")
        while not S.is_empty():
            fp.write(S.pop() + "\n")


# 针对最后一行没有\n的情况
if __name__ == "__main__":
    reverse_file("栈和队列/sample.txt")

