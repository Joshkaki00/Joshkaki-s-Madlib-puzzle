
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!

# Once upon a time in a (adjective) kingdom, there lived a (animal) named (name). This (animal) loved to (verb) every day. One day, it discovered a (adjective) (object) that changed its life forever. It decided to (verb) it to the (place) and share its adventure with (number) friends. Together, they embarked on a journey filled with (plural noun) and (emotion)!

print('Welcome to Madlib! When prompted, please fill in the blanks!')
print('Once upon a time, in a _ kingdom,')
adjective1 = input("Enter an adjective ")
print('there lived a _ named _.')
animal1 = input("Enter an animal: ")
name = input("Enter a name: ")
print ('This', animal1, 'loved to _ every day.')
verb1 = input("Enter a verb: ")
print('One day, it discovered a _ _ that changed its life forever.')
adjective2 = input('Enter an adjective: ')
noun = input('Enter a noun: ')
print('It decided to _ it to the _ and share its adventure with _ friends')
verb2 = input('Enter a verb: ')
place = input('Enter a place: ')
number = input('Enter a number: ')
print('Together, they embarked on a journey filled with _ and _!')
plural_noun = input('Enter a plural noun: ')
emotion = input('Enter an emotion: ')
print(f'Once upon a time in a {adjective1} kingdom, there lived a {animal1} named {name}. This {animal1} loved to {verb1} every day. One day, it discovered a {adjective2} {noun} that changed its life forever. It decided to {verb2} it to the {place} and share its adventure with {number} friends. Together, they embarked on a journey filled with {plural_noun} and {emotion}!')

exit()






































# --------------------------------------------------
# Partial solution
























# name = input("Name:")
# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")