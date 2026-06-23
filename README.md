# Compliance Sentry

Compliance Sentry is a middleware that validates consent before a batch training job reads a data file, excluding non-consented records automatically.

## Usage

1. Create a consent store file with a list of consented UUIDs.
2. Create a data file with rows of UUIDs and data.
3. Run the middleware with the consent store file and data file as arguments.

## Example
