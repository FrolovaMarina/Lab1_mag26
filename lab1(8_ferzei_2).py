import random
from itertools import permutations

def searching():
    solutions = []
    for fields in permutations(range(8)):
        safe = "Yes"
        for i in range(8):
            for j in range(i + 1, 8):
                if abs(i - j) == abs(fields[i] - fields[j]):
                    safe = "No"
                    break
            if safe == "No":
                break
        if safe == "Yes":
            solutions.append(list(fields))
    return solutions

def print_solution(solution):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    coords = []
    for i in range(8):
        line = ['*'] * 8
        line[solution[i]] = 'Ф'
        letter = letters[solution[i]]
        number = 8 - i
        coords.append(f"Ф{letter}{number}")
        print(line)
    print("\nМестоположение ферзей:", ", ".join(coords))

solutions = searching()
print(f"Решений всего: {len(solutions)}")
N = random.randint(0, len(solutions))
print("Одно из решений:")
print_solution(solutions[N])
