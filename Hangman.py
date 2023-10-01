import random

Graphics = (
"""
""",

"""
    
    
    
    
    
    
    
    ___________
    """,

"""
    
    |
    |
    |
    |
    |
    |
    |__________
    """,

"""
    _______
    |      
    |
    |
    |
    |
    |
    |__________
    """,

"""
    _______
    |      |
    |
    |
    |
    |
    |
    |__________
    """,

"""
    _______
    |      |
    |     (_)
    |
    |
    |
    |
    |__________
    """,

"""
    _______
    |      |
    |     (_)
    |      |
    |      |
    |
    |
    |__________
    """,

"""
    _______
    |      |
    |     (_)
    |     /|
    |    / |
    |
    |
    |__________
    """,

"""
    _______
    |      |
    |     (_)
    |     /|\ 
    |    / | \ 
    |
    |
    |__________
    """,

"""
    _______
    |      |
    |     (_)
    |     /|\ 
    |    / | \ 
    |     /
    |    /
    |__________
    """,

"""
    _______
    |      |
    |     (_)
    |     /|\ 
    |    / | \ 
    |     / \ 
    |    /   \ 
    |__________
    """)

quits = ""

while quits != "q":
    print("Welcome to hangman!\n")

    wrong = 0

    with open("hangman_list.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    word = random.choice(words)

    guessed_word = list("_" * len(word))
    lives = 10
    wordGuessed = False

    incorrectletters = []

    while lives>=1 and not wordGuessed == True:

        print(" ".join(guessed_word))

        user_guess = input("Guess a letter / word! ("+str(lives)+" lives remaining) (Guess the whole word after all letters have been filled) ").lower()

        letter_in_word = False
        for i in range(len(word)):
            if user_guess == word[i]:
                guessed_word[i] = user_guess
                letter_in_word = True
        
        if letter_in_word == False and user_guess != word:
            lives -= 1
            print("You guessed incorrectly")
            wrong = wrong + 1
            print (Graphics[wrong])
            incorrectletters.append(user_guess)
            print("Previously guessed letters are: ", ( incorrectletters))

        if user_guess == word:
            print(" ".join(guessed_word))
            print("You have guessed the word correctly")
            wordGuessed = True
            quits = input("Press q to quit or enter to continue")
            quits = quits.lower()

        elif lives < 1:
            print("You have failed to guess the word")
            print("The word was ",word)
            quits = input("Press q to quit or enter to continue")
            quits = quits.lower()
quit