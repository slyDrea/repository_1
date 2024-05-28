name_input = input("Name: ")
if len(name_input) < 3:
    print("Name must be at least 3 characters ")
elif len(name_input) > 50:
    print("Name must be at 50 letter maximum ")
else:
    print()

password_input = input("Password: ")
if len(password_input) < 5:
    print("Password is not long enough ")
elif len(password_input) > 50:
    print("Password is too long ")
else:
    print()

confirm_password_input = input("Confirm your password")
if confirm_password_input == password_input:
    print("Signed in, " + name_input)
