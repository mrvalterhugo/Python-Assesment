import csv

file = open('new_file.txt', 'r')
csv_reader = csv.reader(file, delimiter='\t')
for line in csv_reader:
    ID = line[0]
    print(line[6])
    #if ID != '12':
     #   print(line)
#file2 = open('data.txt', 'r')
#reader = csv.DictReader(file2, delimiter='\t')
#for line in reader:
 #   print(line['ID'])