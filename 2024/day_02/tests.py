import unittest
from solution import is_safe, get_all_subreports


class TestIsSafe(unittest.TestCase):
    def test_safe_asc(self):
        report = [1, 2, 5, 7]
        self.assertTrue(is_safe(report))

    def test_safe_desc(self):
        report = [9, 6, 5, 2]
        self.assertTrue(is_safe(report))

    def test_unsafe_asc(self):
        report = [1, 2, 7]
        self.assertFalse(is_safe(report))

    def test_unsafe_desc(self):
        report = [9, 3]
        self.assertFalse(is_safe(report))

    def test_unsafe_not_asc(self):
        report = [1, 3, 2]
        self.assertFalse(is_safe(report))


class TestGetAllSubreports(unittest.TestCase):
    def test_get_all_subreports(self):
        report = [1, 2, 3]
        expected = [[2, 3], [1, 3], [1, 2]]
        self.assertEqual(get_all_subreports(report), expected)
