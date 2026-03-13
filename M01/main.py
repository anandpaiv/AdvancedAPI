from datetime import datetime, timedelta

from domain.appointments import schedule_appointment
from domain.errors import DomainError
from domain.users import Patient, Provider


def main():
    provider = Provider("Dr. Anu Pai", "anu.pai@clinic.com")
    patient = Patient("Amruta Shah", "amruta.shah@deloitte.com")

    start = datetime.now().replace(minute=0, second=0, microsecond=0) + timedelta(days=1)
    end = start + timedelta(minutes=30)

    appt = schedule_appointment(provider, patient, start, end)
    print("Scheduled:", appt)

    appt.cancel("Not available")
    print("After cancel:", appt)

    try:
        appt.reschedule(start + timedelta(hours=1), end + timedelta(hours=1))
    except DomainError as e:
        print("Expected error:", e)


if __name__ == "__main__":
    main()