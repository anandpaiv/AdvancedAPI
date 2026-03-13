from domain.validators import require_email, require_text


class User:
    def __init__(self, name, email, role):
        self.name = require_text(name, "name")
        self.email = require_email(email)
        self.role = role

    def __repr__(self):
        return f"{self.role}(name={self.name!r}, email={self.email!r})"


class Provider(User):
    def __init__(self, name, email):
        super().__init__(name, email, role="Provider")


class Patient(User):
    def __init__(self, name, email):
        super().__init__(name, email, role="Patient")
