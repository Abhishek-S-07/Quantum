"""
QuantumSecureNet
----------------
Privacy Amplification Module

This module performs privacy amplification on the reconciled key
using SHA-256 hashing.

Purpose:
Reduce any partial information that an eavesdropper may have about
the reconciled key by compressing it into a shorter secure key.

This implementation is intended for educational demonstration of
the BB84 protocol workflow.
"""

import hashlib
from typing import List


class PrivacyAmplification:
    """
    Performs hash-based privacy amplification.
    """

    def __init__(self, output_length: int = 256):
        """
        Parameters
        ----------
        output_length : int
            Desired length of the final key in bits.
            Maximum supported = 256 (SHA-256 output size).
        """

        self.output_length = min(output_length, 256)

    @staticmethod
    def bits_to_string(bits: List[int]) -> str:
        """
        Convert a list of bits into a binary string.

        Example:
        [1,0,1,1] -> "1011"
        """

        return "".join(str(bit) for bit in bits)

    @staticmethod
    def string_to_bits(binary_string: str) -> List[int]:
        """
        Convert a binary string into a list of bits.

        Example:
        "1011" -> [1,0,1,1]
        """

        return [int(bit) for bit in binary_string]

    def generate_secure_key(self, reconciled_key: List[int]) -> List[int]:
        """
        Apply SHA-256 privacy amplification.

        Parameters
        ----------
        reconciled_key : List[int]

        Returns
        -------
        List[int]
            Final secure key after privacy amplification.
        """

        if len(reconciled_key) == 0:
            return []

        binary_key = self.bits_to_string(reconciled_key)

        hash_object = hashlib.sha256(binary_key.encode())

        hex_digest = hash_object.hexdigest()

        binary_digest = bin(int(hex_digest, 16))[2:].zfill(256)

        secure_key = binary_digest[:self.output_length]

        return self.string_to_bits(secure_key)

    @staticmethod
    def key_statistics(original_key: List[int], secure_key: List[int]) -> dict:
        """
        Generate statistics about the amplification process.
        """

        reduction = len(original_key) - len(secure_key)

        reduction_percent = 0

        if len(original_key) > 0:

            reduction_percent = (
                reduction / len(original_key)
            ) * 100

        return {

            "Original Key Length": len(original_key),

            "Final Key Length": len(secure_key),

            "Bits Removed": reduction,

            "Compression (%)": round(reduction_percent, 2)

        }

    @staticmethod
    def display_key(bits: List[int], max_length: int = 64) -> str:
        """
        Return a readable version of the key.

        Long keys are truncated for dashboard display.
        """

        key = "".join(map(str, bits))

        if len(key) <= max_length:
            return key

        return key[:max_length] + " ..."