import random

print("Welcome to hangman!\n")

with open("hangman_list.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
word = random.choice(words)

guessed_word = list("_" * len(word))
lives = 15
wordGuessed = False

while lives>=1 and not wordGuessed == True:

    print(" ".join(guessed_word))

    user_guess = input("Guess a letter / word! ("+str(lives)+" lives remaining) (Guess the whole word after all letters have been filled) ")

    user_guess = user_guess.lower()

    letter_in_word = False
    for i in range(len(word)):
        if user_guess == word[i]:
            guessed_word[i] = user_guess
            letter_in_word = True
    
    if letter_in_word == False and user_guess != word:
        lives -= 1
        print("You guessed incorrectly")

    if user_guess == word:
        print(" ".join(guessed_word))
        print("You have guessed the word correctly")
        wordGuessed = True
        quit

    elif lives < 1:
        print("You have failed to guess the word")
        print("The word was ",word)
        quit