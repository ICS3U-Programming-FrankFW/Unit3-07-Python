#!/usr/bin/env python3
# Created by: Frankie fox
# Created on: Oct 20, 2022
# This program sees if you are old enough or too young to date my grandchild


def main():

    user_string = input("Enter your age:")
    print()

    try:
        # Cast user_string to an int
        user_string_as_int = int(user_string)

        # This checks if you're too old
        if user_string_as_int > 40:
            print("you are too old to date my grandchild")

        # This checks if you are just right
        elif user_string_as_int > 25 and user_string_as_int < 40:
            print("you can date my grandchild")

        # This checks if you are too young
        elif user_string_as_int < 25:
            print("You are too young to date my grandchild")
    except Exception:
        print("This is not an integer ")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
