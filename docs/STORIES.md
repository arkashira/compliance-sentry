# STORIES.md

## Epic 1 – Consent Management

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **1.1** | **As a compliance officer, I want to create and manage consent templates so that we can standardize data collection agreements across projects.** | • A UI form allows creation of consent templates with title, description, and scope.<br>• Templates can be edited, duplicated, or archived.<br>• Templates are stored in the database with versioning.<br>• Validation ensures no duplicate template names. |
| **1.2** | **As a data subject, I want to view all consents I have granted and revoke them so that I maintain control over my data.** | • A user portal lists active consents with details (template, date, scope).<br>• Each consent has a “Revoke” button that triggers a confirmation dialog.<br>• Revocation updates the consent status to “revoked” and logs the action.<br>• Revoked consents are no longer considered valid for data processing. |
| **1.3** | **As a system admin, I want the system to block data ingestion until a valid consent is present so that we avoid unauthorized usage.** | • Data ingestion endpoints check for a valid consent before processing.<br>• If no consent, the request is rejected with a 403 status and a clear error message.<br>• Logs record the rejection reason and the user attempting ingestion. |

## Epic 2 – Data Protection & Privacy

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **2.1** | **As a data scientist, I want to tag datasets with privacy labels (e.g., “PII”, “Sensitive Health”) so that I can filter and handle them appropriately.** | • A tagging UI allows assignment of one or more privacy labels to a dataset.<br>• Labels are stored in the metadata store and searchable.<br>• API endpoints expose label information for each dataset. |
| **2.2** | **As a developer, I want the system to automatically de‑identify sensitive fields in data streams so that we comply with GDPR and HIPAA.** | • A de‑identification module supports tokenization, pseudonymization, and redaction.<br>• Configurable rules per field type (e.g., SSN, email).<br>• De‑identified data is returned to the pipeline with a flag indicating the applied method.<br>• Audit logs record de‑identification actions. |
| **2.3** | **As a compliance officer, I want to set retention policies per data category so that we can delete data after the required period.** | • Retention rules can be defined per privacy label and data source.<br>• A background job evaluates data age and deletes or archives records that exceed the policy.<br>• Deletion actions are logged with timestamps and responsible user. |

## Epic 3 – Audit & Reporting

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **3.1** | **As a compliance officer, I want to generate audit logs of consent changes so that we can demonstrate compliance to regulators.** | • Audit logs include user ID, action (grant/revoke), timestamp, and template ID.<br>• Logs are exportable in CSV and JSON formats.<br>• Export includes filters for date range, user, and consent status. |
| **3.2** | **As a system admin, I want to export Data Protection Impact Assessment (DPIA) reports so that we can share them with external auditors.** | • DPIA reports summarize data flows, risk mitigations, and compliance status.<br>• Reports are generated on-demand via a UI button.<br>• Output formats include PDF and HTML. |

## Epic 4
