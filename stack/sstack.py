from stack.error import SStackException


class SStack(object):
    """docstring for SStack"""
    def __init__(self):
        super(SStack, self).__init__()
        self._element = []

    def is_empty(self):
        return self._element == []

    def push(self, item):
        self._element.append(item)

    def pop(self):
        if self.is_empty():
            raise SStackException('no element in stack')
        return self._element.pop() 

    def top(self):
        if self.is_empty():
            raise SStackException('no element in stack')
        return self._element[-1]


def main():
    s = SStack()
    s.push(2)
    s.push(3)
    while not s.is_empty():
        print('top:{} pop:{}'.format(s.top(), s.pop()))

    pass

if __name__ == '__main__':
    main()