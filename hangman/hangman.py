import random
#--------------------
def check_word(display_word, word):
    """check word"""
    if display_word.lower() == word:
        print("You survived")
        return True
    else:
        return False

#--------------------
#Stage 7 + def letters
def check_letters(letter):
    """check letter"""
    if len(letter) != 1:
        print("You must enter one letter")
    if not letter.islower() or not letter.isalpha():
        print("You must enter English letter")
        return False
    return True
#--------------------

#Stage 8 + menu
#--------------------
while True:
    menu_choice = input('Enter "play" for play the game and "exit" to exit:> ').strip().lower()
    if menu_choice == "play":
#--------------------
#Stage 1
        print("HANGMAN")
#  print("The game will be soon")

#Stage 2
#Stage 3 (random)
#Stage 4 + help + "-"
#Stage 5 + letter in word
        word = ["python", "java", "php", "javascript"]
        word = random.choice(word)

#+ help
        #hlp = word[:3] + "-" * (len(word) - 3) # frst 3 real sym + -
        #print(f"The word is: {hlp}")

#Stage 5 -> + 8 attmp
        attemps = 8
        guess_letter = set()
        disp_word = "-" * len(word)

        while attemps > 0: # every time when attm lose atmp-1
            print(f"Current word:{disp_word}")
            print(f"Attemps :{attemps}")

            letter = input("Input a letter: >").lower().strip() #in lower st - spce

            if not check_letters(letter):
                continue

#--if letter already enter
            if letter in guess_letter:
                print("that letter already enter")
                continue

            guess_letter.add(letter)
#Stage 6
            #attemps = attemps - 1 # -1 attemp in right letter and wrong let

#---if letter in word
            if letter in word:
                disp_word = ''.join([char if char in guess_letter else '-' for char in word])
                #по 1 чару в рядку ворд если чар в списке тогда в результат додаэться сам чар
                #а якщо чар не входить до гесс_летт то замість нього додаємо -
                print("Good guess!!!")
            else:
                attemps = attemps - 1 #only when wrong attmp
                print("That latter not appear in the word")

#----check win
            if check_word(disp_word, word):
                break

            if attemps == 0:
                print("You lost")

# --------------------
#Stage 8 - exit
    elif menu_choice == "exit":
        print("Goodbye!")
        break

    else:
        print("Wrong input. Please try again.")
