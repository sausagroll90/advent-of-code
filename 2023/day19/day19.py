def do_workflow(part, workflow):
    steps = workflow.split(",")
    for step in steps:
        if ">" in step:
            condition, outcome = step.split(":")
            categoryToCompare, valueToCompareAgainst = condition.split(">")
            if part[categoryToCompare] > int(valueToCompareAgainst):
                return outcome
        elif "<" in step:
            condition, outcome = step.split(":")
            categoryToCompare, valueToCompareAgainst = condition.split("<")
            if part[categoryToCompare] < int(valueToCompareAgainst):
                return outcome
        else:
            return step


def is_part_accepted(part, workflows):
    result = do_workflow(part, workflows["in"])
    while True:
        if result == "A":
            return True
        elif result == "R":
            return False
        else:
            result = do_workflow(part, workflows[result])


def main():
    workflows = {}
    parts = []

    with open("input.txt") as f:
        for line in f:
            if line.startswith("{"):
                part = {}
                for property in line[line.index("{") + 1 : line.index("}")].split(","):
                    category, value = property.split("=")
                    part[category] = int(value)
                parts.append(part)
            elif line != "\n":
                workflow_name, workflow = line.split("{")
                workflow = workflow.split("}")[0]
                workflows[workflow_name] = workflow

    accepted_parts = [part for part in parts if is_part_accepted(part, workflows)]

    grand_total = 0
    for part in accepted_parts:
        grand_total += sum(part.values())

    print(grand_total)


if __name__ == "__main__":
    main()
