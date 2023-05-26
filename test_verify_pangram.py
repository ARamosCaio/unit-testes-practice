import unittest
from pangram import verify_pangram

class VerifyPangramTest(unittest.TestCase):
    def test_method(self):
        
        sentence = "Not a pangram"
        is_pangram = verify_pangram(sentence)

        self.assertTrue(is_pangram)

    def test_method(self):
        sentence = "The quick brown fox jumps over a lazy dog"
        is_pangram = verify_pangram(sentence)

        self.assertTrue(is_pangram)