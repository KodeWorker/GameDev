""" UNIT TEST ON GRID MAP MODULE
# Description:
    This is the unit test for Grid Map module.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/06/09
"""
import os
import sys
import unittest

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)
from algorithms.graph.GridMap import GridMap, gridMap

class Test(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.g1 = GridMap(4, 4)
        self.g2 = gridMap(4, 4)
        
    def testGridMap(self):
        self.assertSetEqual(set(self.g1.neighbors((1,1))), set([(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (2, 1), (1, 2), (2, 2)]))
        self.assertSetEqual(set(self.g1.neighbors((1,0))), set([(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)]))
        self.assertSetEqual(set(self.g1.neighbors((3,3))), set([(3, 2), (2, 2), (2, 3)]))
    
    def testgridMap(self):
        self.assertSetEqual(set(self.g2.neighbors((1,1))), set([(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (2, 1), (1, 2), (2, 2)]))
        self.assertSetEqual(set(self.g2.neighbors((1,0))), set([(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)]))
        self.assertSetEqual(set(self.g2.neighbors((3,3))), set([(3, 2), (2, 2), (2, 3)]))

if __name__ == '__main__':
    unittest.main(verbosity=1)  
