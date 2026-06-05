import random
import string

passwords = {}

# Load existing passwords
try:
    with open("password.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except FileNotFoundError:
    pass


def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%"
    pwd = "".join(random.choice(chars) for _ in range(8))
    return pwd


while True:
    print("\n----PERSONAL PASSWORD MANAGER----")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        site = input("Enter website: ")
        pwd = input("Enter Password: ")

        passwords[site] = pwd

        with open("password.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

        print("Saved successfully!")

    elif choice == 2:
        if not passwords:
            print("No Data!")
        else:
            for site, pwd in passwords.items():
                print(site, ":", pwd)

    elif choice == 3:
        print("Generated Password:", generate_password())

    elif choice == 4:
        print("Ok Bye...")
        break

    else:
        print("Invalid Input")
