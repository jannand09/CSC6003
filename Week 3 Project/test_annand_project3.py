import io
import sys
from annand_project3 import *
import unittest


class TestBattleship(unittest.TestCase):

    def test_GameOver(self):
        arr1 = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', 'S', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', 'S', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', 'S', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', 'S', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', 'S', '.', '.', '.', '.', '.', '.', '.', '.']]
        arr2 = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', 'X', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', 'X', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', 'X', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', 'X', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', 'X', '.', '.', '.', '.', '.', '.', '.', '.']]

        self.assertFalse(isGameOver(arr1))
        self.assertTrue(isGameOver(arr2))

    def test_Hit(self):
        arr1 = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', 'S', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', 'S', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', 'S', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', 'S', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', 'S', '.', '.', '.', '.', '.', '.', '.', '.']]

        #code snippet takes the output that gets printed to the console and stores it as variable
        # https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
        function_output = io.StringIO()
        sys.stddout = function_output
        checkHitOrMiss(2, 7, arr1)
        sys.stdout = sys.__stdout__

        self.assertEqual(function_output.getvalue(), "HIT")

    def test_Miss(self):
        arr1 = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', 'S', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', 'S', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', 'S', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', 'S', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', 'S', '.', '.', '.', '.', '.', '.', '.', '.']]

        # Same snippet as before
        function_output = io.StringIO()
        sys.stddout = function_output
        checkHitOrMiss(1, 1, arr1)
        sys.stdout = sys.__stdout__

        self.assertEqual(function_output.getvalue(), "MISS")


    def test_setUp(self):
        arr = setupBoard()

        empty_spaces = 0
        ships = 0

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 'S':
                    ships = ships + 1
                else:
                    empty_spaces = empty_spaces + 1

        self.assertEqual(empty_spaces, 95)
        self.assertEquals(ships, 5)


        

