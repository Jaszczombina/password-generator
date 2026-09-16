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

def generate_password():
    global punctuation
    global characters_to_exclude
    global lower_upper_both
    global length
    list_of_characters = []

    if punctuation == True:
        list_of_characters.extend(s.punctuation)
    if lower_upper_both == "lower":
        list_of_characters.extend(s.ascii_lowercase)
    elif lower_upper_both == "upper":
        list_of_characters.extend(s.ascii_uppercase)
    elif lower_upper_both == "both":
        list_of_characters.extend(s.ascii_lowercase)
        list_of_characters.extend(s.ascii_uppercase)
    for index in range(0, len(characters_to_exclude)):
        list_of_characters.remove(characters_to_exclude[index])
    
    r.shuffle(list_of_characters)
    r.shuffle(list_of_characters)
    generated_password = ""
    while len(generated_password) < length:
        generated_password += r.choice(list_of_characters)
    return generated_password



def save_password(password, username, website):
    pass

def show_passwords():
    pass

def remove_password(username, website):
    pass

def change_password(username, website, new_password):
    pass

def change_website(username, website, new_website):
    pass

def change_username(username, website, new_username):
    pass

def remove_all_passwords():
    pass


def main():
    global punctuation
    global characters_to_exclude
    global lower_upper_both
    global length

    print("Welcome to my password generator!")
    print("Choose which setting you would like to change or simply generate the password!")

    while True:
        print(f"1. Set the length of my password (current: {length} characters)")
        print(f"2. Set the characters to be just lowercase/uppercase/both (current: {lower_upper_both})")
        print(f"3. Set characters to exclude and special characters toggle (current: {characters_to_exclude} and special characters: {punctuation})")
        print("4. Generate my password!")
        print("5. List and/or modify my passwords")
        print("6. Remove all passwords")
        print("7. Exit the generator")
        choice = input("Please select your option: ")

        if choice == "1":  # Set the length of the password
            input_length = input("Please type your preferred length of characters: ")
            length = int(input_length)

        elif choice == "2":  # Change to just lowercase/uppercase or both
            while True:
                print("Which setting you'd like to continue with?")
                print("1. Just lowercase characters")
                print("2. JUST UPPERCASE CHARACTERS")
                print("3. Both lowercase and UPPERCASE characters")
                print("4. Go back to main menu")
                input_size = input("Please select your option: ")
                if input_size == "1":   # Set to use lower case only
                    lower_upper_both = "lower"
                    break
                elif input_size == "2":  # Set to use upper case only
                    lower_upper_both = "upper"
                    break
                elif input_size == "3":  # Set to use both lower and upper case
                    lower_upper_both = "both"
                    break
                elif input_size == "4":   # Go back to main menu
                    break
                else:    # Non-existing choice
                    print("You haven't chosen one of the following options")
                    
        elif choice == "3":   # Toggle special characters and exclude characters
            while True:
                print("What would you like to change about characters?")
                print(f"1. Toggle special characters on/off (current {punctuation})")
                print(f"2. Add/Remove excluded character(s) (current: {characters_to_exclude})")
                print("3. Go back to main menu")
                punc_choice = input("Please select your option: ")

                if punc_choice == "1":    # Toggle special characters
                    if punctuation:
                        punctuation = False
                    else:
                        punctuation = True

                elif punc_choice == "2":     # Add/Remove characters to exclude
                    while True:
                        print(f"Current characters being excluded: {characters_to_exclude}")
                        print("1. Add characters to exclusion")
                        print("2. Remove characters from exclusion")
                        print("3. Go back")
                        excl_choice = input("Please select your option: ")

                        if excl_choice == "1":    # Add characters to exclude
                            print(f"Current characters being excluded: {characters_to_exclude}")
                            exclude_input = input("Type which characters should be excluded (don't worry about spacing): ")
                            for index in range(0, len(exclude_input)):
                                characters_to_exclude.append(exclude_input[index])
                            
                        elif excl_choice == "2":    # Remove characters to exclude
                            print(f"Current characters being excluded: {characters_to_exclude}")
                            excl_rem_input = input("Type which character to remove from the list (don't worry about spacing): ")
                            for index in range(0, len(excl_rem_input)):
                                if excl_rem_input[index] not in characters_to_exclude:
                                    print(f"{excl_rem_input[index]} was not excluded")
                                    continue
                                characters_to_exclude.remove(excl_rem_input[index])
                                                                                                        
                        elif excl_choice == "3":    # Go back to menu number 3 (change (special) characters)
                            break
                        else:    # Non-existing choice
                            print("You haven't chosen one of the following options")

                elif punc_choice == "3":    # Go back to main menu
                    break
                else:    # Non-existing choice
                    print("You haven't chosen one of the following options")

        elif choice == "4":  # Generate a password
            password = generate_password()   
            print(f"This is your generated password: {password}")
            while True:
                print("What do you want to do?")
                print("1. Save password")
                print("2. Generate a new password")
                print("3. Go back")
                save_choice = input("Please select your option: ")

                if save_choice == "1":     # Save password
                    username = input("What is the username/email you use this password with: ")
                    website = input("What is the website/app this password will be used for: ")
                    save_password(password, username, website)

                elif save_choice == "2":     # Generate new password
                    password = generate_password()
                    print(f"This is your generated password: {password}")

                elif save_choice == "3":    # Go back to main menu
                    break
                else:    # Non-existing choice
                    print("You haven't chosen one of the following options")
            
        
        elif choice == "5":   # List and modify passwords
            print("These are your passwords: ")
            show_passwords()
            while True:
                print("What do you want to do?")                  # Maybe an option to go from here to generate passwords
                print("1. Remove a password")
                print("2. Change one of the passwords")
                print("3. Change one of the usernames")
                print("4. Change one of the websites/apps")
                print("5. Go back to main menu")
                list_choice = input("Please select your option: ")
                if list_choice == "1":    # Remove a specific password
                    rem_username = input("What is the username associated with the password: ")
                    rem_website = input("What is the website/app associated with the password: ")
                    remove_password(rem_username, rem_website)

                elif list_choice == "2":    # Change a specific password
                    change_pass_username = input("What is the username associated with the password: ")
                    change_pass_website = input("What is the website/app associated with the password: ")
                    change_pass_new = input("What is the new password: ")
                    change_password(change_pass_username, change_pass_website, change_pass_new)

                elif list_choice == "3":    # Change a specific username
                    change_user_username = input("What is the username associated with the password: ")
                    change_user_website = input("What is the website/app associated with the password: ")
                    change_user_new = input("What is the new username: ")
                    change_username(change_user_username, change_user_website, change_user_new)
                    
                elif list_choice == "4":    # Change a specific website/app
                    change_web_username = input("What is the username associated with the password: ")
                    change_web_website = input("What is the website/app associated with the password: ")
                    change_web_new = input("What is the new website/app: ")
                    change_website(change_web_username, change_web_website, change_web_new)

                elif list_choice == "5":     # Go back to main menu
                    break
                else:    # Non-existing choice
                    print("You haven't chosen one of the following options")
             
        elif choice == "6":     # Remove all passwords
            print("Be aware, this option is irreversible, do you wish to continue?")
            rem_all_choice = input("Please type yes or no: ")

            if rem_all_choice.lower() == "yes":
                remove_all_passwords()
            else:
                continue
        elif choice == "7":  # Exit the generator
            break
        else:   # Non-existing choice
            print("You haven't chosen one of the following options")

main()

