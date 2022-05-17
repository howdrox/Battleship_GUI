"""bot.py: bot functions for battleship"""

import random

def rand_coord():
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    return (x, y)

def guess(mat):
    x, y = rand_coord()
    value = mat[x][y]

    if value != "hit-" or value != "miss":
        return (x, y)
