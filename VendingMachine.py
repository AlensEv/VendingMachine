# display greeting
import sys

print("Welcome to Alens's Vending Machine\n")

print("Here are our products")
print("Item   Price Code")
print("Chips   $.50  1")
print("Granola   $2  2")
print("TrailMix  $1  3")
print("Water     $2  4")

# Step2 create initialize the variable s
ChipsPrice = .50
GranolaPrice = 2
TrailMixPrice = 2
WaterPrice = 2

# Prompt the user to choose their item by typing the code
print("Please enter item code to continue")
# Step-4: Use the int(input()) function and save the response in a variable
# called userCode.
Code = int(input())
if Code == 1:
    print("The price of Chips are $.50 ")

elif Code == 2:
    print("The price of Granola is $2 ")
elif Code == 2:
    print("The price of TrailMix is $1 ")
elif Code == 4:
    print("The price of Water is $2 ")
else:
    Error = True
    print("Error: Invalid Entry Try again ")
    sys.exit(0)


print("To confirm selection Press 1 for yes or press 2 for no")

UserEntry = int(input())


if UserEntry == 1:
    print("Enjoy your purchase, Goodbye")

elif UserEntry == 2:
    print("Thank you for Viewing Alens's Vending Machine, Goodbye")












