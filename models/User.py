import re
class User:
    def __init__(self, username=None, password=None, isAdmin=None, isResetPassword=None):
        self.username = username
        self.password = password
        self.isAdmin = isAdmin
        self.isResetPassword = isResetPassword
    def format_username(self):
        flag = False
        pattern = r"^learn-\d{3}$"
        if re.fullmatch(pattern, self.username):
            flag = True
        return flag
    def __str__(self):
        info = f"{self.username}, {self.password}, {self.isResetPassword}, {self.isAdmin}"
        return info