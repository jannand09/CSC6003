
from annand_project6 import *
import unittest

class TestDeque(unittest.TestCase):

    test_deque = Deque()
    test_deque2 = Deque()
    test_deque3 = Deque()
    test_deque4 = Deque()
    test_deque5 = Deque()
    test_deque6 = Deque()
    test_deque7 = Deque()
    test_deque8 = Deque()

    test_deque.items = [1,2,3,4,5]
    test_deque2.items = [5,6,7,8,9]
    test_deque3.items = [10,11,12,13,14]
    test_deque4.items = [15,16,17,18,19]
    test_deque5.items = [20,21,22,23,24]
    test_deque6.items = [25,26,27,28,29]
    test_deque7.items = [30,31,32,33,34]
    test_deque8.items = [35,36,37,38,39]

    def test_isEmpty(self):
        self.assertEqual(self.test_deque.isEmpty(), False)

    def test_addToStart(self):
        self.assertEqual(self.test_deque2.addToStart(0), [0,5,6,7,8,9])
        
    def test_addToEnd(self):
        self.assertEqual(self.test_deque3.addToEnd(6), [10,11,12,13,14,6])
    
    def test_removeFromStart(self):
        self.assertEqual(self.test_deque4.removeFromStart(), 15)

    def test_removeFromEnd(self):
        self.assertEqual(self.test_deque5.removeFromEnd(), 24)
    
    def test_End(self):
        self.assertEqual(self.test_deque6.End(), 29)
    
    def test_Start(self):
        self.assertEqual(self.test_deque7.Start(), 30)

    def test_size(self):
        self.assertEqual(self.test_deque8.size(), 5)
