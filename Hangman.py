import random

with open("wordlist.txt") as f:
    lines = f.readlines()

rand_num = random.randrange(len(lines))
WORD = lines[rand_num].rstrip()

difficulty = input("Difficulty: 'e': 10 strikes, 'm' 7: strikes, 'h': 5 strikes").lower()

if difficulty == 'e':
    num_strikes = 10
elif difficulty == 'm':
    num_strikes = 7
elif difficulty == 'h':
    num_strikes = 10
else:
    num_strikes = 7

answer = ''
display = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
initial = ''

for letter in WORD:
    answer += "_"
    initial += "_ "

past_guesses = ''
print(initial)

# print(WORD)
print(str(len(WORD)) + " letters")
print(".............")
print("\n")
while num_strikes > 0 and answer != WORD:

    if past_guesses:
        print("Already Guessed: %s" % past_guesses)

    guess = input("Guess: ").lower()

    while len(guess) != 1:
        print("You guessed more than one letter!")
        guess = input("Guess: ").lower
        
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
        print(guess + " is right!")
        for location, letter in enumerate(WORD):
            if letter == guess:
                answer = answer[:location] + letter + answer[
                                                      location + 1:]  # splice before letter, add letter, add back

    display = ''
    for ch in answer:
        display += ch + ' '
    print(display)
    print(str(num_strikes) + " strikes left!")
    print(".............\n")
    past_guesses += guess

if answer == WORD:
    print("Congratulations, you win! The word was: %s" % WORD)
else:
    print("You lose! The correct word was: %s" % WORD)
