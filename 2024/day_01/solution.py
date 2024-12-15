def parse_input() -> tuple[list[int], list[int]]:
    list_a = []
    list_b = []
    with open("input.txt") as f:
        for line in f:
            numbers = line.split("   ")
            list_a.append(int(numbers[0]))
            list_b.append(int(numbers[1]))
    return list_a, list_b


if __name__ == "__main__":
    list_a, list_b = parse_input()

    # Part 1
    list_a_sorted = sorted(list_a)
    list_b_sorted = sorted(list_b)

    total = 0
    for a, b in zip(list_a_sorted, list_b_sorted):
        total += abs(a - b)

    print(f"Part 1 answer: {total}")

    # Part 2
    counts = {}

    for num in list_b:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    total = 0

    for num in list_a:
        if num in counts:
            total += num * counts[num]

    print(f"Part 2 answer: {total}")
