import copy


def parse_input(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            grid.append(list(line.strip()))
    
    return grid


class Grid():
    def __init__(self, grid_map):
        self.grid_map = copy.deepcopy(grid_map)

    def __repr__(self):
        grid_string = ""
        for row in self.grid_map:
            grid_string += "".join(row) + "\n"
        grid_string = grid_string.strip()
        return grid_string
    
    def get_initial_guard_position(self):
        x = None
        y = None
        for row_num, row in enumerate(self.grid_map):
            if "^" in row:
                col_num = row.index("^")
                x = col_num
                y = row_num
                break
        
        if x and y:
            return x, y
        else:
            raise ValueError("No starting location in given grid map")
    
    def get_square_contents(self, x, y) -> str:
        if x < 0 or x > len(self.grid_map[0]) or y < 0 or y > len(self.grid_map):
            raise IndexError
        
        return self.grid_map[y][x]

    def mark_square(self, x, y) -> None:
        self.grid_map[y][x] = "X"
    
    def count_marked_squares(self) -> int:
        count = 0
        for row in self.grid_map:
            count += row.count("X")
        
        return count
    
    def add_obstacle(self, x, y):
        self.grid_map[y][x] = "#"
    
    def get_locations_of_all_marked_squares(self):
        locations = []
        for y, row in enumerate(self.grid_map):
            for x, square in enumerate(row):
                if square == "X":
                    locations.append((x, y))
        
        return locations


class Guard():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = [0, -1]
        self.memory = []
        self.stuck_in_infinite_loop = False

    def __repr__(self):
        return f"At ({self.x}, {self.y}) facing {self.direction}"
    
    def add_to_memory(self):
        self.memory.append((self.x, self.y, self.direction))
    
    def get_next_location(self):
        new_x = self.x + self.direction[0]
        new_y = self.y + self.direction[1]
        return new_x, new_y
    
    def update(self, new_square_contents):
        self.add_to_memory()

        if new_square_contents == "." or new_square_contents == "X":
            self.x = self.x + self.direction[0]
            self.y = self.y + self.direction[1]
        elif new_square_contents == "#":
            self.direction = [-self.direction[1], self.direction[0]]
        
        if (self.x, self.y, self.direction) in self.memory:
            self.stuck_in_infinite_loop = True


def run_simulation(grid: Grid):
    infinite_loop = False

    try:
        guard_x, guard_y = grid.get_initial_guard_position()
    except ValueError:
        print("No starting location given in grid map")
        print(grid)
        return grid, infinite_loop

    guard = Guard(guard_x, guard_y)

    while True:
        grid.mark_square(guard.x, guard.y)
        try:
            next_square_contents = grid.get_square_contents(*guard.get_next_location())
        except IndexError:
            break
        guard.update(next_square_contents)
        if guard.stuck_in_infinite_loop:
            infinite_loop = True
            break
    
    return grid, infinite_loop


if __name__ == "__main__":
    INPUT_FILENAME = "input.txt"
    grid_map = parse_input(INPUT_FILENAME)

    # Part 1
    grid = Grid(grid_map)
    grid, infinite_loop = run_simulation(grid)
    
    print(grid)
    print(grid.count_marked_squares())

    # Part 2

    locations_to_add_obstacles = grid.get_locations_of_all_marked_squares()

    infinite_loops = 0

    locations_to_check = len(locations_to_add_obstacles)

    for i, location in enumerate(locations_to_add_obstacles):
        grid = Grid(grid_map)
        x = location[0]
        y = location[1]
        grid.add_obstacle(x, y)
        grid, infinite_loop = run_simulation(grid)

        if infinite_loop:
            infinite_loops += 1
        
        print(f"Progress: {i}/{locations_to_check}")
    
    print(infinite_loops)
