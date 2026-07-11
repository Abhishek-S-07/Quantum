"""
===========================================================
QuantumSecureNet

Eve Module

Simulates an Intercept-Resend Attack on the BB84 protocol.

===========================================================
"""

import numpy as np


class Eve:
    """
    Eve performs an intercept-resend attack.

    She randomly chooses measurement bases,
    measures Alice's transmitted qubits,
    and resends the measured qubits to Bob.
    """

    def __init__(self, num_qubits):

        self.num_qubits = num_qubits

        self.bases = None
        self.measured_bits = None
        self.resent_states = None

    def generate_bases(self):
        """
        Generate Eve's random measurement bases.

        0 = Rectilinear (+)
        1 = Diagonal (×)
        """

        self.bases = np.random.randint(
            0,
            2,
            self.num_qubits
        )

        return self.bases

    def intercept_resend(self, alice_states):
        """
        Perform the BB84 intercept-resend attack.

        Parameters
        ----------
        alice_states : list
            List of tuples (bit, basis)

        Returns
        -------
        list
            States resent by Eve.
        """

        if self.bases is None:
            self.generate_bases()

        measured_bits = []
        resent_states = []

        for (alice_bit, alice_basis), eve_basis in zip(
            alice_states,
            self.bases
        ):

            # If Eve guesses the correct basis,
            # she measures the correct bit.
            if alice_basis == eve_basis:

                measured_bit = alice_bit

            else:

                measured_bit = np.random.randint(0, 2)

            measured_bits.append(int(measured_bit))

            resent_states.append(
                (
                    int(measured_bit),
                    int(eve_basis)
                )
            )

        self.measured_bits = np.array(measured_bits)

        self.resent_states = resent_states

        return resent_states

    def get_data(self):
        """
        Return Eve's simulation data.
        """

        return {

            "eve_bases": self.bases,

            "eve_bits": self.measured_bits,

            "resent_states": self.resent_states

        }