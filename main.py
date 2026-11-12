import admin
import regular_user
import staff
from query_service import get_all_users, get_user_by_username


def display_test_accounts():
    print("\nTest Accounts")
    print(f"{'Username':<22} {'Password':<12} Role / access")
    print("-" * 60)
    for user in get_all_users():
        access = user.role
        if user.role == "staff":
            staff_roles = []
            if any(10 <= code < 20 for code in user.staff_codes):
                staff_roles.append("Security")
            if any(20 <= code < 30 for code in user.staff_codes):
                staff_roles.append("Cleaning")
            if any(30 <= code < 40 for code in user.staff_codes):
                staff_roles.append("Equipment Manager")
            access = ", ".join(staff_roles) or "Staff"
        print(f"{user.username:<22} {user.password:<12} {access}")
    print()


def run():
    print("Welcome")
    while True:
        username = input("Username (or 0 to exit): ").strip()
        if username == "0":
            print("Exiting program.")
            return
        if username == "-1":
            display_test_accounts()
            continue

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
