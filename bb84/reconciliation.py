"""
===========================================================
QuantumSecureNet

Simplified Parity-Based Error Reconciliation

This module performs a simplified parity-based reconciliation
after BB84 key sifting.

It is intended for educational demonstration purposes and is
NOT a full Cascade implementation.

===========================================================
"""

from typing import List, Tuple


class ErrorReconciliation:
    """
    Simplified parity-based error reconciliation.
    """

    def __init__(self, block_size: int = 8):
        self.block_size = block_size

    @staticmethod
    def parity(bits: List[int]) -> int:
        """
        Compute the parity of a block.

        Returns
        -------
        0 : Even parity
        1 : Odd parity
        """
        return sum(bits) % 2

    def reconcile(
        self,
        alice_key: List[int],
        bob_key: List[int]
    ) -> Tuple[List[int], int, float]:
        """
        Perform simplified parity-based reconciliation.

        Parameters
        ----------
        alice_key : List[int]
        bob_key : List[int]

        Returns
        -------
        Tuple[List[int], int, float]

        corrected_key
        corrected_errors
        correction_rate
        """

        corrected_key = list(bob_key)

        corrected_errors = 0

        length = min(len(alice_key), len(corrected_key))

        for start in range(0, length, self.block_size):

            end = min(start + self.block_size, length)

            alice_block = alice_key[start:end]

            bob_block = corrected_key[start:end]

            alice_parity = self.parity(alice_block)

            bob_parity = self.parity(bob_block)

            if alice_parity != bob_parity:

                # Simplified correction:
                # Correct the first mismatching bit
                # within the current block.

                for i in range(len(alice_block)):

                    if alice_block[i] != bob_block[i]:

                        corrected_key[start + i] = alice_block[i]

                        corrected_errors += 1

                        break

        correction_rate = 0.0

        if length > 0:

            correction_rate = corrected_errors / length

        return (

            corrected_key,

            corrected_errors,

            correction_rate,

        )

    @staticmethod
    def keys_match(
        alice_key: List[int],
        bob_key: List[int]
    ) -> bool:
        """
        Check whether both keys are identical.
        """

        return alice_key == bob_key

    @staticmethod
    def mismatch_count(
        alice_key: List[int],
        bob_key: List[int]
    ) -> int:
        """
        Count mismatching bits.
        """

        return sum(

            1

            for a, b in zip(alice_key, bob_key)

            if a != b

        )

    @staticmethod
    def reconciliation_summary(
        before_errors: int,
        corrected_errors: int,
        key_length: int
    ) -> dict:
        """
        Return reconciliation statistics.
        """

        remaining_errors = max(

            before_errors - corrected_errors,

            0,

        )

        accuracy = 0.0

        if key_length > 0:

            accuracy = (

                (key_length - remaining_errors)

                / key_length

            ) * 100

        return {

            "Initial Errors": before_errors,

            "Corrected Errors": corrected_errors,

            "Remaining Errors": remaining_errors,

            "Accuracy (%)": round(accuracy, 2),

        }


def reconcile_keys(
    alice_key: List[int],
    bob_key: List[int]
) -> List[int]:
    """
    Compatibility function used by protocol.py.

    Returns only the corrected key.
    """

    reconciler = ErrorReconciliation()

    corrected_key, _, _ = reconciler.reconcile(

        alice_key,

        bob_key,

    )

    return corrected_key