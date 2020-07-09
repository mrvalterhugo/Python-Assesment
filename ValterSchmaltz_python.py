import shutil
import csv
import os
from datetime import date

data_file = "python_assessment.txt"

#### This function reads and prints the data inside the file #####
def list_users():
    with open(data_file) as file:
        print(file.read())
    input("Press any key to go back....")

#### This function will add data into the file ####
def add_user():
    global data_file
    while True:
        #### This will check and create the next ID ####
        with open(data_file, 'r') as file:
            file_lines = csv.reader(file, delimiter='\t')
            listing = list(file_lines)
            line_id = listing[-1]
            ID = str(int(line_id[0]) + 1)
        #### This will ask the user to enter the data, also go back to main menu at anytime ####
        name = str(input("Enter the first name of the new user: "))
        surname = str(input("Enter the surname of the new user: "))
        address = str(input("Enter the house NUMBER and the STREET name: "))
        city = str(input("Enter the CITY name: "))
        code = str(input("Enter the POST CODE: "))
        pnumber = str(input("Enter the PHONE number: "))
        data = [ID, name, surname, address, city, code, pnumber]
        print(data)
        check = input('Is the above correct? (Y/N) or "Q" to go back to the main menu\n>>>>')
        #### This will insert the data into the file ####
        if check == "y" or check == "Y":
            write_line = open(data_file, 'a')
            for word in data:
                write_line.write(word)
                write_line.write('\t')
            write_line.write('\n')
            write_line.close()
            print("The user", name, "has been added succesfully!")
            check2 = input('Type any key to add another user or "Q" to exit...')
            if check2 == "Q" or check2 == "q":
                return
        elif check == "Q" or check == "q":
            return
        else:
            print("User has not been saved, press ENTER to try again.")
            input(">>>>")

#### This will list the users and remove users by ID ####
def remove_user():
    global data_file
    while True:
        #### List user database
        with open(data_file) as file:
            print(file.read())
        #### This will ask the user to type an ID to be removed or quit to main menu
        while True:
            print('\nChoose an user ID to remove or type "Q" to go back to the main menu\n')
            UID = input(">>>>")
            if UID == "Q" or UID == "q": return
            elif not UID.isdigit():
                print('Please try again and type a valid number')
                return
            else: break
        UID = int(UID)
        with open(data_file, 'r') as file1:
            file_read = csv.reader(file1, delimiter='\t')
            file_write = open('datanew.txt', 'w')
            for l in file_read:
                if UID != int(l[0]):
                    for word in l:
                        file_write.write(word)
                        file_write.write('\t')
                    file_write.write('\n')
            file_write.close()
        shutil.copy("datanew.txt", data_file)
        print("User ID", UID, "has been removed!\n")
        check = input('Press any key to start again or "Q" to quit...')
        if check == "Q" or check == "q": return

#### This will search by a keyword ####
def user_info():
    global data_file
    while True:
        ##### Menu to select which field the user wants to search
        while True:
            print('Please choose an field to search by:\n',
                  "1 - By ID\n",
                  "2 - By Name\n",
                  "3 - By Surname\n",
                  "4 - By Address\n",
                  "5 - By City\n",
                  "6 - By Post Code\n",
                  "7 - By Phone\n",
                  "8 - Go Back to Main Menu\n")
            choice = input(">>>>")
            if choice == "8": return
            elif choice == "1":
                key = 0
                break
            elif choice == "2":
                key = 1
                break
            elif choice == "3":
                key = 2
                break
            elif choice == "4":
                key = 3
                break
            elif choice == "5":
                key = 4
                break
            elif choice == "6":
                key = 5
                break
            elif choice == "7":
                key = 6
                break
            elif not choice.isdigit():
                input("This is not a valid option. Press any key to try again!")
            else:
                input("This is not a valid option. Press any key to try again!")
        #### Ask the user the pattern to search for
        print("Please type the information you are looking for\n")
        pattern = input(">>>>")
        file1 = open(data_file, 'r')
        file_read = csv.reader(file1, delimiter='\t')
        for l in file_read:
            if pattern.lower() in l[key].lower():
                print(l)
        check = input('Press any key to start again or "Q" to quit...')
        if check == "Q" or check == "q": return
        file1.close()

#### This will update user info ####
def update_info():
    global data_file
    while True:
        ##### Menu to select which field the user wants to modify
        while True:
            print('Please choose an field to modify:\n',
                    "1 - Name\n",
                    "2 - Surname\n",
                    "3 - Address\n",
                    "4 - City\n",
                    "5 - Post Code\n",
                    "6 - Phone\n",
                    "7 - Go Back to Main Menu\n")
            field = input(">>>>")
            if field == "7": return
            elif field == "1": break
            elif field == "2": break
            elif field == "3": break
            elif field == "4": break
            elif field == "5": break
            elif field == "6": break
            elif not field.isdigit(): input("This is not a valid option. Press any key to try again!")
            else: input("This is not a valid option. Press any key to try again!")
        field = int(field)
        #### This will list the file, so the user can select the ID to be updated
        while True:
            with open(data_file) as file:
                print(file.read())
            print("Choose an user ID to modify:")
            UID = input(">>>>")
            if not UID.isdigit():
                input("This is not a valid ID. Press any key to try again!")
            else:
                break
        #### User enters the value to replace the old one
        value = input("Please type the new value >>>> ")
        UID = int(UID)
        with open(data_file, 'r') as file1:
            file_read = csv.reader(file1, delimiter='\t')
            file_write = open('datanew.txt', 'w')
            for l in file_read:
                if UID == int(l[0]):
                    l[field] = value
                for word in l:
                    file_write.write(word)
                    file_write.write('\t')
                file_write.write('\n')
            file_write.close()
        shutil.copy("datanew.txt", data_file)
        check = input('User info has been updated! Press any key to start again or "Q" to quit...')
        if check == "Q" or check == "q": return

#### This will backup the data file ####
def backup():
    global data_file
    #### The new file will have the day and time on its name
    now = str(date.today())
    backup_name = "databk" + now + ".txt"
    shutil.copy(data_file, backup_name)
    print("Backup saved to", backup_name, "successfully")
    input("Press any key to go back to the main menu....")

#### Main Menu ####
while True:
    print("=======Main Menu========\n",
    "1 - List Users Data Base\n",
    "2 - Add a New User\n",
    "3 - Remove a User\n",
    "4 - Search By\n",
    "5 - Update User Information\n",
    "6 - Backup Data Base\n",
    "7 - Exit\n",
    "=========================\n")
    option = input(">>>>")
    if option == "1": list_users()
    elif option == "2": add_user()
    elif option == "3": remove_user()
    elif option == "4": user_info()
    elif option == "5": update_info()
    elif option == "6": backup()
    elif option == "7": exit()
    elif not option.isdigit(): input('Please try again and type a valid number\n')
    else: input("This is not a valid option. Press any key to try again!")
