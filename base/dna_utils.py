# -*- coding: utf-8 -*-
"""
dna_utils module to hold a simple utility class, DnaUtil
"""


DNA_ALPHABET = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A'
}


class DnaUtil(object):
    """
    Holds DNA sequence string data enables simple sequence methods.
    Automatically checks that characters provided in the input string
    are unambiguous DNA characters and casts all strings to uppercase.

    Args:
        sequence (str): DNA sequence provided

    Attributes:
        sequence (str): DNA sequence stored
        DNA_ALPHABET (dict): lookup to validate accepted characters and
            implement reverse complement calculation
    """
    def __init__(self, sequence):
        self.DNA_ALPHABET = DNA_ALPHABET
        sequence = str(sequence)
        sequence = sequence.upper()
        self.sequence = sequence
        self.char_check()

    def __str__(self):
        return "DnaUtil object with DNA sequence: '{}'".format(self.sequence)

    def char_check(self):
        """check that current stored sequence contains only accepted DNA
        characters
        """
        accepted_chars = set(self.DNA_ALPHABET.keys())
        if not set(self.sequence).issubset(accepted_chars):
            raise ValueError(
                "IUPAC non-ambiguous DNA characters required"
                )

    def reverse_complement(self):
        """return a string that is the reverse complement of the stored
        DNA sequence
        """
        reverse_dna = self.sequence[::-1]
        output = ''.join([
            self.DNA_ALPHABET[base] for base in reverse_dna
        ])
        return output
