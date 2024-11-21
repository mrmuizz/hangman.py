#====================================
# Assignment 1, hangman.py
# Name: Abdul Muizz
# Roll no: 281134821
# Section: D
# Time spent: 24hrs
#====================================

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "ad.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if (secret_word == ""): #here we can consider an empty string to be a winning state
        return True  
    #beneath we will add unique letters to a new variable 
    unique_letters = [] #created an empty list to compare the winning state
    for i in range(len(secret_word)):
        letter = secret_word[i]
        if letter not in unique_letters:
            unique_letters.append(letter)
    #here we will compare bothg the secret word and the letters guessed
    for i in range(len(unique_letters)):  
        if unique_letters[i] not in letters_guessed:
            return False
            
    return True
        
    


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
  
    string = ""
    for i in range(len(secret_word)):  
        if secret_word[i] in letters_guessed:
            string += secret_word[i]
        else:
            string += "*"
    return string


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    str="abcdefghijklmnopqrstuvwxyz"
    list="abcdefghijklmnopqrstuvwxyz"
   
    for i in range(len(letters_guessed)):
        for j in range(len(list)):
            if letters_guessed[i]==list[j]:
                str = str.replace(letters_guessed[i],"")     #replaces the specific character with empty space
     
    return str       
    #print(str) 
    



def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    guess_limit = 10
    length=len(secret_word)
    letters_guessed = []
    print(f"Welcome to Hangman! The word is {len(secret_word)} letters long.")

    while guess_limit > 0:
        
        print(f"You have {guess_limit} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        if has_player_won(secret_word, letters_guessed):
            break
        guess = input("Please guess a letter: ").lower()
        
        
        if guess == '!' and with_help and guess_limit >=3:
            missing_letters = []
            for letter in secret_word:
                if letter not in letters_guessed:
                    missing_letters.append(letter)

            if missing_letters:
                revealed_letter = random.choice(missing_letters)
                letters_guessed.append(revealed_letter)  
                print(f"Letter revealed: {revealed_letter}")
                print(get_word_progress(secret_word, letters_guessed))
                guess_limit -= 3
                
            else:
                print("No letters left to reveal.")
            continue
        else:
            print("Oops!Not enough guesses left:",secret_word)
            
        
        
        
        if len(guess) < 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            guess_limit -= 1
            continue
            
        if guess in letters_guessed:
            print("Oops!You've already guessed that letter.",get_available_letters(letters_guessed))
            print("--------")
            continue

        letters_guessed.append(guess)

        if guess in secret_word:
            print("Good guess!",get_word_progress(secret_word, letters_guessed))
            print("-----------")
        
        else:
            print("Oops! That letter is not in my word.")
            if guess in 'aeiou':
                guess_limit -= 2  
            else:
                guess_limit -= 1
                
        
        
                
            
    if has_player_won(secret_word, letters_guessed):
        uniqueletters=0
        for i in range(length):
            for j in range(length):
                if(secret_word[i]==secret_word[j]):
                    uniqueletters=uniqueletters+1
                            
        total_score=guess_limit+4*uniqueletters+3*length
        print("Congratulations, you won!")
        print("Your total score for the game is: ",total_score)
    
    else:
        print(f"Sorry, you ran out of guesses. The word was '{secret_word}'.")
            
    
    
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

     secret_word = choose_word(wordlist)
     with_help = True
     hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your assignment. However, please run test_a1_student.py
    # one more time before submitting to make sure all the tests pass.
    

