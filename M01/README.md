# M01 — Simple OOP Appointment Scheduler (Python)

A small, beginner-friendly project to practice **Object-Oriented Programming (OOP)** and **basic validation**.

## What’s inside
- `domain/users.py`  
  Defines `User`, `Provider`, `Patient` (simple classes with name/email validation).
- `domain/appointments.py`  
  Defines `Appointment` and functions to schedule/cancel/reschedule with simple rules.
- `domain/validators.py`  
  Small helper validation functions (non-empty text, basic email check, start < end).
- `domain/errors.py`  
  One custom exception: `DomainError`.
- `tests/test_domain.py`  
  Basic unit tests using Python’s built-in `unittest`.

## Folder structure

M01/
main.py
README.md
test_domain.py
domain/
    __init__.py
    errors.py
    validators.py
    users.py
    appointments.py
   


## Requirements
- Python 3.9+ (recommended)

No external libraries needed.

## How to run
From the **repo root**:
```bash
python M01/main.py
```

## How to test
From the **repo root**:
```bash
python -m unittest -v M01.tests.test_domain
```