# 1. Create a list of your 5 favourite fruits and print it.
# 2. Print the first and last elements of the list.
# 3. Change the second item in the list to "Mango".
# 4. Insert: Add "Watermelon" at index 2.
# 5. Check existence: Write a program that asks the user for a
# fruit name and checks if it’s in the list.
# 6. Sort the list alphabetically.

fruits = ["apple", "banana", "cherry", "kiwi", "grapes"]
print("First element:", fruits[0])
print("Last element:", fruits[-1])
fruits[1] = "Mango"
print(fruits)
fruits.insert(2, "Watermelon")
print(fruits)
fruit_to_check = input("Enter a fruit name to check if it's in the list: ")
if fruit_to_check in fruits:
    print(f"{fruit_to_check} is in the list.")
else:
   print(f"{fruit_to_check} is not in the list.")

fruits.sort()
print(fruits)
