import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
num_of_placeholder = len(chosen_word)
print(num_of_placeholder * "_")
guess = input("Guess a letter: ").lower()



# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

# display = ""
# for i in chosen_word:
#     if i == guess:
#         display += guess
#     else:
#         display += "_"
# print(display)