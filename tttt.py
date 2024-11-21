if secret_word == "":
        return True  # An empty word can be considered "won"
    
    # Create a list of unique letters in the secret word
    unique_letters = []
    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)

    # Check if all unique letters have been guessed
    for i in range(len(unique_letters)):  # Using 'i' as the index variable
        if unique_letters[i] not in letters_guessed:
            return False
            
    return True



flg=False
    for i in range(len(secret_word)):
        for j in range(len(letters_guessed)):
            if secret_word[i]==letters_guessed[j]:
                flg=True
            else:
                flg=False
      
    return flg




all_letters = string.ascii_lowercase  # Get all lowercase letters
    available_letters = ""  # Initialize an empty string for available letters

    for letter in all_letters:
        if letter not in letters_guessed:
            available_letters += letter  # Concatenate letters that haven't been guessed

    # Create a sorted list from available letters
    sorted_available_letters = ""
    for letter in all_letters:  # Iterate through all_letters again to maintain order
        if letter in available_letters:
            sorted_available_letters += letter  # Build the sorted string

    return sorted_available_letter





str="abcdefghijklmnopqrstuvwxyz"
    list="abcdefghijklmnopqrstuvwxyz"
   
    for i in range(len(letters_guessed)):
        for j in range(len(list)):
            if letters_guessed[i]==list[j]:
                str = str.replace(letters_guessed[i],"")     #replaces the specific character with empty space
     
    return str       
    #print(str)




if(userinput.isalpha()):
            if(has_player_won(secret_word,userinput)==True):
                print("Congratulations, you won!")
                uniqueletters=0
                for i in range(length):
                    for j in range(length):
                        if(secret_word[i]==secret_word[j]):
                            uniqueletters=uniqueletters+1
                            
                total_score=guess+4*uniqueletters+3*length 
                print("Your total total score for the game is: ",total_score)
            elif(with_help==True):
                if guess>2:
                    guess=guess-3
                    print(get_word_progress(secret_word,userinput))
            elif(guess<1):
                print(" Oops! Not enough guesses left:")
                print("Sorry, You ran out of guesses. The word was ",secret_word)
            else:
                for i in range(length):
                    if(secret_word[i]==userinput):
                        print("Good guess:",get_word_progress(secret_word,userinput))
                        print("---------------")
                    elif(userinput=='a'or userinput=='e'or userinput=='i'or userinput=='o'or userinput=='u'):
                        guess=guess-2
                    else:
                        guess=guess-1
        
        
        else:
            guess = guess-1
            print("Incorrect Statement. Please guess either a letter or !.")