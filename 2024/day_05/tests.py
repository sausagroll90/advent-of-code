import unittest
from solution import parse_input, are_pages_in_order, get_middle_page, get_comparison_function


class TestArePagesInOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.orderings, cls.page_lists = parse_input("test_input.txt")

    def test_in_order(self):
        result = are_pages_in_order(self.page_lists[0], self.orderings)
        self.assertTrue(result)

    def test_not_in_order(self):
        result = are_pages_in_order(self.page_lists[4], self.orderings)
        self.assertFalse(result)


class TestGetMiddlePage(unittest.TestCase):
    def test_three_pages(self):
        page_list = ["24", "43", "1"]
        self.assertEqual(get_middle_page(page_list), "43")
    
    def test_seven_pages(self):
        page_list = ["1", "2", "3", "4", "5", "6", "7"]
        self.assertEqual(get_middle_page(page_list), "4")


class TestGetComparisonFunction(unittest.TestCase):
    def test_less_than(self):
        comparisons = [['1', '2'], ['99', '1']]
        compare = get_comparison_function(comparisons)
        self.assertEqual(compare('1', '2'), -1)
    
    def test_greater_than(self):
        comparisons = [['1', '2'], ['99', '1']]
        compare = get_comparison_function(comparisons)
        self.assertEqual(compare('2', '1'), 1)

    def test_equal(self):
        comparisons = [['1', '2'], ['99', '1']]
        compare = get_comparison_function(comparisons)
        self.assertEqual(compare('99', '55'), 0)  
