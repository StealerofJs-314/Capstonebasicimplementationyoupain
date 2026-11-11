import regular_user
import admin
import staff

class User:
    def __init__(
        self, id=-1, username="", password="", staff_id=None,
        role="regular_user", name="",
    ):
        self.id = id
        self.username = username
        self.password = password
        self.staff_id = staff_id if staff_id is not None else []
        self.role = role
        self.name = name or username

    def check_password(self, password):
        if password == self.password:
            return self.id
        return -1


users = [
    User(1001, "alex", "password", role="regular_user", name="Alex"),
    User(1003, "sam", "password", role="regular_user", name="Sam"),
    User(1004, "taylor", "password", role="regular_user", name="Taylor"),
    User(1005, "morgan", "password", role="regular_user", name="Morgan"),
    User(1, "regular_staff_1", "password", [1], "staff"),
    User(2, "regular_staff_2", "password", [2,21], "staff"),
    User(4, "regular_staff_4", "password", [4], "staff"),
    User(11, "security_staff_11", "password", [11], "staff"),
    User(22, "cleaning_staff_22", "password", [22], "staff"),
    User(9001, "admin1", "password", role="admin"),
    User(9002, "admin2", "password", role="admin"),
]


print("Welcome")

while True:
    username = input("Username (or 0 to exit): ").strip()
    if username == "0":
        print("Exiting program.")
        break

    password = input("Password: ")
    user = next((user for user in users if user.username == username), None)
    if user is None or user.check_password(password) == -1:
        print("Invalid username or password.")
        continue

    if user.role == "regular_user":
        regular_user.when_called(user.id, user.name)
    elif user.role == "admin":
        admin.when_called(user.id)
    elif user.role == "staff":
        staff.when_called(user.id, user.staff_id)