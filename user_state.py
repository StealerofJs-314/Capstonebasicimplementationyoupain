from user import User


users = [
    User(1001, "alex", "password", role="regular_user", name="Alex"),
    User(1003, "sam", "password", role="regular_user", name="Sam"),
    User(1004, "taylor", "password", role="regular_user", name="Taylor"),
    User(1005, "morgan", "password", role="regular_user", name="Morgan"),
    User(1, "regular_staff_1", "password", [1], "staff"),
    User(2, "regular_staff_2", "password", [2, 21], "staff"),
    User(4, "regular_staff_4", "password", [4], "staff"),
    User(11, "security_staff_11", "password", [11], "staff"),
    User(22, "cleaning_staff_22", "password", [22], "staff"),
    User(31, "security_equipment", "password", [13, 31], "staff"),
    User(9001, "admin1", "password", role="admin"),
    User(9002, "admin2", "password", role="admin"),
]
