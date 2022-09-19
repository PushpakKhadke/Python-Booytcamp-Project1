# import Module
import random
import os
import sys
from termcolor import colored

# function for clear cmd
def clear(): os.system('cls')

def Word_Puzzle_Game():
    # input name
    name = input("Enter Your  Name:\n")
    clear()
    name = name.title()
    NAME = colored("Welcome, {}".format(name), "red")
    print(NAME)
    input("Press Enter key to continue_ _ _ ")
    clear()

    # print game title and information
    print()
    TITLE = colored("\t\t\t\tWord Puzzle Game!")
    print(TITLE)
    print()
    RULES = colored("\t\t\tInformation of the game!", "red")
    print(RULES)
    print()
    INFO = colored("1. Arrange the appropriate word to answer the question","yellow")
    INFO1=colored("2.Limited Moves 5","yellow")
    INFO2=colored("3.Your total number of move will decrease by 1","yellow")
    INFO3=colored("4.Each Correct ans your score is +1","yellow")
    INFO4=colored("5.Each Wrong ans your score is -1","yellow")
    INFO6=colored("6.once's finished  moves will end then print your result","yellow")
    print(INFO)
    print(INFO1)
    print(INFO2)
    print(INFO3)
    print(INFO4)
    print(INFO6)
    print()
    input("Press Enter key to continue_ _ _ ")
    clear()
    print("Player Name:", name)
    print()
    Words_Gusses = colored("\t\t Limited Moves only 5 time", "blue")
    print(Words_Gusses)

    # main code
    list = ["Green", "Bat", "Father", "Black", "Aeroplane", "Small", "Kite", "Parrot", "Mysirg", "Telusko", "Ineuron","Computer"]
    User_word = set()
    Score = 0  # score
    Gusses = 1  # Number of Gusses
    Limited_moves = 4  # Limited Moves

    while Gusses <= 5:  # condition 1<=5
        word = random.choice(list)  # random choice from list
        word = word.upper()  # Convert random choice in uppercase
        if word in User_word:  # check word in used_Word
            continue  # continue
        User_word.add(word)  # used_word add in word
        computer_word = word
        word = ''.join(random.sample(word, len(word)))  #
        print()
        print("Arrange the letters to form a valid word")  # Printing Message
        print("Letter is:", word)  # Print word in random sequence
        user_word = input("Guess the Word:")  # Enter answer here
        if user_word.upper() == computer_word:  # check_User word  == computer_word
            Correct = colored("Correct", "cyan")
            print(Correct)
            Score += 1
        else:
            Wrong = colored("Wrong", "cyan")
            print(Wrong)
            Score -= 1

        print("Correct Word is:", computer_word)
        print("Your Remaning Moves:", Limited_moves)
        print("Your  Score is:", Score)
        Limited_moves -= 1
        Gusses += 1
    print()
    print("Your Final Score 5 Out of:", Score)
    print()

    again = input("If you want to exit enter 'exit' and if you want to play more enter 'continue'\n")
    if again == "continue":
        clear()
        Word_Puzzle_Game()

    elif again == "exit":
        exit()
    else:
        pass
Word_Puzzle_Game()
