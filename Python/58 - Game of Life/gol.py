import os
from random import randint


def clear():
    os.system("cls")


def move(y, x):
    return "\033[%d;%dH" % (y + 1, x + 1)


class GOL:
    def __init__(self, width, height):
        self.board = []
        self.prev_board = []
        self.width = width
        self.height = height

        for col in range(height):
            self.board.append([])
            self.prev_board.append([])
            for row in range(width):
                cell = randint(0, 1)
                self.board[col].append(cell)
                self.prev_board[col].append(0)

    def set_up_screen(self):
        clear()
        empty_cell = None
        for col in range(self.height):
            for row in range(self.width):
                if self.board[col][row] == 1:
                    print("#", end="")
                else:
                    if empty_cell is None:
                        empty_cell = [col, row]
                    print(" ", end="")
        if empty_cell is not None:
            print(move(empty_cell[0], empty_cell[1]) + " ")
        else:
            print(move(0, 0) + "#")

    def draw(self):
        for col in range(self.height):
            for row in range(self.width):
                if self.board[col][row] != self.prev_board[col][row]:
                    if self.board[col][row] == 1:
                        print(move(col, row) + "#", end="")
                    else:
                        print(move(col, row) + " ", end="")

    def simulate(self):
        self.prev_board = [item[:] for item in self.board]

        for col in range(self.height):
            for row in range(self.width):
                neighbours = self.get_neighbours(col, row)
                if self.prev_board[col][row] == 1:
                    if neighbours < 2 or neighbours > 3:
                        self.board[col][row] = 0
                    else:
                        self.board[col][row] = 1
                elif neighbours == 3:
                    self.board[col][row] = 1
                else:
                    self.board[col][row] = 0

    # Gets the current living neighbours of a cell on the board
    def get_neighbours(self, col: int, row: int) -> int:
        neighbours = 0
        for dcol in range(-1, 2):
            if col + dcol < 0 or col + dcol >= self.height:
                continue
            for drow in range(-1, 2):
                if row + drow < 0 or row + drow >= self.width:
                    continue
                if self.prev_board[col + dcol][row + drow] == 1:
                    neighbours += 1
        return max(neighbours - self.prev_board[col][row], 0)
