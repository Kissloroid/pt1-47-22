import unittest
from ddt import ddt
from ddt import data
from ddt import unpack
from task13 import matching_with_elements


@ddt
class TestSuiteMatchingWithElements(unittest.TestCase):
    """Test for translating an input word
    into a word made up of the names of chemical elements"""
    @data(('silicon', ' SiLiCON'), ('Silver', 'SiLvEr'))
    @unpack
    def test_max_divisor(self, name, expected_result):
        """

        :param name:             input word
        :param expected_result:  output word
        """
        self.assertEqual(matching_with_elements(name), expected_result)
