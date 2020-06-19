import csv
def user_info():
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
        elif choice == "1": key = 0
        elif choice == "2": key = 1
        elif choice == "3": key = 2
        elif choice == "4": key = 3
        elif choice == "5": key = 4
        elif choice == "6": key = 5
        elif choice == "7": key = 6
        elif not choice.isdigit(): input('Please try again and type a valid number\n')
        else: input("This is not a valid option. Press any key to try again!")
        print("Please type the informatio you are looking for\n")
        pattern = input(">>>>")
        file1 = open('data.txt', 'r')
        file_read = csv.reader(file1, delimiter='\t')
        for l in file_read:
            if pattern.lower() in l[key].lower():
                print(l)
        print("Press anyhting to try again!")
        input(">>>>")
        file1.close()


user_info()