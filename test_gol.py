import unittest

class Game:
    def __init__(self, cells):
        self.cells = cells

class TestThis(unittest.TestCase):
    def test_should_be_able_to_create_a_game(self):
        game = Game([(2, 2)])
        self.assertEqual(1, len(game.cells))

