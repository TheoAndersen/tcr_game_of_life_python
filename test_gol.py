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
        next_step_cells = []
        (max_x, max_y) = self.get_grid_bounds()
        for x in range(0, max_x):
            for y in range(0, max_y):
                cell = Cell(x, y)
                num_neighbours = len(self.get_neighbours(cell))
                if cell in self.cells:
                    if num_neighbours > 1 and num_neighbours < 4:
                        next_step_cells.append(cell)
        self.cells = next_step_cells
        return self

    def get_grid_bounds(self):
        x = max(map(lambda cell: cell.x, self.cells))
        y = max(map(lambda cell: cell.y, self.cells))
        return (x, y)


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class TestThis(unittest.TestCase):
    def test_return_max_x_based_on_current_cells(self):
        game = Game([Cell(1, 1), Cell(2, 2), Cell(3, 1), Cell(3, 2)])
        self.assertEqual((3, 2), game.get_grid_bounds())

    def test_step_more_than_three_neighbours_kills_the_cell(self):
        # c-c
        # -X-
        # c-c
        game = Game([Cell(1, 1), Cell(1, 3), Cell(2, 2), Cell(3, 1), Cell(3, 3)])
        game = game.step()
        self.assertEqual(0, len(game.cells))

    def test_step_two_or_three_neighbours_keeps_the_cell_alive(self):
        # c--
        # -X-
        # --c
        game = Game([Cell(1, 1), Cell(2, 2), Cell(3, 3)])
        game = game.step()
        self.assertIn(Cell(2, 2), game.cells)
        self.assertNotIn(Cell(1, 1), game.cells)
        self.assertNotIn(Cell(3, 3), game.cells)

        # c--
        # -X-
        # c-c
        game = Game([Cell(1, 1), Cell(1, 3), Cell(2, 2), Cell(3, 3)])
        game = game.step()
        self.assertIn(Cell(2, 2), game.cells)
        self.assertNotIn(Cell(1, 1), game.cells)
        self.assertNotIn(Cell(1, 3), game.cells)
        self.assertNotIn(Cell(3, 3), game.cells)

    def test_step_less_than_two_neibours_kills_the_cell(self):
        game = Game([Cell(1, 2)])
        game = game.step()
        self.assertEqual(0, len(game.cells))

        game = Game([Cell(1, 1), Cell(3, 3), Cell(5, 5)])
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
