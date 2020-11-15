class SudokuBoard:
    UPPER_LEFT_CORNER = '╔'
    UPPER_RIGHT_CORNER = '╗'
    LOWER_LEFT_CORNER = '╚'
    LOWER_RIGHT_CORNER = '╝'

    T_DOUBLE_JUNCTION_TOP = '╦'
    T_DOUBLE_JUNCTION_LEFT = '╠'
    T_DOUBLE_JUNCTION_RIGHT = '╣'
    T_DOUBLE_JUNCTION_BOTTOM = '╩'

    T_SINGLE_JUNCTION_TOP = '╤'
    T_SINGLE_JUNCTION_BOTTOM = '╧'
    T_SINGLE_JUNCTION_LEFT = '╟'
    T_SINGLE_JUNCTION_RIGHT = '╢'

    CROSS_DOUBLE_JUNCTION = '╬'
    CROSS_SINGLE_DOUBLE_JUNCTION = '╫'
    CROSS_DOUBLE_SINGLE_JUNCTION = '╪'
    CROSS_JUNCTION = '┼'

    HORIZONTAL_DOUBLE_LINE = '═'
    VERTICAL_DOUBLE_LINE = '║'
    HORIZONTAL_LINE = '─'
    VERTICAL_LINE = '│'

    def __init__(self, board):
        self.board = board

    def draw(self):
        self._draw_first_row(self.board, 3)
        for y, row in enumerate(self.board):
            self._draw_data_row(row, 3)

            if len(row) - 1 != y:
                if (y + 1) % 3 == 0:
                    self._draw_inner_square(row, 3)
                else:
                    self._draw_inner_row(row, 3)
        self._draw_last_row(self.board, 3)

    def _draw_data_row(self, row, cell_size):
        print(self._draw_row(row, False, cell_size,
                             self.VERTICAL_DOUBLE_LINE,
                             self.VERTICAL_DOUBLE_LINE,
                             self.VERTICAL_LINE,
                             self.VERTICAL_DOUBLE_LINE,
                             ' '))

    def _draw_first_row(self, row, cell_size):
        print(self._draw_row(row, True, cell_size,
                             self.UPPER_LEFT_CORNER,
                             self.UPPER_RIGHT_CORNER,
                             self.T_SINGLE_JUNCTION_TOP,
                             self.T_DOUBLE_JUNCTION_TOP,
                             self.HORIZONTAL_DOUBLE_LINE))

    def _draw_inner_row(self, row, cell_size):
        print(self._draw_row(row, True, cell_size,
                             self.VERTICAL_DOUBLE_LINE,
                             self.VERTICAL_DOUBLE_LINE,
                             self.CROSS_JUNCTION,
                             self.CROSS_SINGLE_DOUBLE_JUNCTION,
                             self.HORIZONTAL_LINE))

    def _draw_inner_square(self, row, cell_size):
        print(self._draw_row(row, True, cell_size,
                             self.VERTICAL_DOUBLE_LINE,
                             self.VERTICAL_DOUBLE_LINE,
                             self.CROSS_DOUBLE_SINGLE_JUNCTION,
                             self.CROSS_DOUBLE_JUNCTION,
                             self.HORIZONTAL_DOUBLE_LINE))

    def _draw_last_row(self, row, cell_size):
        print(self._draw_row(row, True, cell_size,
                             self.LOWER_LEFT_CORNER,
                             self.LOWER_RIGHT_CORNER,
                             self.T_SINGLE_JUNCTION_BOTTOM,
                             self.T_DOUBLE_JUNCTION_BOTTOM,
                             self.HORIZONTAL_DOUBLE_LINE))

    def _draw_row(self, data_row, is_dummy, cell_size, first_character, last_character,
                  between_cell_single_character, between_cell_double_character, padding):
        padding_character = ""
        for i in range(0, int((cell_size - 1) / 2)):
            padding_character += padding

        line = ""
        for x, data in enumerate(data_row):
            if x == 0:
                line += first_character

            line += "{0}{1}{0}".format(padding_character, data if not is_dummy else padding_character)

            if x == len(data_row) - 1:
                line += last_character
            elif (x + 1) % 3 == 0:
                line += between_cell_double_character
            else:
                line += between_cell_single_character
        return line
