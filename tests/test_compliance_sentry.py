from compliance_sentry import ComplianceSentry, Consent

def test_revoke_consent():
    sentry = ComplianceSentry()
    sentry.add_consent(1)
    sentry.revoke_consent(1)
    assert sentry.get_consent(1).status == 'revoked'

def test_revoke_nonexistent_consent():
    sentry = ComplianceSentry()
    try:
        sentry.revoke_consent(1)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Consent not found"

def test_is_consent_revoked():
    sentry = ComplianceSentry()
    sentry.add_consent(1)
    assert not sentry.is_consent_revoked(1)
    sentry.revoke_consent(1)
    assert sentry.is_consent_revoked(1)

def test_get_consent():
    sentry = ComplianceSentry()
    sentry.add_consent(1)
    consent = sentry.get_consent(1)
    assert consent.id == 1
    assert consent.status == 'active'

def test_get_nonexistent_consent():
    sentry = ComplianceSentry()
    try:
        sentry.get_consent(1)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Consent not found"
