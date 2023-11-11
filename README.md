# Hangman

## Table of Contents
1. [Description](#description) 
2. [Usage](#usage)

### 1. Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### 2. Usage
List of attributes in the class Hangman:
1. word (string): a word to be guessed, picked randomly from the word_list using random.choice method
2. word_guessed (list): a list of the letters of the word, with _ for each letter not yet guessed
3. num_letters (int): a number of unique letters in the word that have not been guessed yet
4. num_lives (int): a number of lives the player has at the start of the game, which is 5 by default
5. word_list (list): a list of words
6. list_of_guesses (list): a list of the guesses that have already been tried

All the codes required to play the game is stored in milestone_5.py so you can start playing by
running milestone_5.py Python file.

