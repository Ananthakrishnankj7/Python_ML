x = int(input("Enter the year to be checked "))
if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print("It is leap year")
        else:
            print("It is not leap year")
    else:
        print("It is leap year")
else:
    print("It is not leap year")
