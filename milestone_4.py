import random
      
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_guessed = len(set([*self.word][self.word_guessed.index('_')]))
        self.list_of_guesses = []
        
    def check_guess(self, guess):
     self.guess_lower = guess.lower()
     if guess in self.word:
      print(f"Good guess! {guess} is in the word.")
      for character in self.word:
          if character == guess:
              self.word_guessed[self.word.index(character)] = character
      num_letters -= 1
     
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
  
test = Hangman(word_list = ['apple', 'mango', 'kiwi'])    
test.ask_for_input()
            
                
  
        
    
        
        
        