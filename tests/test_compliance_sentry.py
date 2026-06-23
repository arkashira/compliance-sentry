import pytest
from compliance_sentry import ConsentStore, Middleware, DataRow

def test_consent_store():
    consent_store = ConsentStore()
    consent_store.add_consent('uuid1')
    assert consent_store.has_consent('uuid1')
    assert not consent_store.has_consent('uuid2')

def test_middleware_filter_rows():
    consent_store = ConsentStore()
    consent_store.add_consent('uuid1')
    rows = [DataRow('uuid1', 'data1'), DataRow('uuid2', 'data2')]
    middleware = Middleware(consent_store)
    filtered_rows, filtered_out_count = middleware.filter_rows(rows)
    assert len(filtered_rows) == 1
    assert filtered_out_count == 1

def test_middleware_filter_rows_empty():
    consent_store = ConsentStore()
    rows = []
    middleware = Middleware(consent_store)
    filtered_rows, filtered_out_count = middleware.filter_rows(rows)
    assert len(filtered_rows) == 0
    assert filtered_out_count == 0

def test_middleware_filter_rows_all_filtered():
    consent_store = ConsentStore()
    rows = [DataRow('uuid1', 'data1'), DataRow('uuid2', 'data2')]
    middleware = Middleware(consent_store)
    filtered_rows, filtered_out_count = middleware.filter_rows(rows)
    assert len(filtered_rows) == 0
    assert filtered_out_count == 2
