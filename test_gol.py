import unittest


class Game:
    def __init__(self, cells):
        self.cells = cells

    def get_neighbours(self, cell):
        (cx, cy) = cell
        neighbours = []
        for (x, y) in self.cells:
            if cx - 1 <= x and cx + 1 >= x and cy - 1 <= y and cy + 1 >= y:
                if not (cy == y and cx == x):
                    neighbours.append((x, y))

        return neighbours


class TestThis(unittest.TestCase):
    def test_should_be_able_to_create_a_game(self):
        game = Game([(2, 2)])
        self.assertEqual(1, len(game.cells))

    def test_get_neighbours(self):
        game = Game([(1, 2), (3, 2), (2, 1), (2, 2), (2, 3)])
        # -c-
        # cXc
        # -c-
        self.assertEqual(4, len(game.get_neighbours((2, 2))))

        # -c-
        # Xcc
        # -c-
        self.assertEqual(3, len(game.get_neighbours((1, 2))))

        self.assertIn((2, 1), game.get_neighbours((2, 2)))
        self.assertIn((1, 2), game.get_neighbours((2, 2)))
        self.assertIn((3, 2), game.get_neighbours((2, 2)))
        self.assertIn((2, 3), game.get_neighbours((2, 2)))
        self.assertNotIn((2, 2), game.get_neighbours((2, 2)))

        # Xc-
        # ccc
        # -c-
        self.assertIn((1, 2), game.get_neighbours((1, 1)))
        self.assertNotIn((3, 2), game.get_neighbours((1, 1)))
        self.assertIn((2, 1), game.get_neighbours((1, 1)))
        self.assertIn((2, 2), game.get_neighbours((1, 1)))
        self.assertNotIn((2, 3), game.get_neighbours((1, 1)))
