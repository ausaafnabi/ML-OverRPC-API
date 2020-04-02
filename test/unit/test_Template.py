import sys
sys.path.append('../../')
import unittest
import os
from utils.CreateTemplate import * #or import CreateTemplate

class Test_Template(unittest.TestCase):
    def test_GetCurrentDirectory(self):
        self.assertEqual(GetCurrentDirectory(),os.getcwd())
