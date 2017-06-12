""" UNIT TEST ON LANGUAGE MODULE
# Description:
    This is the unit test for gamedev.Language module.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/06/09
"""
import os
import sys
import unittest

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)

from algorithms.procedual_generation.Language import consonants, vowels,\
sibilants, liquids, finals, structures, restrictions, consonant_orthography_set,\
vowel_orthography_set
from algorithms.procedual_generation.Language import LangGen

class Test(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        consonant = list(consonants.keys())[0]
        vowel = list(vowels.keys())[0]
        sibilant = list(sibilants.keys())[0]
        liquid = list(liquids.keys())[0]
        final = list(finals.keys())[0]
        structure = sorted(list(structures))[0]
        restriction = sorted(list(restrictions))[0]
        consonant_orthography_type = list(consonant_orthography_set.keys())[0]
        vowel_orthography_type = list(vowel_orthography_set.keys())[0]
    
        self.l = LangGen(consonant, vowel, sibilant, liquid, final, structure, restriction, consonant_orthography_type, vowel_orthography_type, random_seed=1)
        
    def testLangGen(self):
        name = self.l.genName(1,3)
        self.assertEqual(name,'Lellel')
        
if __name__ == '__main__':
    unittest.main(verbosity=1)  
