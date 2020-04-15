import sys
import shutil
sys.path.append('../../')
import unittest
import os
from utils.CreateTemplate import *

class Test_Template(unittest.TestCase):

    def test_GetCurrentDirectory(self):
        self.assertEqual(GetCurrentDirectory(),os.getcwd())

    def test_CreateDirectory(self):
        try:
            CreateDirectory('New')
            self.assertTrue(os.path.exists(str(os.getcwd())+'/New'))
            self.assertRaises(OSError,CreateDirectory('New'))
            os.rmdir(str(os.getcwd())+'/New')
        except Exception as e:
            print(e)


    def test_Generator(self):
        root_dir=str(os.getcwd())
        try:
            Generator(root_dir)
            for i in range(0,len(layer1)):
                layerName = root_dir+'/'+str(layer1_names[i])
                for j in range(0,len(layer1[i])):
                    dirName = layerName +'/'+str(layer1[i][j])
                    self.assertTrue(os.path.exists(dirName))
                    for i in layer1_names:
                        shutil.rmtree(i)
        except Exception as e:
            print(e)
