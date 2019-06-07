# Program that works like the Mad Libs game.

# Description: the program reads from a user's existing file containing the placeholders inputted by the user. The program would then ask for words to replace those placeholders. The program would then copy the results on to a new file and prints out the results. 

# TODO: update this
# Prerequisites:
# Make sure you have an existing text file with your sentence and the placeholder text be all uppercased (as per instructions from the book).
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

# Make  a comment and lowers comments here about this part of the program.
placeholder_list = []
while True:
    placeholder_input = input("What placeholder are you planning on using? (enter nothing to end): ")
    placeholder_input = placeholder_input.upper() # user input has to be uppercased because placeholder used in the text file is (per instructions) to be uppercase.
    if placeholder_input == "":
        break
    elif placeholder_input not in placeholder_list:
        placeholder_list.append(placeholder_input)

# Make a comment and lower comments here about this part of the program.
list_vowels = ["a", "e", "i", "o", "u"]
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in user_list_test:
    i_strip = i
    i_last_letter = i[-1]

    # If the placeholder doesn't end with a letter.
    if i_last_letter.lower() not in alphabet_list:
        i_strip = i.strip(i_last_letter)

    if i_strip in placeholder_list:
        test_index = user_list_test.index(i)

        # Checks on wether it uses "a" or "an" when asking for the placeholder input.
        if i_strip[0].lower() in list_vowels:
            answer = input(f"Enter an {i_strip}: ")
        else:
            answer = input(f"Enter a {i_strip}: ")
        print(user_text_file_read)

        # Checks if the previous word ends with a period so it can capitalize it.
        if user_list_test[user_list_test.index(i) - 1][-1] == ".":
            answer = answer.title()

        # Checks if the word ends with a punctuation.
        if i_last_letter.lower() in alphabet_list:
            user_list_test[test_index] = answer
        else:
            user_list_test[test_index] = answer + i_last_letter

# Combines the words from the new list into a sentence and prints out the results.
user_list_test_joined = " ".join(user_list_test)
print("")
print("Here is your new sentence!:")
print(user_list_test_joined)

# Copies the newly joined text into the results file. (I don't know why, the book said to do to this in accordance with its instructions.)
user_results_file.write(user_list_test_joined)
user_text_file.close()
user_results_file.close()
