import unittest

class Game:
    def __init__(self, cells):
        self.cells = cells
        
def number_neighbors(cells):
    return 1

class TestThis(unittest.TestCase):
    def test_should_be_able_to_create_a_game(self):
        game = Game([(2, 2)])
        self.assertEqual(1, len(game.cells))

    def test_neighboars(self):
        self.assertEqual(1, number_neighbors([(2, 2)]))

