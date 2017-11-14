# -*- coding: utf-8 -*-
"""
dna_freq_calc module to hold the DnaFreqCalc class for solving course problems
"""

from collections import Counter
from dna_utils import DnaUtil


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
        pattern_len = len(pattern_util_obj.sequence)
        diff_length = len(self.sequence) - pattern_len
        for i in range(diff_length + 1):
            end = i + pattern_len
            window_text = self.sequence[i:end]
            if window_text == pattern_util_obj.sequence:
                count += 1
        return count

    def frequent_kmers(self, k):
        """
        Initial frequent_kmers methods
        """
        k = int(k)
        diff_length = len(self.sequence) - k
        kmer_list = []
        for i in range(diff_length + 1):
            kmer_list.append(self.sequence[i: i + k])
        kmer_frequency = Counter(kmer_list)
        return kmer_frequency

    def most_frequent_kmers(self, k):
        """
        List the most frequent kmers in the object's sequence

        Use the 'frequent_kmers' method to get Counter object
        use most_common() method and then retun all keys with
        values equal to the value of the most most_common element
        """
        kmer_freq = self.frequent_kmers(k)
        most_freq = kmer_freq.most_common(1)
        high_count = most_freq[0][1]
        list_most_frequent_kmers = [
            key for key, val in kmer_freq.iteritems() if val == high_count
        ]
        return list_most_frequent_kmers
