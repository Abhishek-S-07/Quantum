import numpy as np


class Alice:
    """
    Alice generates the original random bit string and
    random measurement bases used in the BB84 protocol.
    """

    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.bits = None
        self.bases = None

    def generate_bits(self):
        """
        Generate random classical bits.
        """
        self.bits = np.random.randint(0, 2, self.num_qubits)
        return self.bits

    def generate_bases(self):
        """
        Generate random bases.
        0 = Rectilinear (+)
        1 = Diagonal (×)
        """
        self.bases = np.random.randint(0, 2, self.num_qubits)
        return self.bases

    def prepare_states(self):
        """
        Prepare conceptual BB84 quantum states.

        Returns a list of tuples:
        (bit, basis)
        """

        if self.bits is None:
            self.generate_bits()

        if self.bases is None:
            self.generate_bases()

        states = []

        for bit, basis in zip(self.bits, self.bases):
            states.append((int(bit), int(basis)))

        return states

    def get_data(self):
        """
        Return Alice's generated data.
        """

        return {
            "bits": self.bits,
            "bases": self.bases,
            "states": self.prepare_states()
        }