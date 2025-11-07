correct_password = "12345"

password = input("Enter password: ")

while password != correct_password:
    password = input("Wrong. Try again: ")

print("Access Granted.")
