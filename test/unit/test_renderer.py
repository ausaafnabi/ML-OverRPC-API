import sys
sys.path.append('../../')
import unittest
from core.Renderer.FileRenderer import *

class Test_Renderer(unittest.TestCase):

    def test_Renderer(self):
        Renderer('Test','.py',"HelloWorld")
        virtualcode_read=""
        virtualcode_wrote=""

        with open(Renderer.file,'r') as file:
            for i in file.readlines():
                virtualcode_read+=i
            for i in Renderer.dep:
                virtualcode_wrote+=i
        self.assertEqual(virtualcode_read,virtualcode_wrote)
