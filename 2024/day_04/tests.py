import unittest
from solution import check_pattern

class TestCheckPattern(unittest.TestCase):
    def test_simple_pass(self):
        pattern = [
            "A..",
            "...",
            "...",
        ]
        window = [
            "APC",
            "FOD",
            "BCU",
        ]

        self.assertTrue(check_pattern(pattern, window))

    def test_simple_fail(self):
        pattern = [
            "...",
            "...",
            ".A.",
        ]
        window = [
            "APC",
            "FOD",
            "BCU",
        ]

        self.assertFalse(check_pattern(pattern, window))
    
    def test_complex_pass(self):
        pattern = [
            "M.M",
            ".A.",
            "S.S",
        ]
        window = [
            "MMM",
            "AAK",
            "SOS",
        ]

        self.assertTrue(check_pattern(pattern, window))
    
    def test_complex_fail(self):
        pattern = [
            "FFF",
            "GGG",
            "VCB"
        ]
        window = [
            "FFF",
            "GGG",
            "VMK"
        ]

        self.assertFalse(check_pattern(pattern, window))
