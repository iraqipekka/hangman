#A list of words 
#Getting input from user (guess), has to be a single letter
#Has to track where the letters are in each word to check if guess is in the word

import random

WORDS = ["I LOVE MINECRAFT"]
MAX_TRIES = 7

while True:
    word = random.choice(WORDS)
    guessed = set()
    tries_remaining = MAX_TRIES

    while True:

        display = "".join(letter if letter in guessed else "_" for letter in word)
        display.replace("_", " ") 
        print(display)
        
        
        if "_" not in display:
            print(f"You win! The word was {word}!")
            exit()
        if tries_remaining == 0:
            print(f"You lost! The word was {word}")
            exit()     


        guess = input("Guess letter: ").upper()
        guessed.add(guess)
        if guess not in word: 
            print("Letter not in word")
            tries_remaining -= 1  
            print(f"Tries remaining: {tries_remaining} ")
        

   

    
    
        

    