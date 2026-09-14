import random as r
import string as s

characters = list(
    s.ascii_lowercase +
    s.ascii_uppercase +
    s.digits +
    s.punctuation
)

    punctuation = True
    characters_to_exclude = []
    lower_upper_both = "both"
    length = 16


def main():
    global characters
    global punctuation
    global characters_to_exclude
    global lower_upper_both
    global length

    print("Welcome to my password generator!")
    print("Choose which setting you would like to change or simply generate the password!")

    while True:
        print(f"1. Set the length of my password (current: {length} characters)")
        print(f"2. Set the characters to be just lowercase/uppercase/both (current: {lower_upper_both})")
        print(f"3. Set which characters to exclude (current: {characters_to_exclude})")
        print("4. Generate my password!")
        print("5. Exit the generator")
        choice = input("Please select your option: ")
        if choice == "1":
            input_length = input("Please type your preferred length of characters: ")
            length = input_length

        elif choice == "2":
            while True:
                print("Which setting you'd like to continue with?")
                print("1. Just lowercase characters")
                print("2. JUST UPPERCASE CHARACTERS")
                print("3. Both lowercase and UPPERCASE characters")
                print("4. Go back to main menu")
                input_size = input("Please select your option: ")
                if input_size == "1":
                    lower_upper_both = "lower"
                elif input_size == "2":
                    lower_upper_both = "upper"
                elif input_size == "3":
                    lower_upper_both = "both"
                elif input_size == "4":
                    break
                else:
                    print("You haven't chosen one of the following options")
                    
        elif choice == "3":
            while True:
                print("What would you like to change about punctuation?")
                print(f"1. Toggle punctuation on/off (current {punctuation})")
                print(f"2. Add/Remove excluded character(s) (current: {characters_to_exclude})")
                print("3. Go back to main menu")
                punc_choice = input("Please select your option: ")

                if punc_choice == "1":
                    if punctuation:
                        punctuation = False
                    punctuation = True

                elif punc_choice == "2":
                    while True:
                        print(f"Current characters being excluded: {characters_to_exclude}")
                        print("1. Add characters to exclusion")
                        print("2. Remove characters from exclusion")
                        print("3. Go back")
                        excl_choice = input("Please select your option: ")

                        if excl_choice == "1":
                            print(f"Current characters being excluded: {characters_to_exclude}")
                            exclude_input = input("Type which characters should be excluded (don't worry about spacing): ")
                            for character in exclude_input:
                                characters_to_exclude.append(exclude_input)
                            
                        elif excl_choice == "2":
                            print(f"Current characters being excluded: {characters_to_exclude}")
                            excl_rem_input = input("Type which character to remove from the list (don't worry about spacing): ")
                                for character in excl_rem_input:
                                    characters_to_exclude.remove(excl_rem_input)                                                                        

                        elif excl_choice == "3":
                            break
                        else:
                            print("You haven't chosen one of the following options")

                elif punc_choice == "3":
                    break
                else:
                    print("You haven't chosen one of the following options")

        elif choice == "4":
            generate_password()
            break
        
        elif choice == "5":
            break
        else:
            print("You haven't chosen one of the following options")


        

