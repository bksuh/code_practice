a = int(input())
b = int(input())

diff = b-a

if 1 <= diff <= 20:
    print("You are speeding and your fine is $100.")

elif 21 <= diff <= 30:
    print("You are speeding and your fine is $270.")

elif 31 <= diff:
    print("You are speeding and your fine is $500.")

else:
    print("Congratulations, you are within the speed limit!")