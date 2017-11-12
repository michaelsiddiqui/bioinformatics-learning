# -*- coding: utf-8 -*-
"""
dna_utils module to hold simple utility functions/classes
"""

from collections import Counter

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

class DnaFreqCalc(DnaUtil):
    """
    Holds a DNA sequence. Enables quick calculation of relevant frequency data
    """
    def pattern_count(self, pattern):
        """
        Initial pattern_count method
        """
        count = 0
        pattern_util_obj = DnaUtil(pattern)
        pattern_len = len(pattern)
        diff_length = len(self.sequence) - pattern_len
        for i in range(diff_length + 1):
            end = i + pattern_len
            window_text = self.sequence[i:end]
            if window_text == pattern:
                count +=1
        return count

    def frequent_kmers(self, k):
        """
        Initial frequent_kmers methods
        """
        diff_length = len(self.sequence) - k
        kmer_list = []
        for i in range(diff_length + 1):
            kmer_list.append(self.sequence[i: i+ k])
        kmer_frequency = Counter(kmer_list)
        return kmer_frequency

    def most_frequent_kmers(self, k):
        """
        List the most frequent kmers in the object's sequence

        Use the 'frequent_kmers' method to get Counter object
        use most_common() method and then retun all keys with
        values equal to the value of the most most_common element
        """
        kmer_frequency = self.frequent_kmers(k)
        most_freq = kmer_frequency.most_common(1)
        high_count = most_freq[1]
        list_most_frequent_kmers = [
            key for key, val in kmer_frequency.iteritems if val == high_count
        ]
        return list_most_frequent_kmers
