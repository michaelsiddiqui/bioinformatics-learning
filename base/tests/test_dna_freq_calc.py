# -*- coding: utf-8 -*-
"""
Test module for DnaFreqCalc classes within the bioinformatics-learning package

file_utils unittest.TestCase classes:
* TestDnaFreqCalcMethods

Todo:
    * Test additional classes added to solve course prompts

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html
"""

import os
import unittest

from base.dna_freq_calc import DnaFreqCalc
from base.file_utils import FileUtil
from base.tests.fixtures import FIXTURE_PATH

FIXTURE1_FNAME = 'SamplePatternCount.txt'
FIXTURE2_FNAME = 'PatternCount.txt'
FIXTURE1_FPATH = os.path.join(FIXTURE_PATH, FIXTURE1_FNAME)
FIXTURE2_FPATH = os.path.join(FIXTURE_PATH, FIXTURE2_FNAME)


class TestDnaFreqCalcMethods(unittest.TestCase):
    """
    Test methods of DnaFreqCalc class from course examples
    """
    def test_pattern_count_sample(self):
        """
        Test the pattern_count method using the SamplePatternCount.txt inputs
        """
        file_util_obj = FileUtil(FIXTURE1_FPATH)
        inputs = file_util_obj.inputs
        expected = int(file_util_obj.outputs[0])
        sequence_obj = DnaFreqCalc(inputs[0])
        actual = sequence_obj.pattern_count(inputs[1])
        self.assertEqual(expected, actual)

    def test_pattern_count_extra_dataset(self):
        """
        Test the pattern_count method using the PatternCount.txt fixture

        The course prompt called this the "Extra Dataset"
        """
        file_util_obj = FileUtil(FIXTURE2_FPATH)
        inputs = file_util_obj.inputs
        expected = int(file_util_obj.outputs[0])
        sequence_obj = DnaFreqCalc(inputs[0])
        actual = sequence_obj.pattern_count(inputs[1])
        self.assertEqual(expected, actual)
