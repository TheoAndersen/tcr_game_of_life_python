import unittest

class Game:
    def __init__(self, cells):
        self.cells = cells
        
def number_neighbors(cell, cells):
    (cx, cy) = cell
    n = 0
    for (x, y) in cells:
        if(cx - 1 <= x and cx + 1 >= x and cy -1 <= y and cy + 1 >= cy):
            if(not (cy == y and cx == x)):
               n = n + 1

    return n 

class TestThis(unittest.TestCase):
    def test_should_be_able_to_create_a_game(self):
        game = Game([(2, 2)])
        self.assertEqual(1, len(game.cells))

    def test_neighboars(self):
        cells = [(1, 2), (3, 2), (2, 1), (2, 2), (2, 3)]
        # -c-
        # cXc
        # -c-
        self.assertEqual(4, number_neighbors((2, 2), cells))

        # -c-
        # Xcc
        # -c-
        self.assertEqual(3, number_neighbors((1, 2), cells)) 
