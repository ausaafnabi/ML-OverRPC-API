import sys
sys.path.append('../../')
import unittest
from core.Renderer.FileRenderer import *

class Test_Renderer(unittest.TestCase):

    def test_Renderer(self):
        Renderer('Test','.py',"HelloWorld")
        virtualcode=""
        with open('Test.py','r') as file:
            for i in file.readlines():
                virtualcode+=i
            self.assertEqual(strfile[0],virtualcode)
