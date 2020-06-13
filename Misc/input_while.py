"""
Program: input_while.py
Author: Paul Elsea
Last Modified: 06/13/2020

Program to demonstrate input validation with while loops.
"""
'''Function that declares a list and sentinel value, then prompts user to populate list with numbers between 1 and 100'''
def get_numbers():
    continue_input = False
    input_list = []

    print("Please enter a number between 1 and 100 inclusive: ")
    '''While statement that prompts for user input of integer. Invalid input will result in exception handling
    and prompts for new input.'''
    while continue_input == False:
        try:
            input_num = int(input())
        except ValueError:
            print("Invalid input. Please use only numbers between 1 and 100")
            continue

        if input_num < 1:
            print("Please enter a number of 1 or above")
            continue
        if input_num > 100:
            print("Please enter a number of 100 or below")
            continue
        else:
            input_list.append(input_num)

        '''Section to determine if user wishes to add more numbers using if-else statement'''
        continue_choice = input("Would you like to enter another number? 'Y' to continue, any other key to exit.\n")

        if (continue_choice == "y") or (continue_choice == "yes") or (continue_choice == "Yes") or (continue_choice == "Y"):
            print("Please enter another number between 1 and 100")
            continue
        else:
            continue_input = True

    '''Final statement to print list after sentinel value has been tripped'''
    print('The final list is: ')
    for num in input_list:
        print(num)

if __name__ == '__main__':
    get_numbers()
'''Main method that calls get_numbers()'''