import unittest


class Game:
    def __init__(self, cells):
        self.cells = cells

    def get_neighbours(self, cell):
        targetCell = cell
        neighbours = []
        for thisCell in self.cells:
            if (
                targetCell.x - 1 <= thisCell.x
                and targetCell.x + 1 >= thisCell.x
                and targetCell.y - 1 <= thisCell.y
                and targetCell.y + 1 >= thisCell.y
            ):
                if not (targetCell.y == thisCell.y and targetCell.x == thisCell.x):
                    neighbours.append(thisCell)

        return neighbours

    def step(self):
        self.cells = []
        return self


class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class TestThis(unittest.TestCase):
    def test_step_kills(self):
        game = Game([Cell(1, 2)])
        game = game.step()
        self.assertEqual(0, len(game.cells))

    def test_cell_should_be_immutable(self):
        cell = Cell(1, 2)
        self.assertEqual(Cell(1, 2), Cell(1, 2))
        self.assertNotEqual(Cell(1, 1), Cell(2, 2))

    def test_should_be_able_to_create_a_game(self):
        game = Game([Cell(2, 2)])
        self.assertEqual(1, len(game.cells))

    def test_get_neighbours(self):
        game = Game([Cell(1, 2), Cell(3, 2), Cell(2, 1), Cell(2, 2), Cell(2, 3)])
        # -c-
        # cXc
        # -c-
        self.assertEqual(4, len(game.get_neighbours(Cell(2, 2))))

        # -c-
        # Xcc
        # -c-
        self.assertEqual(3, len(game.get_neighbours(Cell(1, 2))))

        self.assertIn(Cell(2, 1), game.get_neighbours(Cell(2, 2)))
        self.assertIn(Cell(1, 2), game.get_neighbours(Cell(2, 2)))
        self.assertIn(Cell(3, 2), game.get_neighbours(Cell(2, 2)))
        self.assertIn(Cell(2, 3), game.get_neighbours(Cell(2, 2)))
        self.assertNotIn(Cell(2, 2), game.get_neighbours(Cell(2, 2)))

        # Xc-
        # ccc
        # -c-
        self.assertIn(Cell(1, 2), game.get_neighbours(Cell(1, 1)))
        self.assertNotIn(Cell(3, 2), game.get_neighbours(Cell(1, 1)))
        self.assertIn(Cell(2, 1), game.get_neighbours(Cell(1, 1)))
        self.assertIn(Cell(2, 2), game.get_neighbours(Cell(1, 1)))
        self.assertNotIn(Cell(2, 3), game.get_neighbours(Cell(1, 1)))
