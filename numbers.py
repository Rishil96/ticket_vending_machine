from os import system


# Check if user input is valid
def is_input_valid(user_input):
    return user_input in ['1', '2', '3', '4']


# Clear screen
def clear_screen():
    system("cls")
