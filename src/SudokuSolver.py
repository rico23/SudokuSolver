import copy


class SudokuSolver:
    def __init__(self, board_array):
        self.board = board_array

    def solve_board(self):
        return self.__solve_board_recursive(self.board)

    def __solve_board_recursive(self, board):
        tmp_board = copy.deepcopy(board)
        for y, row in enumerate(tmp_board):
            for x, cell in enumerate(tmp_board[y]):
                if board[y][x] == 0:
                    possibilities = self.__calculate_cell_values(tmp_board, x, y)

                    if len(possibilities) == 0:
                        return None

                    for possibility in possibilities:
                        tmp_board[y][x] = possibility
                        response = self.__solve_board_recursive(tmp_board)
                        if response is not None:
                            return response
        return tmp_board

    # Calculates all possible number for a specific cell
    def __calculate_cell_values(self, board, x, y):
        possible_number = []
        for number in range(1, 10):
            if self.__is_cell_valid(board, x, y, number):
                possible_number.append(number)

        return possible_number

    # Validate that all condition is valid for a specific cell
    def __is_cell_valid(self, board, x, y, number):
        return self.__is_row_valid(board, x, y, number) and \
               self.__is_column_valid(board, x, y, number) and \
               self.__is_square_valid(board, x, y, number)

    # Validate if a row is valid for a specific number
    def __is_row_valid(self, board, x, y, number):
        for i, cell in enumerate(board[y]):
            if i is not x and cell is number:
                return False
        return True

    # Validate if a column is valid for a specific number
    def __is_column_valid(self, board, x, y, number):
        for i, row in enumerate(board):
            if i is not y and row[x] is number:
                return False
        return True

    # Validate is the square is valid with specific number
    def __is_square_valid(self, board, x, y, number):
        mod_x = int(x / 3)
        mod_y = int(y / 3)
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if mod_x * 3 <= j < (mod_x + 1) * 3 \
                        and mod_y * 3 <= i < (mod_y + 1) * 3:
                    if (i is not y or j is not x) and cell is number:
                        return False
        return True
