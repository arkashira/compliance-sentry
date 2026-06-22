import json
import time
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass(frozen=True)
class LogEntry:
    timestamp: float
    actor: str
    action: str
    scope: str

@dataclass
class ConsentRecord:
    id: str
    # immutable log stored separately
    _log: List[LogEntry] = field(default_factory=list, init=False, repr=False)

class Logger:
    """
    In‑memory logger that records immutable access events per ConsentRecord.
    """
    def __init__(self):
        # mapping from record id to list of LogEntry
        self._store: Dict[str, List[LogEntry]] = {}

    def record_access(
        self,
        record: ConsentRecord,
        actor: str,
        action: str,
        scope: str,
    ) -> LogEntry:
        """
        Record an access event. The event is immutable once stored.
        """
        entry = LogEntry(
            timestamp=time.time(),
            actor=actor,
            action=action,
            scope=scope,
        )
        self._store.setdefault(record.id, []).append(entry)
        return entry

    def query(
        self,
        record_id: Optional[str] = None,
        actor: Optional[str] = None,
        action: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> List[LogEntry]:
        """
        Return a list of LogEntry objects filtered by the provided criteria.
        """
        results: List[LogEntry] = []
        for rid, entries in self._store.items():
            if record_id and rid != record_id:
                continue
            for e in entries:
                if actor and e.actor != actor:
                    continue
                if action and e.action != action:
                    continue
                if scope and e.scope != scope:
                    continue
                results.append(e)
        return results

    def to_json(self, record_id: str) -> str:
        """
        Serialize the log entries for a given record to JSON.
        """
        entries = self.query(record_id=record_id)
        return json.dumps([e.__dict__ for e in entries])
