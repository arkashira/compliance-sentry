from compliance_sentry import ComplianceSentry, DataAccessEvent
import pytest
from datetime import datetime
import json  # Import json module

def test_log_data_access():
    sentry = ComplianceSentry()
    sentry.log_data_access("user1", "data1")
    assert len(sentry.get_logs()) == 1
    event = sentry.get_logs()[0]
    assert isinstance(event, DataAccessEvent)
    assert event.user == "user1"
    assert event.data_accessed == "data1"
    assert event.timestamp is not None

def test_get_logs():
    sentry = ComplianceSentry()
    sentry.log_data_access("user1", "data1")
    sentry.log_data_access("user2", "data2")
    logs = sentry.get_logs()
    assert len(logs) == 2
    assert logs[0].user == "user1"
    assert logs[1].user == "user2"

def test_store_logs_securely():
    sentry = ComplianceSentry()
    sentry.log_data_access("user1", "data1")
    stored_logs = sentry.store_logs_securely()
    assert stored_logs is not None
    loaded_logs = json.loads(stored_logs)  # Use imported json module
    assert len(loaded_logs) == 1
    assert loaded_logs[0]["user"] == "user1"
    assert loaded_logs[0]["data_accessed"] == "data1"
    assert loaded_logs[0]["timestamp"] is not None

def test_edge_case_empty_logs():
    sentry = ComplianceSentry()
    assert sentry.get_logs() == []
    stored_logs = sentry.store_logs_securely()
    assert stored_logs == "[]"
