from bb84.alice import Alice

alice = Alice(10)

alice.generate_bits()
alice.generate_bases()

print("Bits:")
print(alice.bits)

print()

print("Bases:")
print(alice.bases)

print()

print("States:")
print(alice.prepare_states())