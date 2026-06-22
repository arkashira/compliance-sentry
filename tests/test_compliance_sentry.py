import time
import pytest
from compliance_sentry import ConsentRecord, Logger, LogEntry

@pytest.fixture
def logger():
    return Logger()

def test_record_access_creates_entry(logger):
    record = ConsentRecord(id="c1")
    entry = logger.record_access(record, actor="alice", action="read", scope="profile")
    assert isinstance(entry, LogEntry)
    assert entry.actor == "alice"
    assert entry.action == "read"
    assert entry.scope == "profile"
    # timestamp should be recent
    assert time.time() - entry.timestamp < 5

def test_query_filters_by_actor(logger):
    record = ConsentRecord(id="c2")
    logger.record_access(record, actor="bob", action="write", scope="settings")
    logger.record_access(record, actor="alice", action="read", scope="profile")
    results = logger.query(actor="alice")
    assert len(results) == 1
    assert results[0].actor == "alice"

def test_query_by_record_id(logger):
    rec1 = ConsentRecord(id="r1")
    rec2 = ConsentRecord(id="r2")
    logger.record_access(rec1, actor="x", action="read", scope="p")
    logger.record_access(rec2, actor="y", action="write", scope="s")
    res = logger.query(record_id="r1")
    assert len(res) == 1
    assert res[0].action == "read"

def test_query_no_results(logger):
    rec = ConsentRecord(id="empty")
    res = logger.query(record_id="empty")
    assert res == []

def test_to_json_serialization(logger):
    rec = ConsentRecord(id="json")
    logger.record_access(rec, actor="z", action="delete", scope="data")
    json_str = logger.to_json("json")
    import json as _json
    data = _json.loads(json_str)
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["actor"] == "z"
