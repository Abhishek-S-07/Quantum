from bb84.alice import Alice
from bb84.bob import Bob

NUM_QUBITS = 10

alice = Alice(NUM_QUBITS)

alice.generate_bits()
alice.generate_bases()

states = alice.prepare_states()

bob = Bob(NUM_QUBITS)

bob.generate_bases()
bob.measure(states)

print("Alice Bits")
print(alice.bits)

print()

print("Alice Bases")
print(alice.bases)

print()

print("Bob Bases")
print(bob.bases)

print()

print("Bob Measurements")
print(bob.measured_bits)