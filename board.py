#!/usr/bin/env python

# comandos
#
#   adelante
#   atras
#   paso <size>
#   abajo
#   arriba

__all__ = [ "Board" ]

# drawing configs
GUY = "X"
EMPTY_CELL = "o"

# board defaults configs
N = 10
STEP_SIZE = 1

# command related configs
ROW = 0
COL = 1


class Board:
    """Represents the board."""

    _commands = { 
        "adelante" : [0, 1], "atras" : [0, -1],
        "abajo" : [1, 0], "arriba" : [-1, 0]
    }

    _numbers = {
        "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
        "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10
    }

    def __init__(self, size=10):
        self._size = size
        self._step_size = STEP_SIZE
        self._posr = 0
        self._posc = 0
        self._initialize()

    def _initialize(self):
        self._board = [[0] * self._size for _ in xrange(self._size)]
        self._board[self._posr][self._posc] = 1
   
    def draw(self):
        """
        Draw the current state of the board. Basic CLI implementation, override
        this for a more complex drawing logic (e.g. GTK-based).
        """
        for i in xrange(self._size):
            for j in xrange(self._size):
                cell = EMPTY_CELL
                if self._board[i][j] == 1:
                    cell = GUY
                print cell,
            print

    def move(self, command=""):
        """Update the state of the board based on the given command."""
        if command == "": 
            return
        command = command.lower()
        if command.find("paso") > -1:
            parsed = command.split()
            if len(parsed) == 2:
                self._step_size = self._numbers[parsed[1]]
        elif self._commands.has_key(command):
            self._board[self._posr][self._posc] = 0
            self._posr = (self._posr + self._commands[command][ROW] * self._step_size) % self._size
            self._posc = (self._posc + self._commands[command][COL] * self._step_size) % self._size
            self._board[self._posr][self._posc] = 1


if __name__ == "__main__":
    board = Board()
    board.draw()
    for cmd in ["adelante", "adelante", "paso cinco", "abajo"]:
        board.move(cmd)
        print
        board.draw()
