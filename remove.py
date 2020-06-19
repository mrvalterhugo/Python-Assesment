import csv
import shutil
def remove_user():
    while True:
        #### List user database
        with open('data.txt') as f: file_r = f.readlines()
        for l in file_r: print(l)
################################
        while True:
            print('\nChoose an user ID to remove or type "QUIT" to go back to the main menu\n')
            UID = input(">>>>")
            if UID == "QUIT" or UID == "quit": return
            elif not UID.isdigit():
                print('Please try again and type a valid number')
                return
            else: break
        UID = int(UID)
        file1 = open('data.txt', 'r')
        file_read = csv.reader(file1, delimiter='\t')
        file_write = open('datanew.txt', 'w')
        for l in file_read:
            if UID != int(l[0]):
                for word in l:
                    file_write.write(word)
                    file_write.write('\t')
                file_write.write('\n')
        file_write.close()
        file1.close()
        shutil.copy("datanew.txt", "data.txt")
        print("User ID", UID, "has been removed!\n")
        input("Press any key to start again.\n>>>>")

remove_user()