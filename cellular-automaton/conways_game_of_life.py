"""
Conway's Game of Life
"""
import itertools

class GameOfLife:
    @classmethod
    def dead_grid(cls, *, height=None, width=None):
        return [
            [Dead() for _cols in range(width)]
            for _rows in range(height)
        ]

    @classmethod
    def from_str(cls, string):
        non_empty_lines = (
            line for line in string.splitlines()
            if len(line) > 0
        )
        parsed_grid = [
            [Cell.from_str(char) for char in line]
            for line in non_empty_lines
        ]
        return cls(grid=parsed_grid)

    def __init__(self, grid=None):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])


    def __str__(self):
        return '\n'.join(
            ''.join(str(cell) for cell in row)
            for row in self.grid
        )

    def next_generation(self):
        next_grid = [
            [
                cell.next_state(neighbor_count)
                for cell, neighbor_count in row
            ]
            for row in self.grid_with_live_neighbor_counts()
        ]
        return GameOfLife(grid=next_grid)

    def grid_with_live_neighbor_counts(self):
        '''
        Returns an iterator of grid rows in which each element
        is a tuple containing the cell and the count of living neighbors
        adjacent to that cell.
        E.g. [[(Live, 0), (Dead, 3), ...], ...]
        '''
        return (
            (
                (cell, self.count_live_neighbors(row, col))
                for (row, col), cell in coordinated_row
            )
            for coordinated_row in self.coordinate()
        )

    def coordinate(self):
        '''
        Returns an iterator of grid rows in which each element
        is a tuple containg the coordinates and the content of the grid 
        at those coordinates.
        E.g. [[((0, 0), Live), ((0, 1), Dead), ...], ...]
        '''
        return (
            (
                ((row_index, col_index), cell)
                for col_index, cell in enumerate(row)
            )
            for row_index, row in enumerate(self.grid)
        )

    def count_live_neighbors(self, row, col):
        directions_1D = (-1, 0, 1)
        directions_2D = itertools.product(directions_1D, directions_1D)
        neighbor_coords = (
            (row + d_row, col + d_col)
            for (d_row, d_col) in directions_2D
            if (d_row, d_col) != (0, 0)
        )

        def is_coord_alive(coord):
            cell = self.get(*coord, default=Dead())
            return int(cell.is_alive)

        return sum(map(is_coord_alive, neighbor_coords))

    def get(self, row, col, default=None):
        is_within_rows = (0 <= row < self.height)
        is_within_cols = (0 <= col < self.width)
        if is_within_rows and is_within_cols:
            return self.grid[row][col]
        return default


class Cell:
    @classmethod
    def from_str(cls, string):
        if string == Live.string_form:
            return Live()
        return Dead()

    def __str__(self):
        return self.string_form

class Dead(Cell):
    string_form = '·'
    is_alive = False

    def next_state(self, neighbor_count):
        if neighbor_count == 3:
            return Live()
        return Dead()

class Live(Cell):
    string_form = '0'
    is_alive = True

    def next_state(self, neighbor_count):
        if neighbor_count in [2, 3]:
            return Live()
        return Dead()


from textwrap import dedent

def run_string_example(
    *,
    seed_string=None,
    seed_name=None,
    num_gens=10
):
    seed_game = GameOfLife.from_str(seed_string)
    if seed_name is None:
        seed_name = f'A {seed_game.height}x{seed_game.width} grid'
    print(dedent(f'''
        =========================
        | Conway's Game of Life |
        {'':=^50}
        | {f'Starting with seed: "{seed_name:.10}"': <46.46} |
        | {f'Running for {str(num_gens):1.3} generations.': <46.46} |
        {'':=^50}
    '''))
    latest_generation = seed_game
    for gen_num in range(1, num_gens + 1):
        print(f'Generation {gen_num}:')
        print(str(latest_generation))
        latest_generation = latest_generation.next_generation()
    print('Done')

def glider_example():
    glider_string = dedent('''
        ··0····
        0·0····
        ·00····
        ·······
        ·······
        ·······
    ''')
    run_string_example(
        seed_string=glider_string,
        seed_name='Glider',
        num_gens=15
    )

def question_example():
    from textwrap import dedent

    game_string = dedent('''
        ·0·
        0·0
    ''')
    run_string_example(
        seed_string=game_string,
        num_gens=4
    )

if __name__ == '__main__':
    glider_example()
    question_example()
