class Board:
    def __init__(self, cols, rows, squares):
        self.board = [['.' for _ in range(cols)] for _ in range(rows)]

        self.start_point = None
        self.end_point = None

        for square in squares:
            row = square['row']
            col = square['col']
            color_index = square['color_index']

            if color_index == 0:
                self.board[row][col] = '#'  # Walls represented by #
            elif color_index == 1:
                self.board[row][col] = 'S'  # Start Point represented by S
                self.start_point = (row, col, 0)
            elif color_index == 2:
                self.board[row][col] = 'E'  # End Point represented by E
                self.end_point = (row, col)

    def get_board_and_pos(self):
        return self.board, self.start_point, self.end_point

    def update_board(self, visited):
        rows = len(self.board)
        cols = len(self.board[0])

        for row in range(rows):
            for col in range(cols):
                if visited[row][col]:
                    self.board[row][col] = "V"
