from os import system


# Check if user input is valid
def is_input_valid(user_input):
    return user_input in ['1', '2', '3', '4']


# Clear screen
def clear_screen():
    system("cls")


# Ticket generator for cosmetics
def get_cosmetics_ticket():
    ticket_number = 0
    while True:
        ticket_number += 1
        yield f"C-{ticket_number}"


# Ticket generator for medicines
def get_medicine_ticket():
    ticket_number = 0
    while True:
        ticket_number += 1
        yield f"M-{ticket_number}"


# Ticket generator for perfume
def get_perfume_ticket():
    ticket_number = 0
    while True:
        ticket_number += 1
        yield f"P-{ticket_number}"


# Go back to home screen
def go_back():
    user_input = input("\nPress any button to go back to the home screen:- ")
    return bool(user_input)
