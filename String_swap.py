def swapi(x):
    k = " "
    for i in x:
        if i.islower():
            k += i.upper()
        else:
            k += i.lower()
    return k


name = input("Enter a string")
ret = swapi(name)
print(ret)
