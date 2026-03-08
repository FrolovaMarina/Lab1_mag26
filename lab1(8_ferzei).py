import random

def searching():
    solutions = []
    board = [0] * 8  
    
    def safe_field(board, row, col):  
        for row_before in range(row):
            col_before = board[row_before]
            if col_before == col or abs(col_before - col) == abs(row_before - row):
                return False
        return True

    def field_recurs(board, row):   
        if row == 8:
            solutions.append(board.copy())
            return
        for col in range(8):
            if safe_field(board, row, col):
                board[row] = col
                field_recurs(board, row + 1)

    field_recurs(board, 0)
    return solutions
    
def print_solution(solution):     
    coords = []
    for i in range(8):          
        line = ['*'] * 8
        line[solution[i]] = 'Ф'
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        letter = letters[solution[i]] 
        number = 8 - i                          
        coords.append(f"Ф{letter}{number}")
        print(line)              
    print("\nМестоположение ферзей:", ", ".join(coords))

solutions = searching()
print(f"Решений всего: {len(solutions)}")
print("Одно из решений:")
N = random.randint(1, len(solutions))
print_solution(solutions[N])
