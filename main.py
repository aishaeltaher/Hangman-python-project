import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
n0mbers_letters = len(chosen_word)

lives = 6

from hangman_arts import logo
print(logo)

print(f"The chosen word is {chosen_word}")

display = []

for _ in range (n0mbers_letters):
  display += "_"
print(display)

end_of_game = False

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
  
    for position in range (0, n0mbers_letters):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        print(f"You've guessed {guess}, it's not in the chosen word.")
        lives -= 1
        if lives == 0:
          end_of_game = True
          print("You lose")
    list = ' '.join(display)
    print(list)
            

    if "_" not in display:
         end_of_game = True
         print("You win")

    from hangman_arts import stages
    print(stages[lives])
