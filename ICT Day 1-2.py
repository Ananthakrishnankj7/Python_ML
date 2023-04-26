x = int(input("Enter a number "))
if (x % 2 != 0):
    print("Weird")
elif (x % 2 == 0):
    if x in range(2, 6):
        print("Not Weird")
    elif x in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")
