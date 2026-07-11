from bb84.qber import QBERCalculator

alice_key = [
    1,0,1,1,0,0,1,1,0,1
]

bob_key = [
    1,0,1,0,0,0,1,1,1,1
]

qber = QBERCalculator()

value = qber.calculate(
    alice_key,
    bob_key
)

print("QBER")

print(value)

print()

print(qber.get_statistics())