import EnglishDictionary
import math
def print_menu():
    print('Main Menu: ')
    print()
    print('1. Is it a palindrome?')
    print('2. Is it a crossword square?')
    print('3. Quit')

def get_menu_choice():
    selection = 0
    while selection <= 0:
        selection = int(input('Choose function: '))
    return selection
    #while loop is written so that selection has to be greater than 0 and if the user input is 0 or less than zero, input is asked again until greater than 0
    #the value that the user chose is then returned

def get_phrase():
    phrase = ''
    while len(phrase) <= 0:
        phrase = input("Enter a phrase: ")
    return phrase
    #while loop written so at least one character is inputted, if no characters are inputted, input is asked again until one character is inputted

def is_palindrome(phrase):
    phrase = phrase.lower()
    #.lower() function is so that the the user's string will all be lowercase letters so that uppercase letters will become lowercase and will be True if letters are the same when compared
    i = 0
    j = len(phrase) - 1
    #i starts at the beginning of string while j will start at the end of string to compare if beginning and end characters equal each other
    while i < j:
    #while loop runs if the position of character i is less than character j
        if not phrase[i].isalpha():
            i+=1
        #.isalpha function checks if a character is a letter
        #if loop will cause phrase[i] to increment by one if the character at phrase[i] is not an alphabet letter, and will stop and move on to elif statement if the character[i] is a letter
        elif not phrase[j].isalpha():
            j-=1
        #elif statement will check if phrase[j] is a letter, if it is not a letter then phrase[j] will decrement by one, and will stop when phrase[j] is at a letter
        else:
        #else statement will run if phrase[i] and phrase[j] are at letters and will run the if loop to check if the characters phrase[i] and phrase[j] are equal
            if phrase[i] != phrase[j]:
                return False
            #if phrase[i] and phrase[j] are equal, that means they are the same character and will continue to run until value of i = j, and will return True meaning it is a palindrome
            #if phrase[i] and phrase[j] are not equal, that means that the phrase is not a palindrome and will return False
            i+=1
            j-=1
    return True

def menu_check_palindrome():
# the function menu_check_palindrome combines the function get_phrase() and is_palindrome(phrase) so that this function will get a phrase from get_phrase() and save the prhase into into is_palindrome(phrase)
# if palindrome, which is a variable which equals and calls the function is_palindrome(phrase), is True, that means it is a palindrome and if false then is not a palindrome
    phrase = get_phrase()
    palindrome = is_palindrome(phrase)
    if palindrome == True:
        print(phrase, 'is a palindrome!')
    else:
        print(phrase, 'is not a palindrome!')

def get_crossword_square():
    st = input('Please enter the first word of the square: ')
    order = len(st)
    for i in range(0, order-1):
    # for loop is from 0 to order-1 because you want the user to enter the next couple words relative to the order of the first word which is the length of the first word
    # since the user already entered the first string the for loop it goes from 0 to order-1
    # for example a 4 letter word, you would want to ask the user to enter 4 words to make a square
    # since user already entered the first word, user should only be asked 3 more times to complete the square, which means with a for loop from range(0, order-1)
    # with order being = to length of the first word which is four letters, this means order is 4. This means user will be asked three more times from range(0, order-1) = (0, 4-1) = range(0, 3) in this example
    # meaning it will repeat three times to ask the user to input a word
        st = st + input('Please enter the next word of the square: ')
        # after user enters all the words, it will add the words together because strings can be concatenated and saved in one long string to be saved into one variable called st
    st = st.lower()
    # the function .lower() will lowercase all letters of the words that the user enters and will become a concatenated string and returned
    # this is done so that it doens't matter the format the user types in whether it's capital and lowercase, it will be all lowercase so that it can work with the EnglishDictionary function in the next function
    return st

def check_crossword_square(square):
    order = int(math.sqrt(len(square)))
    # because the square will be the concatenated string, the order will be the square root of the string depending on how many characters are in the string
    for i in range(0, len(square), order):
        horizontal_words = square[i:i+order]
        # for loop is written so that the i character will be determined by the order, or square root of the concatenated string
        # to get the horizontal words, we would go from i to i+order
        # an example to explain why I did this would be a string that has 16 characters, meaning the order is 4 because square root of 16 is 4. in order to get the horizontal words i would skip from 0 to 16 and land on every 4 characters
        # because the horizontal words is [i:i+order], in this example the first i would be 0 and i+order would be 0+4 and so the first word is from [0:4] which would be correct because it gives us first 4 characters, and so on and so on
        # this would continue as the for loop will give more i characters until it reaches end of the concatenated string
        check_horizontal_words = EnglishDictionary.is_word(horizontal_words)
        # after getting horizontal words, EnglishDictionary.isword() function will check if the words are even words to begin with
    for i in range(0, order):
        vertical_words = square[i::order]
        # there was a pattern to find the vertical words where if we started at one character and skipped to the end of the string using the stride, it would give us the vertical word
        # so thats why range(0, order) was used because starting at position 0 and skipping to the next character and the next until the end of the string using the stride, would give us first vertical word and so on in the for loop
        check_vertical_words = EnglishDictionary.is_word(vertical_words)
        # when vertical words are gotten, it will determine if vertical words are all words using EnglishDictionary.is_word() function
    if check_horizontal_words == True and check_vertical_words == True:
        return True
    return False
    # if horizontal words are all words and vertical words are all words then it would be a crossword square which will return True and will return False if either horizontal words is not a word or vertical word is not a word

def menu_check_crossword_square():
    crossword_string = get_crossword_square()
    # the function get_crossword_square() is called giving us a concatenated string of all the words the user entered and is stored in variable crossword_string
    print()
    crossword_square = check_crossword_square(crossword_string)
    # the function check_crossword_square() is called with the users concatenated string variable crossword_string in the parameter and is stored in variable crossword_square
    order = int(math.sqrt(len(crossword_string)))
    for i in range(0, len(crossword_string), order):
        horizontal_words = crossword_string[i:i+order]
        # in order to get horizontal words to print out in the output we would use the previous method to get horizontal words (see function check_crossword_square)
        print(horizontal_words)
    if crossword_square == True:
    # crossword_square gives us a boolean value if it is a crossword square and if it is True and equals True then it will print out is a crossword square, if False prints is not a crossword square
        print('is a crossword square!')
    else:
        print('is not a crossword square!')

def main():
    print_menu()
    selection = get_menu_choice()
    # print_menu() and get_menu_choice() is always called so that it will show up everytime when run
    # get_menu_choice() is saved in a variable selection so that it can be used in a loop to continue asking user to enter a function if user enters selection 1 or 2, but quits on selection 3
    while selection <= 2:
        if selection == 1:
            menu_check_palindrome()
        elif selection == 2:
            menu_check_crossword_square()
        #while loop is written so it will continue to ask the user for the function if selection is 1 or 2
        print_menu()
        selection = get_menu_choice()
        # after user runs through the if and elif clause, it will print_menu() and ask for the users selection again. If user enters 1 or 2 it will go through while loop again or quit if user enters 3

main()
        
        
        
        




    
        
