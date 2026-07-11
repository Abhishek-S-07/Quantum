from bb84.noise import QuantumNoise

noise = QuantumNoise(error_probability=0.15)

bits = [1,0,1,1,0,0,1,1,0,1]

print("Original")

print(bits)

noisy = noise.apply(bits)

print()

print("Noisy")

print(noisy)

print()

print(noise.get_statistics())