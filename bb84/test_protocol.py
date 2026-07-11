from bb84.protocol import BB84Protocol

protocol = BB84Protocol(20)

results = protocol.execute()

print("\nAlice Bits")
print(results["alice_bits"])

print("\nAlice Bases")
print(results["alice_bases"])

print("\nBob Bases")
print(results["bob_bases"])

print("\nBob Bits")
print(results["bob_bits"])

print("\nMatching Positions")
print(results["matching_indices"])

print("\nAlice Sifted Key")
print(results["sifted_alice_key"])

print("\nBob Sifted Key")
print(results["sifted_bob_key"])

print("\nSifted Key Length")
print(results["sifted_key_length"])