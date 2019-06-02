# Program that works like the Mad Libs game.

# Description: the program reads from a user's existing file containing the placeholders NOUN, ADJECTIVE, ADVERB, or VERB, which the program would then ask for inputs to replace those placeholders. The program would then copy the results on to a new file and print it out (the results). MAKE THIS BETTER LOL AND CHANGE IF NOT HARDCODED 

# Prerequisites:
# Make sure you have an existing text file containing a sentence with the chosen words to be replaced to be changed to the placeholders. UPDATE THIS WTF LOL?
# In the line that contains user_text = open() and user_text_results = open(), the first arguments should be the absolute path of your text file.

# Creates a new file where the results will be copied onto.
user_results_file = open("/Users/ramteechua/Desktop/Files/Programming:Computer Science/Programming/HelloWorld/Automate The Boring Stuff With Python/Projects from book/mad_libs files/user_results.txt", "w")
# Reads the user's text file. 
user_text_file = open("/Users/ramteechua/Desktop/Files/Programming:Computer Science/Programming/HelloWorld/Automate The Boring Stuff With Python/Projects from book/mad_libs files/user_text.txt", "r")
user_text_file_read = user_text_file.read()

# Welcome message to the user.
print("Welcome to Mad Libs!\n")
print("Here is your sentence:")
print(user_text_file_read)
print("")

# Takes each word from the text file and stores them as an element in a list so that you can check if the words you're looking for (e.g. ADJECTIVE, NOUN, etc.) are available.
user_list_test = user_text_file_read.split()

# TODO: Repetitive CS50
# TODO: repetition on asking if noun a or an - cs50 
# TODO: try to make everything not hard code including the numbers of prompts for inputs per madlibs.
# TODO: make the madlibs (ADJECTIVES, NOUN, ETC) to variables you can change so it's not hardcoded?
# TODO: CHANGE COMMENTS IN LINE 34 AND 35 if the madlibs are not hardcoded anymore.

# Make  a comment and lowers comments here about this part of the program.
placeholder_list = []
while True:
    placeholder_input = input("What placeholder are you planning on using? (enter nothing to end): ")
    placeholder_input = placeholder_input.upper() # user input has to be uppercased because placeholder used in the text file is (indicated to be per instructions) to be uppercase.
    if placeholder_input == "":
        break
    elif placeholder_input not in placeholder_list:
        placeholder_list.append(placeholder_input)

# Make a comment and lower comments here about this part of the program.
for i in user_list_test:
    i_strip = i.strip(".")
    if i_strip in placeholder_list:
        test_index = user_list_test.index(i)      
        answer = input(f"Enter a {i_strip}: ")
        print(user_text_file_read)
        if i == i_strip:
            user_list_test[test_index] = answer
        else:
            user_list_test[test_index] = answer + "."

# Combines the words from the new list into a sentence and prints out the results.
user_list_test_joined = " ".join(user_list_test)
print("")
print("Here is your new sentence!:")
print(user_list_test_joined)

# Copies the newly joined text into the results file. (I don't know why, the book said to do to this in accorandance with its instructions.)
user_results_file.write(user_list_test_joined)
user_text_file.close()
user_results_file.close()

# Fix the a/an problem.
# TODO: what happens if the placeholder is the start of a sentence and needs to be capitalized?
