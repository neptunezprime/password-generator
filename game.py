
import random
#Picking random words
word_list = ["ardvark", "baboon", "camel"]
for word in word_list :
    chosen_word = random.choice(word_list)

#this is for generating a list
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

end_of_game = False
while end_of_game == False:
    guess = input("guess a letter:").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"current position: {position}\n current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print (display)


    
    if "_" not in display:
        end_of_game = True
        print("you win")
       

