# 1. Create a program that stores fruit prices in a dictionary and lets the user enter a fruit name.
# 2. If the fruit exists in the dictionary, print its price.
# 3. If the fruit doesn’t exist, print "Sorry, this fruit is
# # not available."

fruits = {
    "mango": 50,
    "strawberry": 80,
    "banana": 60,
    "apple": 100,
    "cherry": 120,
    "kiwi": 140
}

fruit = input("Enter a fruit name: ").lower()

if fruit in fruits:
    print(f"The price of {fruit} is {fruits[fruit]}.")
else:
    print("Sorry, this fruit is not available.")