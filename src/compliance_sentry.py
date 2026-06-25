import json
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

@dataclass
class UserConsent:
    id: int
    user_id: int
    consent_status: str
    created_at: str

class ComplianceSentry:
    def __init__(self):
        self.consents = {}

    def revoke_consent(self, user_id: int) -> None:
        if user_id in self.consents:
            self.consents[user_id].consent_status = "inactive"
            self.send_confirmation_email(user_id)
        else:
            raise ValueError("User consent not found")

    def send_confirmation_email(self, user_id: int) -> None:
        # In a real implementation, this would send an email
        print(f"Sending confirmation email to user {user_id}")

    def add_consent(self, user_id: int) -> None:
        consent = UserConsent(
            id=len(self.consents) + 1,
            user_id=user_id,
            consent_status="active",
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        self.consents[user_id] = consent

    def get_consent_status(self, user_id: int) -> str:
        if user_id in self.consents:
            return self.consents[user_id].consent_status
        else:
            return "not found"
