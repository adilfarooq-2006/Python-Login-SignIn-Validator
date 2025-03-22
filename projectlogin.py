import string
import random

def login():
    print("\nICT PROJECT\n")
    print("LOGIN\n")

    user_data = {}  
    
    user_input = input("Press 1 to signup and 2 to login: ").strip()

    if user_input == '1':  # Signup Process
        user_name = input("Enter your username: ").strip()
        
        # Validate Email
        while True:
            email = input("Enter your email: ").strip()
            valid_domains = ["@gmail.com", "@outlook.com", "@hotmail.com", ".com"]
            if any(domain in email for domain in valid_domains):
                break
            else:
                print("Invalid email format. Please enter a valid email address (e.g., abc@gmail.com).")

        # Password Generator Function
        def pass_gen():
            pass_help = input("Do you want help in setting your password?\nPress 1 for yes and 2 for no: ").strip()

            if pass_help == '1':  # Password Generation Help
                include_name = input("Do you want to include your name in the final password? (yes/no): ").strip().lower() == 'yes'
                include_year = input("Do you want to include your birth year in the final password? (yes/no): ").strip().lower() == 'yes'

                year = ""
                if include_year:
                    year = input("Enter the year you were born: ").strip()

                while True:
                    try:
                        pass_len = int(input("What should be your password length?: "))
                        if pass_len < 8:
                            print("Password length should be at least 8 characters.")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid number for password length.")

                letters = string.ascii_letters
                digits = string.digits
                special = "!@$"
                pool = letters + digits + special

                base_pass = ""
                if include_name:
                    base_pass += user_name
                if include_year:
                    base_pass += year

                transformed_pass = ""
                for char in base_pass:
                    if char.lower() == 'a':
                        transformed_pass += random.choice(["a", "A", "@"])
                    elif char.lower() == 's':
                        transformed_pass += random.choice(["s", "S", "$"])
                    elif char.lower() == 'i':
                        transformed_pass += random.choice(["i", "I", "!"])
                    else:
                        transformed_pass += random.choice([char.lower(), char.upper()])

                while len(transformed_pass) < pass_len:
                    transformed_pass += random.choice(pool)

                final_pass = "".join(random.sample(transformed_pass, len(transformed_pass)))
                print("\nThis is your final password: ", final_pass)

                pass_set = input("Do you want to set this password as your main password? Press 1 for yes, 2 for no: ").strip()
                
                if pass_set == '1':
                    return final_pass
                elif pass_set == '2':
                    print("It means you want to set the password on your own.")
                else:
                    print("Wrong input")

        # Password Validation
        def is_valid_password(password):
            return (len(password) >= 8 and
                any(char.isupper() for char in password) and
                any(char.islower() for char in password) and
                any(char.isdigit() for char in password) and
                any(char in string.punctuation for char in password))            

        
        def password_input_flow():
            password = pass_gen() #Password set
            if not password:  
                while True:
                    password = input("Enter your password: ").strip()
                    if not is_valid_password(password):  # Validate password
                        print("Password must be at least 8 characters long, and must include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
                        continue  
                    confirm = input("Retype your password to confirm: ").strip()
                    if password != confirm:
                        print("Passwords do not match! Try signing up again.")
                        continue  
                    break  
            return password

        # Set Password
        password = password_input_flow()

        # Store Data in a File
        with open("Data.txt", "a") as f:
            f.write(f"{user_name}|{email}|{password}\n")
        
        print("\nYour data has been successfully saved.")
        print("\nSignup successful! You are now logged in.\nWELCOME!")
        print("\nDEVELOPED BY MUHAMMAD ADIL FAROOQ (FA24-BSE-045)")
        print("DEVELOPED BY HAFIZ ABDURREHMAN (FA24-BSE-022)")

    elif user_input == '2':  # Login Process
        login_name = input("Enter your username or email: ").strip()
        login_pass = input("Enter your password: ").strip()

        try:
            with open("Data.txt", "r") as f:
                users = f.readlines()

            for user in users:
                username, email, password = user.strip().split('|')
                if (login_name == username or login_name == email) and login_pass == password:
                    print("\nYou are logged in.\nWELCOME!")
                    print("\nDEVELOPED BY MUHAMMAD ADIL FAROOQ (FA24-BSE-045)")
                    print("DEVELOPED BY HAFIZ ABDURREHMAN (FA24-BSE-022)")
                    return
            print("Invalid username/email or password. Please try again.")
        except FileNotFoundError:
            print("No users found. Please sign up first.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Wrong input.")

# Run the Login Function
login()
