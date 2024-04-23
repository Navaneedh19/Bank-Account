import random
from hangman_words import word_list
chosen_word = random.choice(word_list)
world_len = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo

print(f'Pssst, the solution is {chosen_word}.')
display = [ ]
for _ in range(world_len):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed{guess}.")

    for position in range (world_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You lose a life.")            
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")


    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You Win.")
    from hangman_art import stages
    print(stages[lives])        