# -*- coding: utf-8 -*-
"""
file_utils module to hold simple bioinformatics course text file parsing class
"""

INPUT_STRING = 'Input'
OUTPUT_STRING = 'Output'


class FileUtil(object):
    """
    Holds I/O values parsed from course text files for example problems
    Initialized with a text file, parses 'Input' and 'Output' values to
    object attributes.

    Args:
        filename (str): filename pointing to supplied text file

    Attributes:
        inputs (list): inputs from supplied text file
        outputs (list): expected outputs from supplied text file
    """
    def __init__(self, filename):
        self.parse_file(filename)

    def parse_file(self, filename):
        """
        Helper function parses course text files and returns the list
        of inputs and, if provided, the list of expected outputs
        If no input string is found all items before output string are
        returned to inputs, if neither input string nor output string is
        found then all items are returned to input string.
        Space delimited strings are separated.

        Args:
            filename (str): filename pointing to supplied text file

        Returns:
            inputs (list): inputs from supplied text file
            outputs (list): expected outputs from supplied text file
        """
        with open(filename, 'r') as f:
            raw_text = f.read()
        raw_args = [s for i in raw_text.splitlines() for s in i.split(' ')]
        try:
            input_index = raw_args.index(INPUT_STRING)
        except ValueError:
            input_index = -1
        try:
            output_index = raw_args.index(OUTPUT_STRING)
        except ValueError:
            output_index = len(raw_args)
        self.inputs = raw_args[input_index+1:output_index]
        self.outputs = raw_args[output_index+1:]
