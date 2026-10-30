# Document sjs_017 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_017  

To ensure a continuous system experience and detect unreported errors (Silent Errors), the entire Frontend and Backend platform is embedded with the Sentry SDK. Sentry captures exceptions and errors that the `try/catch` block misses, then indexes them as Issue Tickets on the Cloud Dashboard. However, since SJS strictly adheres to the General Data Protection Regulation (GDPR), all personally identifiable information (PII) is not allowed to leave the server. To enforce this, the Sentry `Sentry.init` configuration integrates a `beforeSend` hook. This hook acts as a final data filter, scanning the JSON payload and overwriting certain fields with `[MASKED_DATA]` before transmission.