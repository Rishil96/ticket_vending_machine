from os import system

PERFUME_TICKET_NUMBER = 0
MEDICINE_TICKET_NUMBER = 0
COSMETICS_TICKET_NUMBER = 0


# Check if user input is valid
def is_input_valid(user_input):
    return user_input in ['1', '2', '3', '4']


# Clear screen
def clear_screen():
    system("cls")


# Decorate Ticket
def ticket_message(function):
    def wrapper():
        print("\nYour number is:-")
        print(next(function()))
        print("wait and someone will be with you shortly.\n")

    return wrapper


# Ticket generator for cosmetics
@ticket_message
def get_cosmetics_ticket():
    global COSMETICS_TICKET_NUMBER
    COSMETICS_TICKET_NUMBER += 1
    while True:
        yield f"C-{COSMETICS_TICKET_NUMBER}"


# Ticket generator for medicines
@ticket_message
def get_medicine_ticket():
    global MEDICINE_TICKET_NUMBER
    while True:
        MEDICINE_TICKET_NUMBER += 1
        yield f"M-{MEDICINE_TICKET_NUMBER}"


# Ticket generator for perfume
@ticket_message
def get_perfume_ticket():
    global PERFUME_TICKET_NUMBER
    while True:
        PERFUME_TICKET_NUMBER += 1
        yield f"P-{PERFUME_TICKET_NUMBER}"


# Go back to home screen
def go_back():
    user_input = input("\nPress any button to go back to the home screen:- ")
    return bool(user_input)
