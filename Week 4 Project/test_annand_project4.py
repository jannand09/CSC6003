# Unit test for annand_project4

from annand_project4 import *
import unittest

class TestRectangle(unittest.TestCase):
    
    #Create cases as instances of Rectangle and Parallelepiped classes to test methods
    case1 = Rectangle(1,1)
    case2 = Rectangle(2,2)
    case3 = Rectangle(3,4)

    case4 = Parallelepipede(1,1,1)
    case5 = Parallelepipede(2,3,4)

    #Test perimeter method
    def test_perimeter(self):
        self.assertEqual(self.case1.perimeter(), 4)
        self.assertEqual(self.case2.perimeter(), 8)
        self.assertEqual(self.case3.perimeter(), 14)
    
    #Test area method
    def test_area(self):
        self.assertEqual(self.case1.area(), 1)
        self.assertEqual(self.case2.area(), 4)
        self.assertEqual(self.case3.area(), 12)
    
    #Test volume method
    def test_volume(self):
        self.assertEqual(self.case4.volume(), 1)
        self.assertEqual(self.case5.volume(), 24)
 