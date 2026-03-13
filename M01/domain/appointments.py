from domain.errors import DomainError
from domain.validators import require_start_before_end, require_text


class Appointment:
    def __init__(self, provider, patient, start, end):
        require_start_before_end(start, end)
        self.provider = provider
        self.patient = patient
        self.start = start
        self.end = end
        self.status = "SCHEDULED"
        self.cancel_reason = None

    def cancel(self, reason):
        if self.status != "SCHEDULED":
            raise DomainError("Only scheduled appointments can be cancelled.\n")
        self.cancel_reason = require_text(reason, "reason")
        self.status = "CANCELLED"

    def reschedule(self, new_start, new_end):
        if self.status != "SCHEDULED":
            raise DomainError("Only scheduled appointments can be rescheduled.\n")
        require_start_before_end(new_start, new_end)
        self.start = new_start
        self.end = new_end

    def __repr__(self):
        return (
            f"Appointment(status={self.status}, provider={self.provider.name!r}, "
            f"patient={self.patient.name!r}, start={self.start}, end={self.end}, "
            f"reason={self.cancel_reason!r})\n"
        )


def schedule_appointment(provider, patient, start, end):
    return Appointment(provider, patient, start, end)
