import os

from src.SudokuBoard import SudokuBoard
from src.SudokuSolver import SudokuSolver


def read_file(filepath):
    with open(get_real_path(filepath), "r") as f:
        try:
            board = []
            while True:
                board_line = []
                line = f.readline()

                if line == "":
                    break

                for char in line:
                    if char == '-':
                        board_line.append(None)
                    elif char.isnumeric():
                        board_line.append(int(char))

                board.append(board_line)
            return board
        finally:
            f.close()


def get_real_path(filepath):
    my_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(my_path, filepath)


def is_valid_board_format(board):
    if len(board) != 9:
        return False

    for row in board:
        if len(row) != 9:
            return False

    return True


if __name__ == '__main__':
    board = read_file('../resources/sample1.txt')

    if is_valid_board_format(board):
        print("This is a valid board, ready for action")
        solver = SudokuSolver(board)
        solution = solver.solve_board()

        if solution is not None:
            print("A solution has been found:")
            my_board = SudokuBoard(solution)
            my_board.draw()
        else:
            print("The given board can't be resolved.")
    else:
        print("I can't proceed with this, the board is not valid")
