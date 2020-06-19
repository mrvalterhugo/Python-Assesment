import csv
import shutil
def update_info():
    while True:
        ##### Menu
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
            elif field == "1":
                key = 1
                break
            elif field == "2":
                key = 2
                break
            elif field == "3":
                key = 3
                break
            elif field == "4":
                key = 4
                break
            elif field == "5":
                key = 5
                break
            elif field == "6":
                key = 6
                break
            elif not field.isdigit():
                input("This is not a valid option. Press any key to try again!")
            else:
                input("This is not a valid option. Press any key to try again!")
        field = int(field)
        while True:
            print("Choose an person ID to modify:")
            data = open("data.txt", 'r')
            for u in data:
                print(u)
            UID = input(">>>>")
            if not UID.isdigit():
                input("This is not a valid ID. Press any key to try again!")
            else: break
        value = input("Please type the new value >>>> ")
        UID = int(UID)
        with open('data.txt', 'r') as file1:
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
        shutil.copy("datanew.txt", "data.txt")
        input("User info has been updated! Press any key to start again...")
update_info()