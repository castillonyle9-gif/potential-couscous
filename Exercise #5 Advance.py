days = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

month = int(input("Enter a month number (1-12): "))

if month == 2:
    leap = input("Is it a leap year? (yes/no): ").lower()
    if leap == "yes":
        print("Days: 29")
    else:
        print("Days: 28")
elif month in days:
    print("Days:", days[month])
else:
    print("Invalid month.")