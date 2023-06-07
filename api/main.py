import sys
from service.calculators.alchemiser import alchemiser_calculator
from service.calculators.disassembler import disassembler_calculator

def main():
    #alchemiser_calculator()
    disassembler_calculator()
    return 0

if __name__ == '__main__':
    sys.exit(main())