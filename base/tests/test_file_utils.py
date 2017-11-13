# -*- coding: utf-8 -*-
"""
Test module for file_utils classes within the bioinformatics-learning package

file_utils unittest.TestCase classes:
* Test TestFileUtilsFromCourseExamples

Todo:
    * Additional TestCase for input file without 'Input' or 'Output' strings
    * Additional TestCase for input file with space-delimited lines

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html
"""

import os
import unittest

from base.file_utils import FileUtil
from base.tests.fixtures import FIXTURE_PATH

FIXTURE1_FNAME = 'SamplePatternCount.txt'
FIXTURE2_FNAME = 'empty_file.txt'
FIXTURE3_FNAME = 'SampleFrequentKmers.txt'
FIXTURE1_FPATH = os.path.join(FIXTURE_PATH, FIXTURE1_FNAME)
FIXTURE2_FPATH = os.path.join(FIXTURE_PATH, FIXTURE2_FNAME)
FIXTURE3_FPATH = os.path.join(FIXTURE_PATH, FIXTURE3_FNAME)


class TestFileUtilsFromCourseExamples(unittest.TestCase):
    """
    TestCase class to test parsing example text files from course material

    methods in this TestCase class:
    * test_parse_sample_pattern_count_file
    * test_empty_file_resolves_empty_lists
    """

    def test_parse_sample_pattern_count_file(self):
        """
        Test parsing a text file with inputs and outputs for first prompt
        """
        expected_inputs = ['GCGCG', 'GCG']
        expected_outputs = ['2']
        file_util_obj = FileUtil(FIXTURE1_FPATH)
        actual_inputs = file_util_obj.inputs
        actual_outputs = file_util_obj.outputs
        self.assertEqual(expected_inputs, actual_inputs)
        self.assertEqual(expected_outputs, actual_outputs)

    def test_empty_file_resolves_empty_lists(self):
        """
        Test that when a file with no contents is supplied lists are empty
        """
        file_util_obj = FileUtil(FIXTURE2_FPATH)
        actual_inputs = file_util_obj.inputs
        actual_outputs = file_util_obj.outputs
        self.assertEqual(actual_inputs, actual_outputs)
        self.assertEqual(actual_outputs, [])

    def test_input_file_with_space_delimited_content(self):
        """
        Test behavior when a file has space delimited strings on one line
        """
        expected_inputs = ['ACGTTGCATGTCGCATGATGCATGAGAGCT', '4']
        expected_outputs = ['CATG', 'GCAT']
        file_util_obj = FileUtil(FIXTURE3_FPATH)
        actual_inputs = file_util_obj.inputs
        actual_outputs = file_util_obj.outputs
        self.assertEqual(expected_inputs, actual_inputs)
        self.assertEqual(expected_outputs, actual_outputs)
