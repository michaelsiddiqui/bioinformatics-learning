# -*- coding: utf-8 -*-
"""
Test module for dna_utils classes within the bioinformatics-learning package

file_utils unittest.TestCase classes:
* Test TestDnaUtilsMethods

Todo:
    * Test additional classes added to solve course prompts

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html
"""

import os
import unittest

from base.dna_utils import DnaUtil
from base.dna_utils import DnaFreqCalc
from base.file_utils import FileUtil
from base.tests.fixtures import FIXTURE_PATH

GOOD_DNA = 'ACGTACGT'
LOWER_DNA = 'acgtacgt'
BAD_DNA = 'ACGBT2'
TEST_FWD_SEQ = 'AATTGGCC'
TEST_REV_COMP_SEQ = 'GGCCAATT'

FIXTURE1_FNAME = 'SamplePatternCount.txt'
FIXTURE2_FNAME = 'PatternCount.txt'
FIXTURE1_FPATH = os.path.join(FIXTURE_PATH, FIXTURE1_FNAME)
FIXTURE2_FPATH = os.path.join(FIXTURE_PATH, FIXTURE2_FNAME)

class TestDnaUtilsMethods(unittest.TestCase):
    """
    TestCase class to test DnaUtil methods
    Want to make sure dna sequences are cast to uppercase,
    bad DNA sequences raise errors when supplied as input, and
    the reverse_complement function works as expected
    """
    def test_object_created_with_good_dna_sequence(self):
        """
        Test with a 'good' expected DNA sequence
        """
        dna_util_obj = DnaUtil(GOOD_DNA)
        expected = GOOD_DNA
        actual = dna_util_obj.sequence
        self.assertEqual(expected, actual)

    def test_object_created_with_lowercase_dna_sequence(self):
        """
        Test with a 'good lowercase' DNA sequence
        """
        dna_util_obj = DnaUtil(LOWER_DNA)
        expected = GOOD_DNA
        actual = dna_util_obj.sequence
        self.assertEqual(expected, actual)

    def test_raises_value_error_when_supplied_bad_sequence(self):
        """
        Test that DnaUtil.__init__ raises ValueError when given bad sequence
        """
        with self.assertRaises(ValueError) as c:
            DnaUtil(BAD_DNA)
        self.assertTrue(
            "IUPAC non-ambiguous DNA characters required" in c.exception)

    def test_reverse_complement_gives_correct_sequence(self):
        """
        Test reverse complement method with test sequences
        """
        dna_util_obj = DnaUtil(TEST_FWD_SEQ)
        expected = TEST_REV_COMP_SEQ
        actual = dna_util_obj.reverse_complement()
        self.assertEqual(expected, actual)

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
