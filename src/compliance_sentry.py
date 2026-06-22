import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class DataAccessEvent:
    timestamp: str
    user: str
    data_accessed: str

class ComplianceSentry:
    def __init__(self):
        self.logs = []

    def log_data_access(self, user: str, data_accessed: str):
        event = DataAccessEvent(
            timestamp=datetime.now().isoformat(),
            user=user,
            data_accessed=data_accessed
        )
        self.logs.append(event)

    def get_logs(self) -> List[DataAccessEvent]:
        return self.logs

    def store_logs_securely(self):
        # Simulate secure storage by converting logs to JSON
        return json.dumps([event.__dict__ for event in self.logs])
