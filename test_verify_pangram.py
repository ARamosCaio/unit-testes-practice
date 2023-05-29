import unittest
from pangram import verify_pangram

class VerifyPangramTest(unittest.TestCase):
    def test_method(self):
        sentence = input('Insira a frase: ')
        is_pangram = verify_pangram(sentence)

        self.assertEqual(is_pangram, False)
        #sentence = "The quick brown fox jumps over a lazy dog"
    
    def test_method(self):
        sentence = input('Insira a frase: ')
        is_pangram = verify_pangram(sentence)

        self.assertEqual(is_pangram, True)