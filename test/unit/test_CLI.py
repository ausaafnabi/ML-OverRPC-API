import sys
sys.path.append('../../')
import unittest
from CLI import *
from PyInquirer import (ValidationError,Validator)

class Test_CLI(unittest.TestCase):
    def test_CLI_EmptyValidator(self):
        self.value1= EmptyValidator()
        self.value2= EmptyValidator()

        self.assertTrue(self.value1.validate('Sometext'))
        self.assertRaises(ValidationError,self.value2.validate(''))
