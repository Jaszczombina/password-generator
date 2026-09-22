import random as r
import string as s
import json

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


def save_data(filepath, pass_data):
    data = {
        'pass_data': pass_data
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    
def load_password_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data['pass_data']
    except (FileNotFoundError, json.JSONDecodeError):    # If there's no file, set the data as an empty list
        return []
    

def save_password(pass_data, website, username, password):
    pass_data.append({"website": website, "username": username, "password": password})
    print(f"Added password and username '{username}' for website/app '{website}'")

def show_passwords(pass_data):
    if pass_data == []:
        print("You have 0 passwords saved")
        return
    print("Passwords saved: \n")
    for p in pass_data:
        print(f"- Website/app: {p['website']}, Username: {p['username']}, Password: {p['password']}")
    

def remove_password(pass_data, website, username):
    for i, password in enumerate(pass_data):
        if password['website'] == website and password['username'] == username:
            removed_pass = pass_data.pop(i)
            print(f"Removed password for website/app '{website}' and username '{username}'")
            return
    else:
        print("\nWebsite and/or username not found, please check the list of passwords")

def change_password(pass_data, website, username, new_password):
    for i, password in enumerate(pass_data):
        if password['website'] == website and password['username'] == username:
            password['password'] = new_password
            return
        else:
            print(f"\nWebsite and/or username not found, please check the list of passwords")

def change_website(pass_data, website, username, new_website):
    for i, password in enumerate(pass_data):
        if password['website'] == website and password['username'] == username:
            password['website'] = new_website
            return
        else:
            print(f"\nWebsite and/or username not found, please check the list of passwords")

def change_username(pass_data, website, username, new_username):
    for i, password in enumerate(pass_data):
        if password['website'] == website and password['username'] == username:
            password['username'] = new_username
            return
        else:
            print(f"\nWebsite and/or username not found, please check the list of passwords")

def remove_all_passwords(pass_data):
    pass_data.clear()
    print("\nYour password list has been cleared")


def main():
    global punctuation
    global characters_to_exclude
    global lower_upper_both
    global length

    print("Welcome to my password generator!")
    print("\nChoose which setting you would like to change or simply generate the password!") 
    filepath = 'password_data.json'                   # Set the filepath for file with passwords
    pass_data = load_password_data(filepath)           # pass_data contains website, username and password values

    while True:
        print(f"\n1. Set the length of my password (current: {length} characters)")
        print(f"2. Set the characters to be just lowercase/uppercase/both (current: {lower_upper_both})")
        print(f"3. Set characters to exclude and special characters toggle (current: {characters_to_exclude} and special characters: {punctuation})")
        print("4. Generate my password!")
        print("5. List my passwords")
        print("6. Modify my passwords")
        print("7. Exit the generator")
        choice = input("\nPlease select your option: ")

        if choice == "1":  # Set the length of the password
            input_length = input("Please type your preferred length of characters: ")
            length = int(input_length)

        elif choice == "2":  # Change to just lowercase/uppercase or both
            while True:
                print("\nWhich setting you'd like to continue with?")
                print("\n1. Just lowercase characters")
                print("2. JUST UPPERCASE CHARACTERS")
                print("3. Both lowercase and UPPERCASE characters")
                print("4. Go back to main menu")
                input_size = input("\nPlease select your option: ")
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
                print("\nWhat would you like to change about characters?")
                print(f"\n1. Toggle special characters True/False (current {punctuation})")
                print(f"2. Add/Remove excluded character(s) (current: {characters_to_exclude})")
                print("3. Go back to main menu")
                punc_choice = input("\nPlease select your option: ")

                if punc_choice == "1":    # Toggle special characters
                    if punctuation:
                        punctuation = False
                    else:
                        punctuation = True

                elif punc_choice == "2":     # Add/Remove characters to exclude
                    while True:
                        print(f"\nCurrent characters being excluded: {characters_to_exclude}")
                        print("\n1. Add characters to exclusion")
                        print("2. Remove characters from exclusion")
                        print("3. Go back")
                        excl_choice = input("\nPlease select your option: ")

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
                                                                                                        
                        elif excl_choice == "3":    # Go back to previous menu
                            break
                        else:    # Non-existing choice
                            print("You haven't chosen one of the following options")

                elif punc_choice == "3":    # Go back to main menu
                    break
                else:    # Non-existing choice
                    print("You haven't chosen one of the following options")

        elif choice == "4":  # Generate a password
            password = generate_password()   
            print(f"\nThis is your generated password: {password}")
            while True:
                print("\nWhat do you want to do?")
                print("\n1. Save password")
                print("2. Generate a new password")
                print("3. Go back")
                save_choice = input("\nPlease select your option: ")

                if save_choice == "1":     # Save password
                    website = input("What is the website/app this password will be used for: ")
                    username = input("What is the username/email you use this password with: ")
                    save_password(pass_data, website, username, password)
                    break

                elif save_choice == "2":     # Generate a new password
                    password = generate_password()
                    print(f"This is your generated password: {password}")

                elif save_choice == "3":    # Go back to main menu
                    break
                else:    # Non-existing choice
                    print("You haven't chosen one of the following options")
            
        elif choice == "5":   # Lists all the passwords
            print("\nThese are your passwords: ")
            show_passwords(pass_data)

        elif choice == "6":   # Modify passwords
            if pass_data == []:          #check this
                print("Password list is empty, going back to main menu")
                continue
            while True:
                print("\nWhat do you want to do?")               
                print("1. Remove a password")
                print("2. Change one of the passwords")
                print("3. Change one of the usernames")
                print("4. Change one of the websites/apps")
                print("5. Remove ALL passwords")
                print("6. Go back to main menu")
                list_choice = input("\nPlease select your option: ")
                if list_choice == "1":                                   # Remove a specific password
                    rem_website = input("What is the website/app associated with the password: ")
                    rem_username = input("What is the username associated with the password: ")
                    remove_password(pass_data, rem_website, rem_username)

                elif list_choice == "2":    # Change a specific password
                    change_pass_website = input("What is the website/app associated with the password: ")
                    change_pass_username = input("What is the username associated with the password: ")
                    for i, password in enumerate(pass_data):
                        if password['website'] != change_pass_website or password['username'] != change_pass_username:
                            print("\nCannot find a password with this website/app or username. Please check the list to make sure the password exists")
                            break                                    
                        else:
                            while True:
                                print("\nWhat would you like to do?")
                                print("1. Generate a new password")
                                print("2. I have a new password already")
                                print("3. Go back")
                                new_pass_choice = input("Please select your option: ")
                                if new_pass_choice == "1":      # Generate a password to have a password for a change
                                    new_pass_generated = generate_password()
                                    while True:
                                        print(f"\nThis is your new generated password: {new_pass_generated}")
                                        print("\nWhat would you like to do?")
                                        print("1. Change password using the one generated")
                                        print("2. Generate a new password")
                                        save_pass_choice = input("Please select your option: ")
                                        if save_pass_choice == "1":      # Save the newly generated password with the values above
                                            change_password(pass_data, change_pass_website, change_pass_username, new_pass_generated)
                                            break

                                        elif save_pass_choice == "2":      # Generate a new password
                                            new_pass_generated = generate_password()
                                        else:    # Non-existing choice
                                            print("You haven't chosen one of the following options")
                                    break   # Go back 2 menus as we changed the password already
                            

                                elif new_pass_choice == "2":       # User has a new password ready
                                    change_pass_new = input("What is the new password: ")                                      
                                    change_password(pass_data, change_pass_website, change_pass_username, change_pass_new)
                                    break
                                elif new_pass_choice == "3":    # Go back
                                    break
                                else:    # Non-existing choice
                                    print("You haven't chosen one of the following options")

                elif list_choice == "3":    # Change a specific username
                    change_user_website = input("What is the website/app associated with the password: ")
                    change_user_username = input("What is the username associated with the password: ")
                    change_user_new = input("What is the new username: ")
                    change_username(pass_data, change_user_website, change_user_username, change_user_new)
                    
                elif list_choice == "4":    # Change a specific website/app
                    change_web_website = input("What is the website/app associated with the password: ")
                    change_web_username = input("What is the username associated with the password: ")
                    change_web_new = input("What is the new website/app: ")
                    change_website(pass_data, change_web_website, change_web_username, change_web_new)
                
                elif list_choice == "5":  # Remove/Clear the list with all passwords
                    print("Be aware, this option is irreversible, do you wish to continue?")
                    rem_all_choice = input("\nPlease type yes or no: ")

                    if rem_all_choice.lower() == "yes":
                        remove_all_passwords(pass_data)
                        break
                    else:
                        continue

                elif list_choice == "6":     # Go back to main menu
                    break
                else:    # Non-existing choice
                    print("You haven't chosen one of the following options")
             
        elif choice == "7":  # Save the data in the file and exit the generator
            save_data(filepath, pass_data)
            print("\nExiting the generator")
            break
        else:   # Non-existing choice
            print("You haven't chosen one of the following options")

if __name__ == "__main__":
    main()

