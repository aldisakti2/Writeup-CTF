import string
import secrets

accounts = []
sessions = {}

def register(username, password, role):
    try:
        for account in accounts:
            if username == account[0]:
                return "Username is used, try again"
        
        username = username.strip()

        if username == "":
            return "Username can't blank"

        session = secrets.token_hex(15)
        accounts.append((username, password, role))
        sessions[session] = username

        return f"Your session key: {session}"
    except:
        return "Something wrong, please try again"

def login(choice, username = "", password = "", session = ""):
    if choice == 1:
        for account in accounts:
            if account[0] == username and account[1] == password:
                return account[0], account[2]
    elif choice == 2:
        for account in accounts:
            if account[0] == sessions[session]:
                return account[0], account[2]
    
    return "", ""


if __name__ == "__main__":
    name, role = "", ""
    register("cf-min", secrets.token_hex(15), "admin")

    while True:

        if role == "":
            print("Main Menu")
            print("1. Login")
            print("2. Register")

            c = input("Choice: ")

            if c == "1":
                print("1. Login with username and password")
                print("2. Login with sessions key")

                s = input("Select: ")

                if s == "1":
                    name, role = login(1, username=input("Username: "), password=input("Password: "))
                elif s == "2":
                    name, role = login(2, session=input("Session key: "))
                    
                else:
                    print("Wrong choice, back to main menu")
                
            elif c == "2":
                result = register(input("Username: "), input("Password: "), "user")
                print(result)
            else:
                print("Wrong choice, exiting")
                break
        
        elif role == "user":
            print("Feature doesn't implement yet")
            print("Return to main menu")
            role = ""
            name = ""
        
        elif role == "admin":
            print("Administator Menu")
            print("1. Debug")
            print("2. Back to Main Menu")

            c = input("Choice: ")

            if c == "1":
                try:
                    inp = input("Input command: ")

                    if len(inp) > 15:
                        raise Exception("Your command is too long, please try again")
                    else:
                        for i in inp:
                            if i not in string.ascii_lowercase and i not in string.ascii_uppercase and i not in ["(", ")"]:
                                raise Exception("Only alphabet allowed for calling functions")
                        eval(inp)
                except:
                    print("Something is wrong, exiting")
                    break
            
            elif c == "2":
                role = ""
                name = ""
            
            else:
                print("Wrong choice, exiting")
                break

    print("Thanks for visiting our service")