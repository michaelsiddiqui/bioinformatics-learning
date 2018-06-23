# -*- coding: utf-8 -*-
"""
Test module for the DnaUtil class within the bioinformatics-learning package

file_utils unittest.TestCase classes:
* TestDnaUtilsMethods

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html
"""

import os
import unittest

from base.dna_utils import DnaUtil
from base.file_utils import FileUtil
from base.tests.fixtures import FIXTURE_PATH

GOOD_DNA = 'ACGTACGT'
LOWER_DNA = 'acgtacgt'
BAD_DNA = 'ACGBT2'
TEST_FWD_SEQ = 'AATTGGCC'
TEST_REV_COMP_SEQ = 'GGCCAATT'

FIXTURE1_FNAME = 'SampleReverseComplement.txt'
FIXTURE2_FNAME = 'ReverseComplement.txt'
FIXTURE3_FNAME = 'ReverseComplementTest1.txt'
FIXTURE4_FNAME = 'SampleLocatePattern.txt'
FIXTURE5_FNAME = 'LocatePattern1.txt'
FIXTURE6_FNAME = 'LocatePattern2.txt'
FIXTURE7_FNAME = 'LocatePattern3.txt'
FIXTURE8_FNAME = 'LocatePattern4.txt'
FIXTURE1_FPATH = os.path.join(FIXTURE_PATH, FIXTURE1_FNAME)
FIXTURE2_FPATH = os.path.join(FIXTURE_PATH, FIXTURE2_FNAME)
FIXTURE3_FPATH = os.path.join(FIXTURE_PATH, FIXTURE3_FNAME)
FIXTURE4_FPATH = os.path.join(FIXTURE_PATH, FIXTURE4_FNAME)
FIXTURE5_FPATH = os.path.join(FIXTURE_PATH, FIXTURE5_FNAME)
FIXTURE6_FPATH = os.path.join(FIXTURE_PATH, FIXTURE6_FNAME)
FIXTURE7_FPATH = os.path.join(FIXTURE_PATH, FIXTURE7_FNAME)
FIXTURE8_FPATH = os.path.join(FIXTURE_PATH, FIXTURE8_FNAME)


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

    def test_reverse_complement_from_sample_dataset(self):
        """
        Test reverse_complement method with 'Sample' dataset
        """
        file_util_obj = FileUtil(FIXTURE1_FPATH)
        inputs = file_util_obj.inputs
        expected = file_util_obj.outputs[0]
        sequence_obj = DnaUtil(inputs[0])
        actual = sequence_obj.reverse_complement()
        self.assertEqual(expected, actual)

    def test_reverse_complement_from_extra_dataset(self):
        """
        Test reverse_complement method with 'Extra' dataset
        """
        file_util_obj = FileUtil(FIXTURE2_FPATH)
        inputs = file_util_obj.inputs
        expected = file_util_obj.outputs[0]
        sequence_obj = DnaUtil(inputs[0])
        actual = sequence_obj.reverse_complement()
        self.assertEqual(expected, actual)

    def test_reverse_complement_from_test_dataset_one(self):
        """
        Test reverse_complement method with 'Test' dataset
        """
        file_util_obj = FileUtil(FIXTURE3_FPATH)
        inputs = file_util_obj.inputs
        expected = file_util_obj.outputs[0]
        sequence_obj = DnaUtil(inputs[0])
        actual = sequence_obj.reverse_complement()
        self.assertEqual(expected, actual)

    def test_locate_pattern_from_sample_dataset(self):
        """
        Test locate_pattern method with 'Sample' dataset
        """
        file_util_obj = FileUtil(FIXTURE4_FPATH)
        inputs = file_util_obj.inputs
        expected = file_util_obj.outputs
        sequence_obj = DnaUtil(inputs[1])
        actual = sequence_obj.locate_pattern_in_sequence(inputs[0])
        self.assertEqual(expected, actual)

    def test_locate_pattern_from_dataset_one(self):
        """
        Test locate_pattern method with 'Test' dataset one
        """
        file_util_obj = FileUtil(FIXTURE5_FPATH)
        inputs = file_util_obj.inputs
        expected = file_util_obj.outputs
        sequence_obj = DnaUtil(inputs[1])
        actual = sequence_obj.locate_pattern_in_sequence(inputs[0])
        self.assertEqual(expected, actual)

    def test_locate_pattern_from_dataset_two(self):
        """
        Test locate_pattern method with 'Test' dataset two
        """
        file_util_obj = FileUtil(FIXTURE6_FPATH)
        inputs = file_util_obj.inputs
        expected = file_util_obj.outputs
        sequence_obj = DnaUtil(inputs[1])
        actual = sequence_obj.locate_pattern_in_sequence(inputs[0])
        self.assertEqual(expected, actual)

    def test_locate_pattern_from_dataset_three(self):
        """
        Test locate_pattern method with 'Test' dataset three
        """
        file_util_obj = FileUtil(FIXTURE7_FPATH)
        inputs = file_util_obj.inputs
        expected = file_util_obj.outputs
        sequence_obj = DnaUtil(inputs[1])
        actual = sequence_obj.locate_pattern_in_sequence(inputs[0])
        self.assertEqual(expected, actual)

    def test_locate_pattern_from_dataset_four(self):
        """
        Test locate_pattern method with 'Test' dataset four
        """
        file_util_obj = FileUtil(FIXTURE8_FPATH)
        inputs = file_util_obj.inputs
        expected = file_util_obj.outputs
        sequence_obj = DnaUtil(inputs[1])
        actual = sequence_obj.locate_pattern_in_sequence(inputs[0])
        self.assertEqual(expected, actual)
