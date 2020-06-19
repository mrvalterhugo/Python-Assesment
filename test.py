import shutil
'''
file = open('data.txt', 'r+')
UID = int(input(">>>>"))
for l in file:
    n = int(l[0])
    if UID != n:
        print(l)
file.close()

file = open('data.txt', 'r')
print(len(file.readlines()))


file_name = str(input("Please Enter a backup file name: \n")) + ".txt"
shutil.copy("data.txt", file_name)
print("Backup completed successfuly saved to", file_name)


def get_details():
    ID = 1
    while True:
        print('To go back to menu type "QUIT" at any time!')
        name = input("Please enter the FULL name of the new user: ")
        if name == "QUIT":
            return
        address = input("Now, enter the house NUMBER and the STREET name: ")
        if address == "QUIT":
            return
        city = input("Please enter the CITY name: ")
        if city == "QUIT":
            return
        code = input("Please enter the POST CODE: ")
        if code == "QUIT":
            return
        pnumber = input("Please enter the PHONE number: ")
        if pnumber == "QUIT":
            return

        print(ID, name, address, city, code, pnumber)
        check = input("Is the above correct? (Y/N)")
        if check == "y" or check == "Y":
            break
    print("The user", name, " has been added succesfully!")


add data
file2 = open('data.txt', 'a')
file2.write("\n")
file2.writelines([ID, "   ", name, "   ", address, "   ", city, "   ", code, "   ", pnumber])
file2.close()


different way to add data
    file2 = open('data.txt', 'a')
    data = ID, name, address, city, code, pnumber
    file2.write("\n")
    for d in data:
        d = str(d)
        #upper = d.upper()
        file2.write(d)
        file2.write("   ")
    file2.close()
    
    
'''
with open('data.txt') as f: file_r = f.readlines()
for l in file_r: print(l)
print(len(file_r))
file_r.de


#### This is another way of getting the ID
'''
file = open('data.txt', 'r')
file_lines = file.readlines()
file.close()
ID = str(len(file_lines) + 1)
print(ID)

file = open('data.txt', 'r')
n_l = 0
for l in file:
   n_l += 1
d = n_l + 1
print (d)

### Another way of counting lines and printing IDs:
with open('data.txt') as my_file:
   c = sum(1 for _ in my_file) + 5
   print(c)
'''
'''
Old way, but does not work when the number is higher than 10
file1 = open('data.txt', 'r')
for line in file1:
    ID = int(line[0])
    if ID == int(line[0]):
        ID += 1
file1.close()
'''
'''
### Another way of printing line by line:

with open("data.txt", 'r') as f:
    data = f.readlines()
for l in data:
    print(l)

print line by line
file = open('data.txt', 'r')
print(file.readline()[0])


import time

t = time.localtime()
current_time = time.strftime("backup-%D", t)
print(current_time)

### writing data into the file easier
ID = "2"
name = "valter schmaltz"
address = "3 fgdfg"
city = "manchester"
code = "m22"
pnumber = "43534534"
file2 = open('data.txt', 'a')
file2.write("\n")
file2.writelines([ID, "\t", name, "\t", address, "\t", city, "\t", code, "\t", pnumber])
file2.close()


def user_info():

    while True:
        file = open('data.txt', 'r')
        ID = str(input('Please type a keyword to search for or "QUIT" to go back to the main menu:\n>>>>'))
        if ID == "QUIT" or ID == "quit":
            return
        for l in file:
            if ID.lower() in l.lower():
                print (l)
        file.close()
user_info()

'''
## how to read lines with csv metod
import csv
file = open('data.txt', 'r')
    file_read = csv.reader(file, delimiter='\t')
    for l in file: print(l)
    file.close()