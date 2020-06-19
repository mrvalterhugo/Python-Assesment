def remove_user():
    while True:
        #### List user database
        with open('data.txt') as f: file_r = f.readlines()
        for l1 in file_r: print(l1)
################################
        while True:
            print('\nChoose an user ID to remove or type "QUIT" to go back to the main menu\n')
            UID = input(">>>>")
            if UID == "QUIT" or UID == "quit":
                return
            elif not UID.isdigit():
                print('Please type a valid number or type "QUIT" to go back to the main menu!')
            else:
                break
        file = open('data.txt', 'r')
        #n_l = 0
        #for l in file:
         #  n_l += 1
        #n_l = int(n_l + 1)

        l_n = 0
        UID = int(UID)
        #file_w = open('data.txt', 'w')
        for l in file:
            l_n += 1
            if UID != l_n:
                print(l)
                #file_w.write(l)
        #file_w.close()
        file.close()
        print("User ID", UID, "has been removed!\n")
        input("Press any key to start again.\n>>>>")

remove_user()