import json

def create_blank_board(N):
    '''Returns an empty board'''
    return [[0 for i in range(N)] for j in range(N)]

def populate_board(N, queens):
    '''Returns a board populated with given list of queen locations'''
    assert type(queens) is list
    board = create_blank_board(N)
    for queen in queens:
        board[queen[1]][queen[0]] = 1
    return board

def render_board(board):
    '''Prints board to terminal'''
    assert type(board) is list and type(board[0]) is list
    outstr = ""
    formatstr = "| {} " * len(board) + "|"
    _board = board.copy()
    for row in _board:
        row = ['_' if i == 0 else '#' for i in row]
        rowstr = formatstr.format(*row)
        outstr += (rowstr + "\n")
    return outstr

def show_board(board):
    assert type(board) is list and type(board[0]) is list
    board_render = render_board(board)
    print(board_render)

def save_board(board):
    assert type(board) is list and type(board[0]) is list
    N = len(board)
    board_render = render_board(board)
    solutions_fname = "{}_solutions.json".format(N)
    with open(solutions_fname) as f:
        solutions = json.load(f)
    solutions[board_render] = 1
    with open(solutions_fname, 'w') as f:
        json.dump(solutions, f)

def write_board(board):
    assert type(board) is list and type(board[0]) is list
    board_render = render_board(board)
    fname = "{}_queen_problem.txt".format(len(board))
    with open(fname, 'a') as f:
        f.write(board_render)
        f.write("\n\n")

def initialize_solutions_json(N):
    with open("{}_solutions.json".format(N), 'w') as f:
        f.write('{}')

