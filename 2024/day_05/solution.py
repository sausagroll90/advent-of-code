from functools import cmp_to_key


def parse_input(filename: str):
    with open(filename) as f:
        lines = f.readlines()
        new_line_index = lines.index("\n")
        orderings_lines = lines[:new_line_index]
        page_lists_lines = lines[new_line_index + 1:]
        orderings = [ordering.strip().split("|") for ordering in orderings_lines]
        page_lists = [page_list.strip().split(",") for page_list in page_lists_lines]
        
    return orderings, page_lists


def are_pages_in_order(page_list, orderings):
    for i in range(len(page_list) - 1):
        for j in range(i + 1, len(page_list)):
            ordering_to_check = [page_list[j], page_list[i]] # if reversed order is in required orderings, then page order is invalid
            if ordering_to_check in orderings:
                return False
    
    return True


def get_middle_page(page_list):
    return page_list[(len(page_list) - 1) // 2]


def get_comparison_function(orderings):
    def compare(page_a, page_b):
        if [page_a, page_b] in orderings:
            return -1
        elif [page_b, page_a] in orderings:
            return 1
        else:
            return 0
    
    return compare


if __name__ == "__main__":
    orderings, page_lists = parse_input("input.txt")

    # Part 1
    total = 0
    for page_list in page_lists:
        if are_pages_in_order(page_list, orderings):
            total += int(get_middle_page(page_list))

    print(total)

    # Part 2

    total = 0
    compare = get_comparison_function(orderings)

    for page_list in page_lists:
        if not are_pages_in_order(page_list, orderings):
            sorted_page_list = sorted(page_list, key=cmp_to_key(compare))
            total += int(get_middle_page(sorted_page_list))

    print(total)
