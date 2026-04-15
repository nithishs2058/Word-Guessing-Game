import random 
 
words = ["python", "java", "developer"] 
word = random.choice(words) 
guessed = ["_"] * len(word) 
attempts = 6 
 
while attempts > 0 and "_" in guessed: 
    print(" ".join(guessed)) 
    guess = input("Enter letter: ") 
 
    if guess in word: 
        for i in range(len(word)): 
            if word[i] == guess: 
                guessed[i] = guess 
    else: 
        attempts -= 1 
 
if "_" not in guessed: 
    print("You Win!") 
else: 
    print("You Lose! Word:", word)