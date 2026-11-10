import regular_user
import admin
import staff

print("Welcome")

while True:
    try:
        response = int(input("Choose an option:\n0. Exit\n1. Regular User\n2. Admin\n3. Staff\nEnter a number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if response == 0:
        print("Exiting program.")
        break
    elif response == 1:
        regular_user.when_called()
    elif response == 2:
        admin.when_called()
    elif response == 3:
        staff.when_called()
    else:
        print("Invalid option. Please choose 0, 1, 2, or 3.")