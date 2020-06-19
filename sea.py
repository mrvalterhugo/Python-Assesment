def user_info():
    while True:
        file = open('data.txt', 'r')
        ID = str(input('Please type a keyword to search for or "QUIT" to go back to the main menu:\n>>>>'))
        if ID == "QUIT" or ID == "quit":
            return
        for l in file:
            if ID.lower() in l.lower():
                print(l)
        file.close()
user_info()