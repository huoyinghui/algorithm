from unittest import TestCase
from stack.sstack import SStack


class TestSStack(TestCase):
    def setUp(self):
        self.data = SStack()
        self.data.push(1)

    def test_is_empty(self):
        if self.data.is_empty():
            self.fail()

    def test_push(self):
        self.data.push(100)
        if self.data.top() != 100:
            self.fail()

    def test_pop(self):
        self.data.push(100)
        if self.data.pop() != 100:
            self.fail()

    def test_top(self):
        self.data.push(1000)
        if self.data.top() != 1000:
            self.fail()

    def tearDown(self):
        self.data = None
