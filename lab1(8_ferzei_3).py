import random

def min_conflict(n=8, max_iter=1000):
    board = list(range(n))

    def conflicts(row, col):
        count = 0
        for i in range(n):
            if i != row and (board[i] == col or abs(i - row) == abs(board[i] - col)):
                count += 1
        return count

    for iteration in range(max_iter):
        solution = "Yes"
        conflict_rows = []
        col_conflicts = []
        conflict_counts = []
        best_col = []
        for field in range(n):
            if conflicts(field, board[field]) > 0:
                conflict_rows.append(field)
                solution = "No"
        if solution == "Yes":
            return board
        row = random.choice(conflict_rows)
        
        for col in range(n):
            if col != board[row]:
                sum_conflicts = conflicts(row, col)
                col_conflicts.append((col, sum_conflicts))
        
        for col, conflict in col_conflicts:
            conflict_counts.append(conflict)
        min_conflict = min(conflict_counts)  
        
        for col, conflict in col_conflicts:
            if conflict == min_conflict:
                best_col.append(col)      
        board[row] = random.choice(best_col)
    return  

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

solution = min_conflict()
print_solution(solution)  
