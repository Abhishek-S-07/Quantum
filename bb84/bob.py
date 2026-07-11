import numpy as np


class Bob:
    """
    Bob receives the quantum states sent by Alice and measures them
    using randomly selected bases according to the BB84 protocol.
    """

    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.bases = None
        self.measured_bits = None

    def generate_bases(self):
        """
        Generate Bob's random measurement bases.

        0 = Rectilinear (+)
        1 = Diagonal (×)
        """
        self.bases = np.random.randint(0, 2, self.num_qubits)
        return self.bases

    def measure(self, alice_states):
        """
        Measure Alice's transmitted states.

        If Alice's basis matches Bob's basis:
            Bob measures the correct bit.

        Otherwise:
            Bob obtains a random bit.
        """

        if self.bases is None:
            self.generate_bases()

        measured = []

        for (alice_bit, alice_basis), bob_basis in zip(alice_states, self.bases):

            if alice_basis == bob_basis:

                measured.append(alice_bit)

            else:

                measured.append(np.random.randint(0, 2))

        self.measured_bits = np.array(measured)

        return self.measured_bits

    def get_data(self):
        """
        Return Bob's generated data.
        """

        return {
            "bases": self.bases,
            "measured_bits": self.measured_bits
        }