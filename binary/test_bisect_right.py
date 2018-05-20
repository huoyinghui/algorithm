from unittest import TestCase
from binary.bisect import bisect_right, insort_right

class TestBisect(TestCase):
    def setUp(self):
        self.data = [1, 5, 9, 10]

    def test_right(self):
        index = bisect_right(self.data, 2)
        assert index == 1

    def tearDown(self):
        self.data = None
