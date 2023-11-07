while True:
    guess = input("Please enter a single alphabetical character: ")
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        
        
word = "apple"       
if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")
    
def check_guess(guess):
    guess_lower = guess.lower()
    if guess in word:
      print(f"Good guess! {guess} is in the word.")
    else:
      print(f"Sorry, {guess} is not in the word. Try again.")
      

def ask_for_input():
    while True:
     guess = input("Please enter a single alphabetical character: ")
     if len(guess) == 1 and guess.isalpha():
        break
     else:
        print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)    
    
ask_for_input()