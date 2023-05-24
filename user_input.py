VALID_CHARS = 'abcdefghijklmnopqrstuvwxyz1234567890!&()/-+. '

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
        if char not in VALID_CHARS:
            return False

    return True