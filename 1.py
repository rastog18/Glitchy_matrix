#DIFFICULT CHALLENGE
y = int(input("Enter the year for which you wish to check:"))
if (y % 4) == 0:
    if (y % 100) == 0:
        if (y % 400) == 0:
            print(f"The year {y} is a leap year.")
        else:
            print(f"The year {y} is not a leap year.")
    else:
        print(f"The year {y} is a leap year")
