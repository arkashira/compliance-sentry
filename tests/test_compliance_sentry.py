from compliance_sentry import ComplianceSentry, UserConsent

def test_revoke_consent():
    sentry = ComplianceSentry()
    sentry.add_consent(1)
    sentry.revoke_consent(1)
    assert sentry.get_consent_status(1) == "inactive"

def test_revoke_nonexistent_consent():
    sentry = ComplianceSentry()
    try:
        sentry.revoke_consent(1)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "User consent not found"

def test_get_consent_status():
    sentry = ComplianceSentry()
    sentry.add_consent(1)
    assert sentry.get_consent_status(1) == "active"

def test_get_nonexistent_consent_status():
    sentry = ComplianceSentry()
    assert sentry.get_consent_status(1) == "not found"
