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
    phrase = get_phrase()
    palindrome = is_palindrome(phrase)
    if palindrome == True:
        print(phrase, 'is a palindrome!')
    else:
        print(phrase, 'is not a palindrome!')

def get_crossword_square():
    st = input('Enter first string: ')
    order = len(st)
    for i in range(0, order-1):
        st = st + input('Enter next string: ')
    return st

def check_crossword_square(square):
    order = int(math.sqrt(len(square)))
    for i in range(0, len(square), order):
        horizontal_words = square[i:i+order]
        check_horizontal_words = EnglishDictionary.is_word(horizontal_words)
    for i in range(0, order):
        vertical_words = square[i::order]
        check_vertical_words = EnglishDictionary.is_word(vertical_words)
    if check_horizontal_words == True and check_vertical_words == True:
        return True
    return False

def menu_check_crossword_square():
    crossword_string = get_crossword_square()
    print()
    crossword_square = check_crossword_square(crossword_string)
    order = int(math.sqrt(len(crossword_string)))
    for i in range(0, len(crossword_string), order):
        horizontal_words = crossword_string[i:i+order]
        print(horizontal_words)
    if crossword_square == True:
        print('is a crossword square!')
    else:
        print('is not a crossword square!')

def main():
    print_menu()
    selection = get_menu_choice()
    while selection <=2:
        if selection == 1:
            menu_check_palindrome()
        elif selection == 2:
            menu_check_crossword_square()
        print_menu()
        selection = get_menu_choice()

main()
        
        
        
        




    
        
