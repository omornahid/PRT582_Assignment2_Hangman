import random
import time
import sys
from words import basic_words, intermediate_phrases

class Hangman:
    def __init__(self, level="basic"):
        self.level = level
        self.word_list = basic_words if level == "basic" else intermediate_phrases
        self.secret_word = self.get_random_word()
        self.hidden_word = self.get_hidden_word()
        self.lives = 6
        self.guessed_letters = []
        self.game_over = False
        
    def get_random_word(self):
        return random.choice(self.word_list)
    
    def get_hidden_word(self):
        hidden = []
        for char in self.secret_word:
            if char == '_':
                hidden.append(' ')
            elif char == ' ':
                hidden.append(' ')
            else:
                hidden.append('_')
        return ''.join(hidden)
    
    def process_guess(self, guess):
        guess = guess.upper()
        correct = False
        new_hidden = list(self.hidden_word)
        
        for i, char in enumerate(self.secret_word):
            if char == guess:
                new_hidden[i] = guess
                correct = True
        
        self.hidden_word = ''.join(new_hidden)
        return correct
    
    def is_word_guessed(self):
        return '_' not in self.hidden_word
    
    def display_game_state(self):
        """Display current game state"""
        print(f"\n{'='*50}")
        print(f"Lives: {self.lives} | Level: {self.level.upper()}")
        print(f"Word: {self.hidden_word}")
        print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")
        print(f"{'='*50}")
    
    def play_turn(self):
        self.display_game_state()
        
        print("\nYou have 15 seconds to guess a letter...")
        start_time = time.time()
        
        try:
            guess = input("Enter your guess: ").strip().upper()
            end_time = time.time()
            time_taken = end_time - start_time
            
            print(f"Time taken: {time_taken:.1f} seconds")
            
            # Check if time is up
            if time_taken > 15:
                self.lives -= 1
                print("Time's up! You lost a life.")
                return
            
            # Validate input
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter (A-Z)")
                return
                
            if guess in self.guessed_letters:
                print("You already guessed that letter!")
                return
                
            # Process the guess
            self.guessed_letters.append(guess)
            is_correct = self.process_guess(guess)
            
            if is_correct:
                print(f"Correct! '{guess}' is in the word.")
                if self.is_word_guessed():
                    self.game_over = True
                    print(f"Congratulations! You guessed it: {self.secret_word}")
            else:
                self.lives -= 1
                print(f"Wrong! '{guess}' is not in the word.")
                if self.lives <= 0:
                    self.game_over = True
                    print(f"Game Over! The word was: {self.secret_word}")
                    
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")

def choose_level():
    """Let player choose game level"""
    print("WELCOME TO HANGMAN!")
    print("Choose your level:")
    print("1. Basic (Single Words)")
    print("2. Intermediate (Phrases)")
    
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice == '1':
            return "basic"
        elif choice == '2':
            return "intermediate"
        else:
            print("Invalid choice. Please enter 1 or 2.")

def main():
    """Main game function"""
    level = choose_level()
    game = Hangman(level)
    
    print(f"\nGame started! The word has {len(game.secret_word)} characters.")
    print("You have 6 lives. Guess wisely!")
    
    while not game.game_over:
        game.play_turn()
    
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again == 'y':
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()