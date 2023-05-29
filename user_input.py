import constants

# alchemiser functions
def get_user_input():
    '''
    Takes user input and ensures it's valid then returns it after being formatted.
    '''
    
    user_input = input('What item would you like to check?> ').lower()

    while True:
        if validate_user_input(user_input):
            return user_input.capitalize()
        else:
            print('Input invalid, Please try again')
            user_input = take_user_input()

# helper functions
def validate_user_input(user_input):
    '''
    Checks user input, if all characters are valid, returns True,
    otherwise returns False.
    '''

    for char in user_input:
        if char not in constants.VALID_CHARS:
            return False

    return True

# disassembler functions
def validate_choice():
    '''
    Prints options to user and takes and ensures input is valid before returning it.
    '''

    # print options to screen along with index
    render_options()

    # take user choice
    choice = input('Please choose an item: ')

    # True or False, print error message if invalid
    valid = is_choice_valid(choice)
    
    # cycle until input is valid
    while not valid:
        render_options()
        choice = input('Please choose an item: ')
        valid = is_choice_valid(choice)

    return int(choice)

def is_choice_valid(choice):
    valid_choice = [idx for idx in range(len(constants.ITEMS))]

    if choice not in constants.VALID_NUMS:
        print('Invalid input. Input must be a single number!. Please try again.')
        return False
    if int(choice) not in valid_choice:
        print('Invalid selection. Please select one of the above options.')
        return False
    return True

def render_options():
    print('Which item are you going to disassemble?')

    for index, item in enumerate(constants.ITEMS):
        print(f'[{index}] {item}')