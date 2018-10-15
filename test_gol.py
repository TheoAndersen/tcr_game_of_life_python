import unittest

class Game:
    def __init__(self):
        pass

class TestThis(unittest.TestCase):
    def test_should_be_able_to_create_a_game(self):
        game = Game()

