from board_functions import create_blank_board, populate_board, render_board, show_board, save_board, write_board, initialize_solutions_json

def get_safe_squares(N, queens):
    '''
    Takes a list of (x, y) input representing position of each queen
    Returns a list of safe (x, y) squares not being hit by any queens
    '''
    assert type(queens) is list
    X,Y = 0,1
    # 1 represents a square is safe, 0 represents it is not
    square_index = {(i,j): 1 for i in range(N) for j in range(N)}
    for queen in queens:
        for key in square_index.keys():
            # check if in same row or column
            if (key[X] == queen[X] or key[Y] == queen[Y]):
                square_index[key] = 0
            # check if in same diagonal
            if (abs(key[X] - queen[X]) == abs(key[Y] - queen[Y])):
                square_index[key] = 0
    safe_squares = [k for k,v in square_index.items() if v == 1]
    return safe_squares

def find_solutions(N, queens = []):
    '''NxN board solver, brute force'''
    if (len(queens) == N):
        board = populate_board(N, queens)
        save_board(board)

    safe_squares = get_safe_squares(N, queens)
    for square in safe_squares:
        find_solutions(N, queens + [square])

def main():
    for N in range(1,9):
        initialize_solutions_json(N)
        find_solutions(N)

if __name__ == '__main__':
    main()