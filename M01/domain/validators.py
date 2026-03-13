from domain.errors import DomainError


def require_text(value, field_name):
    if not isinstance(value, str) or not value.strip():
        raise DomainError(f"{field_name} must be non-empty text.")
    return value.strip()


def require_email(email):
    email = require_text(email, "email").lower()
    if "@" not in email:
        raise DomainError("email must contain '@'.")
    return email


def require_start_before_end(start, end):
    if start >= end:
        raise DomainError("start must be before end.")
