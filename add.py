import csv
while True:
    #### This will check and create the next ID ####
    with open('data.txt', 'r') as file:
        file_lines = csv.reader(file, delimiter='\t')
        for n in file_lines:
            ID = int(n[0])
    ID = str(ID + 1)
    #### This will ask the user to enter the data, also go back to main menu at anytime ####
    name = str(input("Enter the first name of the new user: "))
    surname = str(input("Enter the surname of the new user: "))
    address = str(input("Enter the house NUMBER and the STREET name: "))
    city = str(input("Enter the CITY name: "))
    code = str(input("Enter the POST CODE: "))
    pnumber = str(input("Enter the PHONE number: "))
    data = [ID, name, surname, address, city, code, pnumber]
    print(data)
    check = input('Is the above correct? (Y/N) or "QUIT" to go back to the main menu\n>>>>')
    #### This will insert the data into the file ####
    if check == "y" or check == "Y":
        write_line = open('data.txt', 'a')
        for word in data:
            write_line.write(word)
            write_line.write('\t')
        write_line.write('\n')
        write_line.close()
    name = "valter"
    print("The user", name, "has been added succesfully!")
    check2 = input('Type any key to add another user or "QUIT" to exit...')
    if check2 == "QUIT" or check2 == "quit":
        return