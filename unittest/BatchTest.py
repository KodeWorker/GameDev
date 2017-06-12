""" BATCH TEST ON ALL UNIT TESTS
# Description:
    This is the batch test file for all the unit test in this folder.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/06/09
# Reference: https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory
"""

import os
import unittest

def Main():
    current_script = os.path.basename(__file__)    
    test_files = [x[2] for x in os.walk(os.path.dirname(__file__))][0]
    testmodules = [x[:-3] for x in test_files if x != current_script]
    suite = unittest.TestSuite()
    
    for t in testmodules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['suite'])
            suitefn = getattr(mod, 'suite')
            suite.addTest(suitefn())
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

    unittest.TextTestRunner().run(suite)
    
if __name__ == '__main__':
    Main()



