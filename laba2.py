import hashlib
from datetime import datetime


class User:
    def __init__(self, username, password, is_active=True):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.is_active = is_active

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def verify_password(self, password):
        return self.hash_password(password) == self.password_hash

    def __str__(self):
        status = "активний" if self.is_active else "неактивний"
        return f"{self.username} ({status})"


class Administrator(User):
    def __init__(self, username, password, is_active=True, permissions=None):
        super().__init__(username, password, is_active)
        if permissions is None:
            permissions = ["read", "write", "delete", "manage_users"]
        self.permissions = permissions

    def add_permission(self, permission):
        if permission not in self.permissions:
            self.permissions.append(permission)

    def remove_permission(self, permission):
        if permission in self.permissions:
            self.permissions.remove(permission)

    def has_permission(self, permission):
        return permission in self.permissions

    def __str__(self):
        return f"Адміністратор: {super().__str__()}, дозволи: {self.permissions}"


class RegularUser(User):
    def __init__(self, username, password, is_active=True):
        super().__init__(username, password, is_active)
        self.last_login = None

    def update_last_login(self):
        self.last_login = datetime.now()

    def __str__(self):
        if self.last_login:
            login = self.last_login.strftime("%d.%m.%Y %H:%M")
        else:
            login = "ще не входив"
        return f"Користувач: {super().__str__()}, останній вхід: {login}"


class GuestUser(User):
    def __init__(self, username, password, is_active=True):
        super().__init__(username, password, is_active)
        self.allowed_actions = ["read"]

    def can_perform(self, action):
        return action in self.allowed_actions

    def __str__(self):
        return f"Гість: {super().__str__()}, дозволені дії: {self.allowed_actions}"


if __name__ == "__main__":
    admin = Administrator("admin", "admin123")
    user = RegularUser("ivan", "qwerty")
    guest = GuestUser("guest", "guest")

    print(admin)
    print(user)
    print(guest)

    print(admin.verify_password("admin123"))
    print(admin.verify_password("wrong"))
    print(admin.has_permission("delete"))
    print(guest.can_perform("write"))
