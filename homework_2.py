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
    
        
