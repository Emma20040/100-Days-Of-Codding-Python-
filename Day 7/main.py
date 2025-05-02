import random
import hangman_word
from hangman_arts import stages, logo


                                                                    
lives= 6
print(logo)

# randomly selects a letter from the list usin the wordlist file
chosen_word= random.choice(hangman_word.word_list)
# print(chosen_word) is used just for testing when playing the game comment it 
print(chosen_word)


display= []
word_lenght= len(chosen_word)
for _ in range(word_lenght):
    display +="_"
# print(display)


# checks if the letter the user selected is in chosen_word
end_of_game= False
# while loop to allow he game to continue untilll the list is completed
while not end_of_game:
    guess= input("Guess a letter\n").lower()
    # if the user has entered a letter that they've already guesses, print the letter and let them know
    if guess in display:
        print(f"you have already guessed {guess}")
    for position in range(word_lenght):
        letter= chosen_word[position]
        # print(f"current position {position}\n current letter {letter}\n guessed letter {guess}")
        if letter==guess:
            display[position]= letter

    if guess not in chosen_word:
        # if the letter is not in the chosen word, print out the
        # letter and let them know it is not in the chosen word

        print(f"you guessed {guess} this letter that is not in the  word, so you loss a life")
        lives -=1
        if lives ==0:
            end_of_game=True

        #join all the elements in the list and  turn it into a string
    print(f"{''.join(display)}")
    # condition for the while loop to stop
    if "_" not in display:
        end_of_game=True
        print("you win")
    print(stages[lives])