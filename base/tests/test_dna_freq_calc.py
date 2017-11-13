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
FIXTURE3_FNAME = 'SampleFrequentKmers.txt'
FIXTURE4_FNAME = 'FrequentKmers.txt'
FIXTURE1_FPATH = os.path.join(FIXTURE_PATH, FIXTURE1_FNAME)
FIXTURE2_FPATH = os.path.join(FIXTURE_PATH, FIXTURE2_FNAME)
FIXTURE3_FPATH = os.path.join(FIXTURE_PATH, FIXTURE3_FNAME)
FIXTURE4_FPATH = os.path.join(FIXTURE_PATH, FIXTURE3_FNAME)
PATTERN_COUNT_TEST_FNAMES = [
    fname for fname in os.listdir(FIXTURE_PATH) if 'PatternCountTest' in fname
]
PATTERN_COUNT_TEST_FNAMES.sort()


class TestDnaFreqCalc(unittest.TestCase):
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

    def test_pattern_count_test_three(self):
        """
        Test the pattern_count method using the TEST DATASET 3 fixture

        Saved in PatternCountTest3.txt
        This dataset checks if your code correctly handles cases where there
        is an occurrence of Pattern at the very end of Text.
        Note that there are no overlapping occurrences of Pattern (i.e. AAAA),
        and there is no occurrence of Pattern at the very beginning of Text,
        so assuming your code passed Test Dataset 2, this test would only check
        for off­by­one errors at the end of Text.
        """
        fname = PATTERN_COUNT_TEST_FNAMES[2]
        fpath = os.path.join(FIXTURE_PATH, fname)
        file_util_obj = FileUtil(fpath)
        inputs = file_util_obj.inputs
        expected = int(file_util_obj.outputs[0])
        sequence_obj = DnaFreqCalc(inputs[0])
        actual = sequence_obj.pattern_count(inputs[1])
        self.assertEqual(expected, actual)

    def test_pattern_count_test_four(self):
        """
        Test the pattern_count method using the TEST DATASET 3 fixture

        Saved in PatternCountTest3.txt
        This test dataset checks if your code is also counting occurrences of
        the Reverse Complement of Pattern (which would have an output of 4),
        which is out of the scope of this problem (that will come up later in
        the chapter). Your code should only be looking for perfect matches of
        Pattern in Text at this point.
        """
        fname = PATTERN_COUNT_TEST_FNAMES[3]
        fpath = os.path.join(FIXTURE_PATH, fname)
        file_util_obj = FileUtil(fpath)
        inputs = file_util_obj.inputs
        expected = int(file_util_obj.outputs[0])
        sequence_obj = DnaFreqCalc(inputs[0])
        actual = sequence_obj.pattern_count(inputs[1])
        self.assertEqual(expected, actual)

    def test_most_frequent_kmer_sample(self):
        """
        Test the pattern_count method using the SamplePatternCount.txt inputs

        From prompt: The sample dataset is not actually run on your code.
        """
        file_util_obj = FileUtil(FIXTURE3_FPATH)
        inputs = file_util_obj.inputs
        expected = file_util_obj.outputs
        sequence_obj = DnaFreqCalc(inputs[0])
        actual = sequence_obj.most_frequent_kmers(inputs[1])
        self.assertEqual(expected, actual)

    def test_most_frequent_kmer_extra_dataset(self):
        """
        Test the pattern_count method using the FrequentKmers.txt fixture

        The course prompt called this the "Extra Dataset"
        """
        file_util_obj = FileUtil(FIXTURE4_FPATH)
        inputs = file_util_obj.inputs
        expected = file_util_obj.outputs
        sequence_obj = DnaFreqCalc(inputs[0])
        actual = sequence_obj.most_frequent_kmers(inputs[1])
        self.assertEqual(expected, actual)
