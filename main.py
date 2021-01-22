print("WELCOME")
print("here is the star genarator")
user_in = int(input("how many rows of stars do you need\n"))

for star in range(0, user_in + 1):
    for j in range(1, star+1):
        print("*",end= " ")
    print()


