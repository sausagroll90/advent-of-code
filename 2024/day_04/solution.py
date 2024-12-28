def parse_input(filename: str):
    wordsearch = []
    with open(filename) as f:
        for line in f:
            wordsearch.append(line.strip())
    
    return wordsearch


def index_in_range(row: int, col: int, wordsearch) -> bool:
    num_rows = len(wordsearch)
    num_cols = len(wordsearch[0])
    return row >= 0 and row < num_rows and col >= 0 and col < num_cols


def check_for_xmas(row: int, col: int, wordsearch) -> int:
    directions = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1)
    ]

    count = 0

    for direction in directions:
        d_x = direction[0]
        d_y = direction[1]
        if index_in_range(row + d_y, col + d_x, wordsearch) and wordsearch[row + d_y][col + d_x] == "M":
            if index_in_range(row + 2*d_y, col + 2*d_x, wordsearch) and wordsearch[row + 2*d_y][col + 2*d_x] == "A":
                if index_in_range(row + 3*d_y, col + 3*d_x, wordsearch) and wordsearch[row + 3*d_y][col + 3*d_x] == "S":
                    count += 1
    
    return count


def mas_cross_exists(window) -> bool:
    patterns = [
        [
            "M.M",
            ".A.",
            "S.S",
        ],
        [
            "M.S",
            ".A.",
            "M.S",
        ],
        [
            "S.S",
            ".A.",
            "M.M",
        ],
        [
            "S.M",
            ".A.",
            "S.M",
        ],
    ]

    for pattern in patterns:
        if check_pattern(pattern, window):
            return True
    
    return False


def check_pattern(pattern, window) -> bool:
    for i, row in enumerate(pattern):
        for j, letter in enumerate(row):
            if letter == ".":
                continue
            elif letter == window[i][j]:
                continue
            else:
                return False
    
    return True


if __name__ == "__main__":
    INPUT_FILENAME = "input.txt"
    wordsearch = parse_input(INPUT_FILENAME)

    # Part 1
    count = 0

    for i, row in enumerate(wordsearch):
        for j, letter in enumerate(row):
            if letter == "X":
                count += check_for_xmas(i, j, wordsearch)
    
    # print(count)

    # Part 2

    count = 0

    wordsearch_num_rows = len(wordsearch)
    wordsearch_num_cols = len(wordsearch[0])
    for row in range(wordsearch_num_rows - 2):
        for col in range(wordsearch_num_cols - 2):
            window = []
            for i in range(3):
                window.append(wordsearch[row + i][col:col+3])

            if mas_cross_exists(window):
                count += 1
    
    print(count)
