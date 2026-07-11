from bb84.alice import Alice
from bb84.eve import Eve

alice = Alice(10)

alice.generate_bits()
alice.generate_bases()

states = alice.prepare_states()

eve = Eve(10)

resent = eve.intercept(states)

print("Alice States")
print(states)

print()

print("Eve Bases")
print(eve.bases)

print()

print("Eve Measurements")
print(eve.measured_bits)

print()

print("Resent States")
print(resent)