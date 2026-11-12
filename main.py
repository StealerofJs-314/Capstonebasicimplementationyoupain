import admin
import regular_user
import staff
from query_service import get_user_by_username


def run():
    print("Welcome")
    while True:
        username = input("Username (or 0 to exit): ").strip()
        if username == "0":
            print("Exiting program.")
            return

        password = input("Password: ")
        user = get_user_by_username(username)
        if user is None or not user.check_password(password):
            print("Invalid username or password.")
            continue

        if user.role == "regular_user":
            regular_user.run_dashboard(user.id, user.name)
        elif user.role == "admin":
            admin.run_dashboard(user.id)
        elif user.role == "staff":
            staff.run_dashboard(user.id, user.staff_codes)
        else:
            print("This account has no assigned role.")


if __name__ == "__main__":
    run()
