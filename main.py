import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
end_of_game = False
lives = 6
word_length = len(chosen_word)
display = []
current_guesses = []

print(logo)
print (f"\nThe answer is {chosen_word}")

for blanks in range(word_length):
    display.append("_")

while end_of_game == False:
    guess = input("\nGuess a letter: ").lower()
    
    if guess in current_guesses:
        print (f"\nYou've already guessed {guess}.")
        print(f"\n{' '.join(display)}")
    
    else: 
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        
        if guess not in chosen_word: 
            lives -= 1
            print(f"\nYou guessed {guess}, that's not in the word. You lose a life")
            if lives == 0:
                end_of_game = True
                print ("\nYou have ran out of lives. You lose!")

        print(f"\n{' '.join(display)}")
      
        if "_" not in display:
            end_of_game = True
            print("\nYou win!")
  
    current_guesses += guess
    print(stages[lives])