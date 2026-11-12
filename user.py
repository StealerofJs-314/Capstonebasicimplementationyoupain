class User:
    def __init__(
        self,
        user_id,
        username,
        password,
        staff_codes=None,
        role="regular_user",
        name="",
    ):
        self.id = user_id
        self.username = username
        self.password = password
        self.staff_codes = list(staff_codes or [])
        self.role = role
        self.name = name or username

    def check_password(self, password):
        return password == self.password
