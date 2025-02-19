email = input("Enter your Email: ")  # Example: g@g.in , dinesh0707@gmail.com

k, j, d = 0, 0, 0  # Flags for space, uppercase, and invalid characters

if len(email) >= 6:
    if email[0].isalpha():  # First character should be a letter
        if "@" in email and email.count("@") == 1:  # '@' should be present only once
            if email[-4] == "." or email[-3] == ".":  # Email should end with a proper domain
                for i in email:
                    if i.isspace():  
                        k = 1  # Space found
                    elif i.isalpha():
                        if i.isupper():
                            j = 1  # Uppercase letter found
                    elif i.isdigit():
                        continue
                    elif i in "_@.":
                        continue
                    else:
                        d = 1  # Invalid character found
                
                # If any error flag is raised, it's an invalid email
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email 5")
                else:
                    print("Valid Email ✅")
            else:
                print("Wrong Email 4")  # Invalid domain
        else:
            print("Wrong Email 3")  # Invalid '@' usage
    else:
        print("Wrong Email 2")  # First character is not a letter
else:
    print("Wrong Email 1")  # Length is too short
