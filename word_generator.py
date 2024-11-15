from wonderwords import RandomWord

# Method to generate a word using wonderwords.
# Word is customizable in size as well as in start and end characters for an easy mode.
# Returns the chosen word to be used in the hangman game.
def generate_word():
    # loop if invalid input or no word generated
    while True:
        answer = input("Would you like to set restrictions on the word? "
                       "Type Y for easy mode and N for hard mode! ").strip().upper()
        if answer == "N":
            r = RandomWord()
            chosen_word = r.word()
            return chosen_word
        
        elif answer == "Y": 
            
            start = input("What should the word start with? Type 'anything' if no preference.")
            if start.lower() != "anything" and not start.isalpha():
                print("Invalid input. Please enter alphabetic characters only.")
                continue
            else:
                word_start = "" if start.lower() == "anything" else start
            

            end = input("What should the word end with? Type 'anything' if no preference")
            if end.lower() != "anything" and not end.isalpha():
                print("Invalid input for the end. Please enter alphabetic characters only.")
                continue
            else:
                word_end = "" if end.lower() == "anything" else end

            min_length = input("What should the word's minimum length be?")
            if min_length.isnumeric():
                word_min = int(min_length) # cast string input to int
            else:
                print("Invalid input for word minimum length. Please enter an integer.")
                continue


            max_length = input("What should the word's max length be?")
            if max_length.isnumeric():
                word_max = int(max_length)
            else:
                print("Invalid input for word maximum length. Please enter an integer.")
                continue

            r = RandomWord()
            # try to create the word
            try:
                chosen_word = r.word(
                    starts_with = word_start, 
                    ends_with= word_end, 
                    word_min_length= word_min, 
                    word_max_length=word_max)
                return chosen_word
            
            # no word available in wonderwords database, loop back to top
            except Exception as e:
                print("No word available with those restrictions.")
                
        else:
                print("Invalid input. Please type Y or N")
    
