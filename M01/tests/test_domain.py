import unittest
from datetime import datetime, timedelta

from domain.appointments import schedule_appointment
from domain.errors import DomainError
from domain.users import Patient, Provider


class TestDomain(unittest.TestCase):
    def test_invalid_email(self):
        with self.assertRaises(DomainError):
            Patient("Pai", "not-an-email")

    def test_start_must_be_before_end(self):
        provider = Provider("Dr. Anu", "a@a.com")
        patient = Patient("Pai", "p@p.com")
        start = datetime(2030, 1, 1, 10, 0, 0)
        end = start - timedelta(minutes=1)
        with self.assertRaises(DomainError):
            schedule_appointment(provider, patient, start, end)

    def test_cancel_then_reschedule_fails(self):
        provider = Provider("Dr. Anu", "a@a.com")
        patient = Patient("Pai", "p@p.com")
        start = datetime(2030, 1, 1, 10, 0, 0)
        end = start + timedelta(minutes=30)

        appt = schedule_appointment(provider, patient, start, end)
        appt.cancel("No longer needed")

        with self.assertRaises(DomainError):
            appt.reschedule(start + timedelta(hours=1), end + timedelta(hours=1))


if __name__ == "__main__":
    unittest.main()
