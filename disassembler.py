class Disassembler_Calculator():
    
    def __init__(self):
        # initialise constants needed for calculator
        self.CHARGES_PER_ITEM = 3.8
        self.CORRUPTED_MAGIC_LOGS_ID = 40338
        self.DIVINE_CHARGE_ID = 36390
        self.ITEMS_PROCESSED_PER_HOUR = 60
        self.MAGIC_LOGS_ID = 1513
        self.SOAPSTONE_ID = 49458
        self.LOGS_COMPS = {
            'simple parts': 0.99,
            'junk': 0.034
        }
        self.SOAPSTONE_COMPS = {
            'special': {
                'historic': 0.16,
                'classic': 0.4
                },
            'normal': {
                'simple parts': 1.0,
                'junk': 27.2
            }
        }

    # helper methods
    def cost_of_charges(self):

        # returns cost of charges needed to process 1 item
        return self.CHARGES_PER_ITEM * self.cost_of_charge()

    def cost_of_charge(self):

        # returns the current cost of 1 charge
        charge_cost = get_item_cost(self.DIVINE_CHARGE_ID) / 3000
        charge_cost = round(charge_cost, 2)

        return charge_cost
    
    def validate_choice(self):

        # define list of 3 items
        options = self.define_options()

        # print options to screen along with index
        self.render_options(options)

        # take user choice
        choice = self.take_choice()

        # True or False, print error message if invalid
        valid = self.is_choice_valid(choice)
        
        # cycle until input is valid
        while not valid:
            self.render_options(options)
            choice = self.take_choice()
            valid = self.is_choice_valid(choice)

        return choice

    def is_choice_valid(self, choice):
        VALID_CHARS = '012'

        if choice not in VALID_CHARS:
            print('Invalid selection please try again.')
            return False
        if len(choice) > 1:
            print('Input can only be 1 number! Please try again.')
            return False

        return True

    def take_choice(self):
        choice = input('Please choose an item: ')
        return choice

    def render_options(self, options):
        print('Which item are you going to disassemble?')

        for index, item in enumerate(options):
            print(f'[{index}] {item}')

    def define_options(self):
        options = ['magic logs', 'corrupted magic logs', 'soapstone']
        return options

    def get_item_value(self, choice):
        item_cost = get_item_cost(choice)
        return item_cost