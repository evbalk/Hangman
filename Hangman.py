import random

with open("wordlist.txt") as f:
    lines = f.readlines()

rand_num = random.randrange(len(lines))
WORD = lines[rand_num]

num_strikes = int(input("How many strikes would you like?"))
answer = ''
display = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter in WORD:
    answer += "_"

past_guesses = ''

while num_strikes > 0 and answer != WORD:

    guess = input("Guess: ").lower()
    print(guess)

    while guess not in alphabet:
        print("Guess was not a letter")
        guess = input("Guess: ").lower()

    while guess in past_guesses:
        print("You've already guessed %s" % guess)
        guess = input("Guess: ").lower()

    if guess not in WORD:
        print(guess + " is wrong")
        num_strikes -= 1
    else:
        for location, letter in enumerate(WORD):
            if letter == guess:
                answer = answer[:location] + letter + answer[
                                                      location + 1:]  # splice before letter, add letter, add back

    display = ''
    for ch in answer:
        display += ch + ' '
    print(display)
    print(str(num_strikes) + " stikes left!")
    print("---------------\n")
    past_guesses += guess

if answer == WORD:
    print("Congratulations, you win! The word was: %s" % WORD)
else:
    print("You lose! The correct word was: %s" % WORD)
