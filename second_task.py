username = input("Enter your username: ")
password = input("Enter your password: ")

username = username.lower()
username = username.split(" ")
username = "_".join(username)

length = len(password)

print(f"Welcome to the system, {username}!")
print(f"Your password length is: {length} characters.")

password_length = length >= 8
username_check = username == "admin"
password_check = password == "1234"
default_account_check = username_check and password_check

print(f"Is The Password Valid? {password_length}")
print(f"Is The username 'admin'? {username_check}")
print(f"Is The Password Default? {password_check}")
print(f"Is The Account Default? {default_account_check}")

print(f"Welcome {username}! Your password length is {length}.")