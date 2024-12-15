def parse_input(filename: str) -> list[list[int]]:
    output = []
    with open(filename) as f:
        for line in f:
            report = [int(number) for number in line.split(" ")]
            output.append(report)

    return output


def is_safe(report: list[int]) -> bool:
    ascending = report[0] < report[1]
    for i, num in enumerate(report[:-1]):
        diff = report[i + 1] - num

        if abs(diff) > 3 or abs(diff) < 1:
            return False

        if ascending and diff < 0:
            return False

        if not ascending and diff > 0:
            return False

    return True


def get_all_subreports(report: list[int]) -> list[list[int]]:
    subreports = []
    for i in range(len(report)):
        subreport = report[:i] + report[i + 1 :]
        subreports.append(subreport)

    return subreports


if __name__ == "__main__":
    reports = parse_input("input.txt")

    # Part 1
    safe_reports = sum(map(is_safe, reports))
    print(f"Part one answer: {safe_reports}")

    # Part 2
    safe_reports = 0
    for report in reports:
        if is_safe(report) or any(map(is_safe, get_all_subreports(report))):
            safe_reports += 1

    print(f"Part two answer: {safe_reports}")
