import unittest
from hangman import Hangman
from words import basic_words, intermediate_phrases

class TestHangman(unittest.TestCase):
    
    def setUp(self):
        self.basic_game = Hangman("basic")
        self.intermediate_game = Hangman("intermediate")
    
    def test_get_random_word_basic(self):
        """Test that get_random_word returns a valid basic word"""
        word = self.basic_game.get_random_word()
        self.assertIn(word, basic_words)
        self.assertIsInstance(word, str)
        self.assertTrue(len(word) > 0)
    
    def test_get_random_word_intermediate(self):
        """Test that get_random_word returns a valid intermediate phrase"""
        word = self.intermediate_game.get_random_word()
        self.assertIn(word, intermediate_phrases)
        self.assertIsInstance(word, str)
        self.assertTrue(len(word) > 0)
    
    def test_get_hidden_word(self):
        """Test that hidden word has correct underscores"""
        self.basic_game.secret_word = "TEST"
        hidden = self.basic_game.get_hidden_word()
        self.assertEqual(hidden, "____")
        
        self.basic_game.secret_word = "HELLO_WORLD"
        hidden = self.basic_game.get_hidden_word()
        self.assertEqual(hidden, "_____ _____")
    
    def test_process_guess_correct(self):
        """Test processing a correct guess"""
        self.basic_game.secret_word = "PYTHON"
        self.basic_game.hidden_word = "______"
        
        is_correct = self.basic_game.process_guess('P')
        self.assertTrue(is_correct)
        self.assertEqual(self.basic_game.hidden_word, "P_____")
        
        is_correct = self.basic_game.process_guess('Y')
        self.assertTrue(is_correct)
        self.assertEqual(self.basic_game.hidden_word, "PY____")
    
    def test_process_guess_incorrect(self):
        """Test processing an incorrect guess"""
        self.basic_game.secret_word = "PYTHON"
        self.basic_game.hidden_word = "______"
        
        is_correct = self.basic_game.process_guess('Z')
        self.assertFalse(is_correct)
        self.assertEqual(self.basic_game.hidden_word, "______")
    
    def test_process_guess_multiple_occurrences(self):
        """Test processing a guess that appears multiple times"""
        self.basic_game.secret_word = "BANANA"
        self.basic_game.hidden_word = "______"
        
        is_correct = self.basic_game.process_guess('A')
        self.assertTrue(is_correct)
        self.assertEqual(self.basic_game.hidden_word, "_A_A_A")
    
    def test_is_word_guessed(self):
        """Test word guessing detection"""
        self.basic_game.hidden_word = "PYTHON"
        self.assertTrue(self.basic_game.is_word_guessed())
        
        self.basic_game.hidden_word = "PYTH_N"
        self.assertFalse(self.basic_game.is_word_guessed())
        
        self.basic_game.hidden_word = "______"
        self.assertFalse(self.basic_game.is_word_guessed())
    
    def test_initial_game_state(self):
        """Test initial game state setup"""
        self.assertEqual(self.basic_game.lives, 6)
        self.assertEqual(self.basic_game.guessed_letters, [])
        self.assertFalse(self.basic_game.game_over)
        self.assertIsNotNone(self.basic_game.secret_word)
        self.assertIsNotNone(self.basic_game.hidden_word)

if __name__ == '__main__':
    unittest.main(verbosity=2)