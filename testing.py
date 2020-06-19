import csv
'''
with open('data.txt', 'r') as file_r:
    csv_reader = csv.reader(file_r, delimiter = '\t')

    write_line = open('new_file.txt', 'w')
    for line in csv_reader:
        for word in line:
            write_line.write(word)
            write_line.write('\t')
        write_line.write('\n')
'''
name = str(input("Enter the first name of the new user: "))
surname = str(input("Enter the surname of the new user: "))
address = str(input("Enter the house NUMBER and the STREET name: "))
city = str(input("Enter the CITY name: "))
code = str(input("Enter the POST CODE: "))
pnumber = str(input("Enter the PHONE number: "))
ID = '5'
data = [ID, name, surname, address, city, code, pnumber]

write_line = open('new_file.txt', 'a')
for word in data:
    write_line.write(word)
    write_line.write('\t')
write_line.write('\n')