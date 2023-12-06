from sys import exit


class Interpreter:
    def __init__(self, text):
        self.board = []
        self.x = 0
        self.y = 0
        self.vector = '>'
        self.stack = []
        self._init_board(text)

    def get(self):
        return self.board[self.x][self.y]

    def step(self):
        if self.vector == '>':
            self.y += 1
        elif self.vector == '<':
            self.y -= 1
        elif self.vector == '^':
            self.x -= 1
        elif self.vector == 'v':
            self.x += 1
        if (len(self.board) <= self.x or self.x < 0 or
                len(self.board[0]) <= self.y or self.y < 0):
            exit('Задеты границы поля')

    def _init_board(self, text):
        row = len(text)
        column = 0

        for line in text:
            if len(line) > column:
                column = len(line)

        self.board = [' '] * row
        for i in range(row):
            self.board[i] = [' '] * column

        for i in range(len(text)):
            for j in range(len(text[i])):
                self.board[i][j] = text[i][j]
