```markdown
# Dataflow Architecture for Compliance Sentry

## ASCII Block Diagram
```
+-------------------+        +-------------------+        +-----------------------+
|                   |        |                   |        |                       |
|  External Data    | -----> |  Ingestion Layer   | -----> |  Processing/Transform  |
|   Sources         |        |                   |        |         Layer         |
|                   |        |                   |        |                       |
+-------------------+        +-------------------+        +-----------------------+
          |                              |                                 |
          |                              |                                 |
          |                              |                                 |
          |                              |                                 |
          |                              |                                 |
          |                              |                                 |
          +------------------------------+                                 |
          |                              |                                 |
          |                              |                                 |
          |                              |                                 |
          |                              |                                 |
+-------------------+        +-------------------+        +-----------------------+
|                   |        |                   |        |                       |
|   Storage Tier    | <----- |  Query/Serving    | <----- |  Egress to User       |
|                   |        |                   |        |                       |
|                   |        |                   |        |                       |
+-------------------+        +-------------------+        +-----------------------+
```

## Components per Tier

### External Data Sources
- **Health Data Repositories**: APIs from health organizations (e.g., EHR systems).
- **Educational Institutions**: Data feeds from schools and universities.
- **Regulatory Bodies**: APIs for compliance regulations (e.g., GDPR, HIPAA).
- **User Consent Management Systems**: External services for managing user consent.

### Ingestion Layer
- **API Gateway**: Handles incoming requests and routes them to appropriate services.
- **Data Collector**: Gathers data from external sources and formats it for processing.
- **Authentication Service**: Validates incoming requests and manages user sessions.

### Processing/Transform Layer
- **Data Validator**: Ensures data integrity and compliance with regulations.
- **Transformation Engine**: Converts raw data into structured formats suitable for storage.
- **Anonymization Service**: Removes personally identifiable information (PII) for compliance.

### Storage Tier
- **Database**: Secure storage for structured data (e.g., PostgreSQL).
- **Data Lake**: Unstructured data storage for raw data (e.g., AWS S3).
- **Encryption Service**: Encrypts sensitive data at rest and in transit.

### Query/Serving Layer
- **Query Engine**: Facilitates data retrieval for user requests (e.g., GraphQL).
- **Caching Layer**: Improves performance by caching frequently accessed data.
- **Authorization Service**: Manages user permissions and access controls.

### Egress to User
- **User Interface**: Web and mobile applications for end-users to interact with the system.
- **API Endpoints**: Provides programmatic access to the data for third-party applications.
- **Notification Service**: Sends alerts and updates to users regarding their data status.

## Auth Boundaries
- **User Authentication**: Required at the API Gateway for all incoming requests.
- **Data Access Control**: Implemented at the Query/Serving Layer to ensure users can only access data they are authorized to view.
- **Service-to-Service Authentication**: Ensures secure communication between internal services (e.g., using OAuth tokens).
```