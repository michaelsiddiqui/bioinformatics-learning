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
PATTERN_COUNT_TEST_FNAMES = [
    fname for fname in os.listdir(FIXTURE_PATH) if 'PatternCountTest' in fname
]
PATTERN_COUNT_TEST_FNAMES.sort()


class TestDnaFreqCalcMethods(unittest.TestCase):
    """
    Test methods of DnaFreqCalc class from course examples
    """
    def test_pattern_count_sample(self):
        """
        Test the pattern_count method using the SamplePatternCount.txt inputs

        From prompt: The sample dataset is not actually run on your code.
        Notice that “GCG” occurs twice in Text: once at the beginning (GCG​CG)
        and once at the end (GCGCG​). A common mistake for this problem is
        incorrectly handling overlaps and not counting the second of these two
        occurrences (because it begins at the end of the previous occurrence).
        The sample dataset checks for the following things:
        * Off­by­one at the beginning of Text (result would be 1)
        * Off­by­one at the end of Text (result would be 1)
        * Not counting overlaps (result would be 1)
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

    def test_pattern_count_test_one(self):
        """
        Test the pattern_count method using the TEST DATASET 1 fixture

        Saved in PatternCountTest1.txt
        This dataset just checks if you’re correctly counting.
        It is the “easiest” test. Notice that all occurrences of CG in Text
        (ACG​TACG​TACG​T) are away from the very edges (so your code won’t fail
        on off­by­one errors at the beginning or at the end of Text) and that
        none of the occurrences of Pattern overlap (so your code won’t fail if
        you fail to account for overlaps).
        """
        fname = PATTERN_COUNT_TEST_FNAMES[0]
        fpath = os.path.join(FIXTURE_PATH, fname)
        file_util_obj = FileUtil(fpath)
        inputs = file_util_obj.inputs
        expected = int(file_util_obj.outputs[0])
        sequence_obj = DnaFreqCalc(inputs[0])
        actual = sequence_obj.pattern_count(inputs[1])
        self.assertEqual(expected, actual)

    def test_pattern_count_test_two(self):
        """
        Test the pattern_count method using the TEST DATASET 2 fixture

        Saved in PatternCountTest2.txt
        This dataset checks if your code correctly handles cases where there
        is an occurrence of Pattern at the very beginning of Text.
        Note that there are no overlapping occurrences of Pattern (i.e. AAAA),
        and there is no occurrence of Pattern at the very end of Text,
        so assuming your code passed Test Dataset 1, this test would only check
        for off­by­one errors at the beginning of Text.
        """
        fname = PATTERN_COUNT_TEST_FNAMES[1]
        fpath = os.path.join(FIXTURE_PATH, fname)
        file_util_obj = FileUtil(fpath)
        inputs = file_util_obj.inputs
        expected = int(file_util_obj.outputs[0])
        sequence_obj = DnaFreqCalc(inputs[0])
        actual = sequence_obj.pattern_count(inputs[1])
        self.assertEqual(expected, actual)
