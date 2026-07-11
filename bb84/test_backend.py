from bb84.protocol import BB84Protocol

print("=" * 60)
print("QuantumSecureNet Backend Test")
print("=" * 60)

protocol = BB84Protocol(
    num_qubits=1000,
    eve_enabled=False,
    noise_probability=0.02
)

results = protocol.execute()

print()

print("Simulation Successful")

print()

print("Qubits :", results["num_qubits"])
print("Sifted Key :", results["sifted_key_length"])
print("Final Key :", results["final_key_length"])
print("QBER :", round(results["qber"],2),"%")

status = results["status"]

if hasattr(status,"status"):
    print("Status :",status.status)
    print("Recommendation :",status.recommendation)

print()

print("Backend Test Passed")