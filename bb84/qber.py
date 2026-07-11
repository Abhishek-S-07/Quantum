"""
===========================================================
QuantumSecureNet

Quantum Bit Error Rate (QBER) Module

Calculates the Quantum Bit Error Rate between Alice's
and Bob's sifted keys.

===========================================================
"""


class QBERCalculator:
    """
    Quantum Bit Error Rate (QBER) Calculator.

    QBER = (Number of Different Bits / Total Sifted Bits) × 100
    """

    def __init__(self):

        self.total_bits = 0
        self.error_bits = 0
        self.qber = 0.0

    def calculate(self, alice_key, bob_key):
        """
        Calculate the QBER.

        Parameters
        ----------
        alice_key : list
        bob_key : list

        Returns
        -------
        float
            QBER percentage.
        """

        if len(alice_key) != len(bob_key):
            raise ValueError(
                "Alice and Bob keys must have the same length."
            )

        self.total_bits = len(alice_key)
        self.error_bits = 0

        if self.total_bits == 0:
            self.qber = 0.0
            return self.qber

        for alice_bit, bob_bit in zip(
            alice_key,
            bob_key
        ):

            if alice_bit != bob_bit:
                self.error_bits += 1

        self.qber = (
            self.error_bits /
            self.total_bits
        ) * 100

        return round(self.qber, 2)

    def get_statistics(self):
        """
        Return QBER statistics.
        """

        return {

            "total_bits": self.total_bits,

            "error_bits": self.error_bits,

            "qber": round(self.qber, 2)

        }


def calculate_qber(alice_key, bob_key):
    """
    Convenience function used by protocol.py.

    Parameters
    ----------
    alice_key : list
    bob_key : list

    Returns
    -------
    float
        QBER percentage.
    """

    calculator = QBERCalculator()

    return calculator.calculate(
        alice_key,
        bob_key
    )