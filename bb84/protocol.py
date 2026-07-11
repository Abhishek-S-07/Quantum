"""
===========================================================
QuantumSecureNet
Main BB84 Protocol Controller

Executes the complete BB84 Quantum Key Distribution workflow.

Workflow
--------
1. Alice generates random bits and bases.
2. Alice prepares conceptual quantum states.
3. Optional Eve intercept-resend attack.
4. Optional channel noise.
5. Bob measures received states.
6. Basis reconciliation (Sifting).
7. QBER calculation.
8. Error reconciliation.
9. Privacy amplification.
10. Quantum Communication Health Monitor (QCHM).
===========================================================
"""

from bb84.alice import Alice
from bb84.bob import Bob
from bb84.eve import Eve
from bb84.noise import QuantumNoise
from bb84.qber import calculate_qber
from bb84.reconciliation import reconcile_keys
from bb84.privacy import PrivacyAmplification
from bb84.qchm import evaluate_channel


class BB84Protocol:
    """
    Main BB84 Protocol Controller.
    """

    def __init__(
        self,
        num_qubits=1000,
        eve_enabled=False,
        noise_probability=0.0,
    ):

        self.num_qubits = num_qubits
        self.eve_enabled = eve_enabled
        self.noise_probability = noise_probability

    def execute(self):
        """
        Execute one complete BB84 simulation.

        Returns
        -------
        dict
            Simulation results.
        """

        ############################################################
        # Alice
        ############################################################

        alice = Alice(self.num_qubits)

        alice_bits = alice.generate_bits()
        alice_bases = alice.generate_bases()

        alice_states = alice.prepare_states()

        ############################################################
        # Quantum Channel
        ############################################################

        transmitted_states = list(alice_states)

        ############################################################
        # Eve Attack (Optional)
        ############################################################

        if self.eve_enabled:

            eve = Eve(self.num_qubits)

            transmitted_states = eve.intercept_resend(
                transmitted_states
            )

        ############################################################
        # Channel Noise
        ############################################################

        noise = QuantumNoise(self.noise_probability)

        transmitted_bits = [
            bit for bit, basis in transmitted_states
        ]

        transmitted_bases = [
            basis for bit, basis in transmitted_states
        ]

        noisy_bits = noise.apply(transmitted_bits)

        noisy_states = list(
            zip(
                noisy_bits,
                transmitted_bases
            )
        )

        ############################################################
        # Bob
        ############################################################

        bob = Bob(self.num_qubits)

        bob.generate_bases()

        bob_bits = bob.measure(noisy_states)

        bob_bases = bob.bases

        ############################################################
        # Basis Reconciliation (Sifting)
        ############################################################

        sifted_alice = []
        sifted_bob = []

        for a_bit, b_bit, a_basis, b_basis in zip(
            alice_bits,
            bob_bits,
            alice_bases,
            bob_bases,
        ):

            if a_basis == b_basis:

                sifted_alice.append(int(a_bit))
                sifted_bob.append(int(b_bit))

        ############################################################
        # QBER
        ############################################################

        qber = calculate_qber(
            sifted_alice,
            sifted_bob,
        )

        ############################################################
        # Error Reconciliation
        ############################################################

        corrected_key = reconcile_keys(
            sifted_alice,
            sifted_bob,
        )

        ############################################################
        # Privacy Amplification
        ############################################################

        final_key = PrivacyAmplification().generate_secure_key(
            corrected_key
        )

        ############################################################
        # QCHM
        ############################################################

        status = evaluate_channel(qber)

        ############################################################
        # Noise Statistics
        ############################################################

        noise_statistics = noise.get_statistics()

        ############################################################
        # Results
        ############################################################

        results = {

            "num_qubits": self.num_qubits,

            "eve_enabled": self.eve_enabled,

            "noise_probability": self.noise_probability,

            "noise_statistics": noise_statistics,

            "alice_bits": alice_bits,

            "alice_bases": alice_bases,

            "alice_states": alice_states,

            "bob_bits": bob_bits,

            "bob_bases": bob_bases,

            "sifted_alice_key": sifted_alice,

            "sifted_bob_key": sifted_bob,

            "sifted_key": corrected_key,

            "sifted_key_length": len(corrected_key),

            "final_key": final_key,

            "final_key_length": len(final_key),

            "qber": qber,

            "status": status,

        }

        return results