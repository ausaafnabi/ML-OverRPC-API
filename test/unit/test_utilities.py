import io
from contextlib import redirect_stdout
import sys
sys.path.append('../../')
import unittest
import os
from utils.utilities import *

class Test_utilities(unittest.TestCase):
    def test_Fetch_directories(self):
        subdirs= Fetch_directories(str(os.getcwd())+'/test')
        self.assertEqual(subdirs,['integration','unit'])

    def test_convert_date(self):
        self.assertEqual('12 Apr 2020',convert_date(1586718992))

    def test_get_latest_modified(self):
        capturedOutput = io.StringIO()
        with redirect_stdout(capturedOutput):
            get_latest_modified(str(os.getcwd())+'/test/unit/testobj')
            self.assertEqual('13-04-2020 Plz do Not Modify.txt Last Modified: 13 Apr 2020\n',capturedOutput.getvalue())


    def test_Pattern_Match(self):
        capturedOutput = io.StringIO()
        with redirect_stdout(capturedOutput):
            Pattern_Match(str(os.getcwd())+'/README.md')
            self.assertEqual(str(os.getcwd())+"/README.md\n",capturedOutput.getvalue())
        capturedOutput = io.StringIO()
        with redirect_stdout(capturedOutput):
            Pattern_Match(str(os.getcwd())+'/*.md')
            self.assertEqual(str(os.getcwd())+"\\README.md\n",capturedOutput.getvalue())
