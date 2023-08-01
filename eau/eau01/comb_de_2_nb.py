def generate_combinations():
    combinations = []
    for i in range(100):
        for j in range(i + 1, 100):
            combinations.append(f"{i:02d} {j:02d}")
    return ", ".join(combinations)

result = generate_combinations()
print(result)

