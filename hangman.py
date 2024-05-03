# hangman attempt

import random
import time

words = ["Bird", "Cow", "Chicken", "Mattress", "Television", "Computer", "Python"]
word = random.choice(words)
attempts = 6
guesses = []
done = False

def hint(w):
    if w == words[0]:
        print("HINT: can fly")
    elif w == words[1]:
        print("HINT: makes milk")
    elif w == words[2]:
        time.sleep(1)
        print("HINT: makes eggs")
    elif w == words[3]:
        print("HINT: you sleep on it")
    elif w == words[4]:
        print("HINT: where you can watch your favourite shows")
    elif w == words[5]:
        print("HINT: you can play games on it")
    elif w == words[6]:
        print("HINT: programming language")

print("type 'hint' if you need one")
while not done:
    time.sleep(0.5)
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")
    time.sleep(0.5)
    guess = input(f"attempts left: {attempts}; next guess: ")
    time.sleep(0.5)
    guesses.append(guess.lower())
    if guess.lower() == word.lower():
        done = True
        break
    if guess.lower() == "hint":
        hint(word)
    if guess.lower() not in word.lower():
        if guess.lower() == "hint":
            continue
        else:
            attempts -= 1
            if attempts == 0:
                break
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"you found the word, it was {word.lower()}.")
else:   
    print(f"you lose, the word was {word.lower()}.")