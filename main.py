# Ticket Vending Machine
import numbers
import time

perfume_ticket = numbers.get_cosmetics_ticket()
medicine_ticket = numbers.get_cosmetics_ticket()
cosmetics_ticket = numbers.get_cosmetics_ticket()


def main():

    print("Welcome to the Ticket Vending Machine.")
    is_open = True

    while is_open:

        numbers.clear_screen()

        user_input = input("Which part of the store do you want to visit:-"
                           "\n[1] Perfumes.\n[2] Medicines.\n[3] Cosmetics.\n[4] Close Store"
                           "\nEnter your input: ")

        if not numbers.is_input_valid(user_input):
            print("Invalid Input. Try again in 3 seconds!")
            time.sleep(3)
            continue

        if user_input == "1":
            print("Welcome to Cosmetics Store")
            print(next(numbers.get_cosmetics_ticket()))
            time.sleep(3)

    return None


if __name__ == "__main__":
    main()