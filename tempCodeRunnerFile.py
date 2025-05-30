n = int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or row == col - n//2 or row == n - col - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
