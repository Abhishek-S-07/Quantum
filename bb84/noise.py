"""
===========================================================
QuantumSecureNet

Noise Channel Module

Simulates a depolarizing-like noisy quantum channel by
randomly flipping transmitted bits with a configurable
probability.

===========================================================
"""

import numpy as np


class QuantumNoise:
    """
    Simulates channel noise.

    Parameters
    ----------
    error_probability : float
        Probability of a transmitted bit flipping.
    """

    def __init__(self, error_probability=0.02):

        self.error_probability = error_probability

        self.total_errors = 0

    def apply(self, bit_sequence):
        """
        Apply channel noise.

        Parameters
        ----------
        bit_sequence : list or numpy array

        Returns
        -------
        list
            Noisy bit sequence.
        """

        bit_sequence = np.asarray(bit_sequence)

        noisy_bits = []

        self.total_errors = 0

        for bit in bit_sequence:

            bit = int(bit)

            if np.random.random() < self.error_probability:

                bit ^= 1

                self.total_errors += 1

            noisy_bits.append(bit)

        return noisy_bits

    def get_statistics(self):
        """
        Return channel statistics.
        """

        return {

            "error_probability": self.error_probability,

            "errors_introduced": self.total_errors,

        }
    