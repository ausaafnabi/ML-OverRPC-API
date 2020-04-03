import sys
sys.path.append('../../')
import unittest
import os
from utils.CreateTemplate import *

class Test_Template(unittest.TestCase):
    def test_GetCurrentDirectory(self):
        self.assertEqual(GetCurrentDirectory(),os.getcwd())


    def test_CreateDirectory(self):
            CreateDirectory('New')
            self.assertTrue(os.path.exists(str(os.getcwd())+'/New'))
            self.assertRaises(OSError,CreateDirectory,'New')



    def test_Generator(self):
        Generator(os.getcwd())
        self.assertTrue(os.path.exists(str(os.getcwd()+'/overviewDirectory1/A1')))
        self.assertTrue(os.path.exists(str(os.getcwd()+'/overviewDirectory1/A2')))
        self.assertTrue(os.path.exists(str(os.getcwd()+'/overviewDirectory2/B1')))
        self.assertTrue(os.path.exists(str(os.getcwd()+'/overviewDirectory2/B2')))
