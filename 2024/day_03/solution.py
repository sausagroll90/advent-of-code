import re


def load_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def parse_mul_instruction(instruction: str) -> int:
    numbers = instruction.strip("mul()").split(",")
    return int(numbers[0]) * int(numbers[1])


if __name__ == "__main__":
    INPUT_FILE = "input.txt"
    corrupted_memory = load_input(INPUT_FILE)

    mul_regex_string = r"mul\(\d+,\d+\)"
    mul_instruction_regex = re.compile(mul_regex_string)
    mul_instruction_matches = mul_instruction_regex.finditer(corrupted_memory)

    dont_regex_string = r"don't\(\)"
    dont_instruction_regex = re.compile(dont_regex_string)
    dont_instruction_matches = dont_instruction_regex.finditer(corrupted_memory)

    do_regex_string = r"do\(\)"
    do_instruction_regex = re.compile(do_regex_string)
    do_instruction_matches = do_instruction_regex.finditer(corrupted_memory)

    all_matches = list(mul_instruction_matches) + list(dont_instruction_matches) + list(do_instruction_matches)
    all_matches_sorted = sorted(all_matches, key=lambda match: match.start())

    instruction_list = map(lambda match: match.group(), all_matches_sorted)
    
    do = True
    total = 0
    for instruction in instruction_list:
        if instruction == "do()":
            do = True
        elif instruction == "don't()":
            do = False
        elif do:
            total += parse_mul_instruction(instruction)

    print(total)
    