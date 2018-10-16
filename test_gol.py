import unittest

class Game:
    def __init__(self, cells):
        self.cells = cells
        
def number_neighbors(cell, cells):
        
    return len(cells) - 1

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

