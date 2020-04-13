import sys
from contextlib import contextmanager
from io import StringIO
sys.path.append('../../')
import unittest
from CLI import *
from PyInquirer import (ValidationError,Validator)


class Test_CLI(unittest.TestCase):

    def test_askProjectInfo(self):
