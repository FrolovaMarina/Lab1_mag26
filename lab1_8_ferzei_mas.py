import random
import time

def searching(n=8, max_iter=1000):
    board = list(range(n))

    def all_conflicts(row, col):
        conflicts = 0
        for r in range(n):
            if r == row:
                continue
            c = board[r]
            if c == col or abs(r - row) == abs(c - col):
                conflicts += 1
        return conflicts

    for i in range(max_iter):
        conflicts = 0
        for r in range(n):
            conflicts += all_conflicts(r, board[r])       
        if conflicts == 0:
            return board 
        conflict_agents = []
        for r in range(n):
            if all_conflicts(r, board[r]) > 0:
                conflict_agents.append(r)          
        row = random.choice(conflict_agents)       
        best_cols = []
        min_conflicts = 64     
        for col in range(n):
            if col == board[row]:
                continue 
            conf = all_conflicts(row, col)
            if conf < min_conflicts:
                min_conflicts = conf
                best_cols = [col]
            elif conf == min_conflicts:
                best_cols.append(col)
        board[row] = random.choice(best_cols)           
    return None 

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

solution = searching()  
print("Решение:")
print_solution(solution)
