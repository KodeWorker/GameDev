""" UNIT TEST ON PATH FINDING MODULE
# Description:
    This is the unit test for path finding module.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/06/08
"""
import os
import sys
import unittest

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)
from algorithms.graph.GridMap import GridMap
from algorithms.graph.PathFinding import PathFinding

class Test(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.g = GridMap(3, 3)
        self.g.remove_node((1,1))
        self.f = PathFinding(self.g)        
        
    def testPathFinder(self):
        path = self.f.get_path((0,0), (2,2))
        self.assertEqual(path, [(0, 0), (0, 1), (1, 2), (2, 2)])

if __name__ == '__main__':
    unittest.main(verbosity=1)  
