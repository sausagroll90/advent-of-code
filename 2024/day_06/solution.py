def parse_input(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            grid.append(list(line.strip()))
    
    return grid


class Grid():
    def __init__(self, grid_map):
        self.grid_map = grid_map

    def __repr__(self):
        grid_string = ""
        for row in self.grid_map:
            grid_string += "".join(row) + "\n"
        grid_string = grid_string.strip()
        return grid_string
    
    def get_initial_guard_position(self):
        for row_num, row in enumerate(self.grid_map):
            if "^" in row:
                col_num = row.index("^")
                x = col_num
                y = row_num
                break
        
        return x, y
    
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


class Guard():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = [0, -1]

    def __repr__(self):
        return f"At ({self.x}, {self.y}) facing {self.direction}"
    
    def get_next_location(self):
        new_x = self.x + self.direction[0]
        new_y = self.y + self.direction[1]
        return new_x, new_y
    
    def update(self, new_square_contents):
        if new_square_contents == "." or new_square_contents == "X":
            self.x = self.x + self.direction[0]
            self.y = self.y + self.direction[1]
        elif new_square_contents == "#":
            self.direction = [-self.direction[1], self.direction[0]]


if __name__ == "__main__":
    INPUT_FILENAME = "input.txt"
    grid_map = parse_input(INPUT_FILENAME)

    grid = Grid(grid_map)

    guard_x, guard_y = grid.get_initial_guard_position()
    guard = Guard(guard_x, guard_y)

    while True:
        grid.mark_square(guard.x, guard.y)
        try:
            next_square_contents = grid.get_square_contents(*guard.get_next_location())
        except IndexError:
            print("left grid")
            break
        guard.update(next_square_contents)
    
    print(grid)
    print(grid.count_marked_squares())
