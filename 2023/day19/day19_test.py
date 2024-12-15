from day19 import do_workflow, is_part_accepted


def test_do_workflow_simple_A():
    test_part = {"x": 1, "m": 1, "a": 1, "s": 1}
    test_workflow = "A"
    assert do_workflow(test_part, test_workflow) == "A"


def test_do_workflow_simple_R():
    test_part = {"x": 1, "m": 1, "a": 1, "s": 1}
    test_workflow = "R"
    assert do_workflow(test_part, test_workflow) == "R"


def test_do_workflow_simple_other():
    test_part = {"x": 1, "m": 1, "a": 1, "s": 1}
    test_workflow = "vnc"
    assert do_workflow(test_part, test_workflow) == "vnc"


def test_do_workflow_greater_than_fail():
    test_part = {"x": 1, "m": 1, "a": 1, "s": 1}
    test_workflow = "x>10:A,R"
    assert do_workflow(test_part, test_workflow) == "R"


def test_do_workflow_greater_than_pass():
    test_part = {"x": 11, "m": 1, "a": 1, "s": 1}
    test_workflow = "x>10:A,R"
    assert do_workflow(test_part, test_workflow) == "A"


def test_do_workflow_less_than_fail():
    test_part = {"x": 1, "m": 1, "a": 10, "s": 1}
    test_workflow = "a<5:mrf,ccx"
    assert do_workflow(test_part, test_workflow) == "ccx"


def test_do_workflow_less_than_pass():
    test_part = {"x": 1, "m": 1, "a": 10, "s": 1}
    test_workflow = "m<5:mrf,ccx"
    assert do_workflow(test_part, test_workflow) == "mrf"


test_workflows = {
    "px": "a<2006:qkq,m>2090:A,rfg",
    "pv": "a>1716:R,A",
    "lnx": "m>1548:A,A",
    "rfg": "s<537:gd,x>2440:R,A",
    "qs": "s>3448:A,lnx",
    "qkq": "x<1416:A,crn",
    "crn": "x>2662:A,R",
    "in": "s<1351:px,qqz",
    "qqz": "s>2770:qs,m<1801:hdj,R",
    "gd": "a>3333:R,R",
    "hdj": "m>838:A,pv",
}


def test_is_part_accepted_true():
    test_part = {"x": 787, "m": 2655, "a": 1222, "s": 2876}
    assert is_part_accepted(test_part, test_workflows)


def test_is_part_accepted_false():
    test_part = {"x": 1679, "m": 44, "a": 2067, "s": 496}
    assert not is_part_accepted(test_part, test_workflows)
