correct_password = "12345"
attempts = 5

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access Granted.")
        break

    attempts -= 1
    print("Wrong. Attempts left:", attempts)

if attempts == 0:
    print("Maximum attempts reached. Authorities alerted.")
