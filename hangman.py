from os import system
import time

word = ["v","i","s","u","a","l","s","t","u","d","i","o"]
empty = ["v"," "," "," "," ","l","s"," "," "," "," ","o"]
move = 0
guess = ""
flag = 1
count = 0

def print_word():
    global count
    count = 0
    system('cls')
    print("Welcome to Word Guesser\n")
    for x in empty:
        if x == " ":
            print("_",end=" ")
            count+=1
        else:
            print(x,end=" ")
    print("\n\nYou have",10-move,"moves remaining")

def input_word():
    global guess
    guess = input("\nEnter a Guess: ")

def cmp_word():
    global guess
    global flag
    global move
    
    flag = 1

    i = 0
    while i<len(word):
        if guess == word[i]:
            empty[i] = guess
            flag = 0
            print("You guessed correctly")
            time.sleep(2)
        i+=1

    if flag:
        move+=1
        print("You guessed wrong, you lost 1 move")
        time.sleep(2)
            
while move<10:
    print_word()
    if count>0:
        input_word()
        cmp_word()
    else:
        break

if move>=10:
    print("You lost the game... Better Luck Next Time...")
elif count == 0:
    print("Congratulations, you won the game")