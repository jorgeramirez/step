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

    __commands = { 
        "adelante" : [0, 1], "atras" : [0, -1],
        "abajo" : [1, 0], "arriba" : [-1, 0]
    }

    __numbers = {
        "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
        "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10
    }

    def __init__(self, size=10):
        self.__size = size
        self.__step_size = STEP_SIZE
        self.__posr = 0
        self.__posc = 0
        self.__initialize()

    def __initialize(self):
        self.__board = [[0] * self.__size for _ in xrange(self.__size)]
        self.__board[self.__posr][self.__posc] = 1
   
    def draw(self):
        """
        Draw the current state of the board. Basic CLI implementation, override
        this for a more complex drawing logic (e.g. GTK-based).
        """
        for i in xrange(self.__size):
            for j in xrange(self.__size):
                cell = EMPTY_CELL
                if self.__board[i][j] == 1:
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
                self.__step_size = self.__numbers[parsed[1]]
        elif self.__commands.has_key(command):
            self.__board[self.__posr][self.__posc] = 0
            self.__posr = (self.__posr + self.__commands[command][ROW] * self.__step_size) % self.__size
            self.__posc = (self.__posc + self.__commands[command][COL] * self.__step_size) % self.__size
            self.__board[self.__posr][self.__posc] = 1


if __name__ == "__main__":
    board = Board()
    board.draw()
    for cmd in ["adelante", "adelante", "paso cinco", "abajo"]:
        board.move(cmd)
        print
        board.draw()
