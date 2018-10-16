import unittest

class Game:
    def __init__(self, cells):
        self.cells = cells
        
def number_neighbors(cell, cells):
    (cx, cy) = cell
    n = 0
    for (x, y) in cells:
        if(cx - 1 <= x and cx + 1 >= x and cy -1 <= y and cy + 1 >= cy):
            n = n + 1

    return n - 1

class TestThis(unittest.TestCase):
    def test_should_be_able_to_create_a_game(self):
        game = Game([(2, 2)])
        self.assertEqual(1, len(game.cells))

    def test_neighboars(self):
        cell = (2, 2)
        cells = [(1, 2), (3, 2), (2, 1), (2, 2), (2, 3)]
        # -c-
        # cXc
        # -c-
        self.assertEqual(4, number_neighbors(cell, cells))

