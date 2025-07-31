num = int(input("Enter a number: "))
for i in range(1, num + 1):
    for space in range(num - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()
    
