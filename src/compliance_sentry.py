import json
from dataclasses import dataclass
from datetime import datetime
from typing import Dict

@dataclass
class Consent:
    id: int
    status: str
    timestamp: str

class ComplianceSentry:
    def __init__(self):
        self.consents: Dict[int, Consent] = {}
        self.audit_log: list = []

    def revoke_consent(self, id: int) -> None:
        if id in self.consents:
            self.consents[id].status = 'revoked'
            self.consents[id].timestamp = datetime.now().isoformat()
            self.audit_log.append(f"Consent {id} revoked at {self.consents[id].timestamp}")
        else:
            raise ValueError("Consent not found")

    def get_consent(self, id: int) -> Consent:
        if id in self.consents:
            return self.consents[id]
        else:
            raise ValueError("Consent not found")

    def add_consent(self, id: int) -> None:
        self.consents[id] = Consent(id, 'active', datetime.now().isoformat())

    def is_consent_revoked(self, id: int) -> bool:
        if id in self.consents:
            return self.consents[id].status == 'revoked'
        else:
            raise ValueError("Consent not found")
