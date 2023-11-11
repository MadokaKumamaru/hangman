# Import random module which is one of Python's built-in modules
import random
      
# Define the class Hangman with 2 parameters, 6 attributes, and 2 methods      
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        
    
    def check_guess(self, guess):
     self.guess_lower = guess.lower()
     if guess in self.word:
      print(f"Good guess! {guess} is in the word.")
      for index, item in enumerate(self.word):
          if item == guess:
              self.word_guessed[index] = item
              print(self.word_guessed)
      self.num_letters -= 1
     else:
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.") 
        print(f"You have {self.num_lives} lives left.")
      
     
    def ask_for_input(self):
        while True:
            guess = input('Please enter a single alphabetical character: ')
            if len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
                
# Define a function play_game() with 1 parameter  
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0:
            print("Congradurations. You won the game!")
            break

# Create a word_list with 5 words and try the game using play_game() function
word_list = ['banana', 'strawberry', 'apple', 'lychee', 'mango']
play_game(word_list)