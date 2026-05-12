x = int(input("Give me an EVEN integer from 1 to 100: "))

if x < 1:
    print("That is too small, error!!!")
elif x > 100:
    print("That is too big, error!!!")
elif x%2 == 1: # Remainder is 1 not 0
    print("That is ODD not even, error!!!")
else:
    print("Thank you, that is EVEN and from 1 to 100")
