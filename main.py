# Ticket Vending Machine
import generator_functions
import time


def main():

    print("Welcome to the Ticket Vending Machine.")
    is_open = True

    while is_open:

        generator_functions.clear_screen()

        user_input = input("Which part of the store do you want to visit:-"
                           "\n[1] Perfumes.\n[2] Medicines.\n[3] Cosmetics.\n[4] Close Store"
                           "\nEnter your input: ")

        if not generator_functions.is_input_valid(user_input):
            print("Invalid Input. Try again in 3 seconds!")
            time.sleep(3)
            continue

        if user_input == "1":
            generator_functions.clear_screen()
            print("Welcome to Perfume Store.")
            generator_functions.get_perfume_ticket()
            generator_functions.go_back()

        elif user_input == "2":
            generator_functions.clear_screen()
            print("Welcome to Medicine Store.")
            generator_functions.get_medicine_ticket()
            generator_functions.go_back()

        elif user_input == "3":
            generator_functions.clear_screen()
            print("Welcome to Cosmetics Store.")
            generator_functions.get_cosmetics_ticket()
            generator_functions.go_back()

        else:
            generator_functions.clear_screen()
            print("\nThe store is now closed. Come back again tomorrow :)")
            is_open = False

    return None


if __name__ == "__main__":
    main()
