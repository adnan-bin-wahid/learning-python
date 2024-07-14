master_pass = input("What is the master password: ")

def view():
    pass
    

def add():
    with open("pass_man.txt","a") as f: 
        user_name = input("Enter your user name: ")
        password = input("Enter your password")
        f.write(user_name+"|"+password)



while True:
    command = input("What do you want to do?(view/add) for quit press q: ").lower()
    
    if command == "q":
        break
    elif command == "view":
        view()
    elif command == "add":
        add()  
    else: 
        print("Invalid command ")