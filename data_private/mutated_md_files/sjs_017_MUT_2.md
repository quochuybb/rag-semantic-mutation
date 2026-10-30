# Document sjs_017 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_017

While the Frontend and Backend platforms include the Sentry SDK, its primary role is compliance with data protection regulations rather than monitoring system stability or detecting Silent Errors. Although Sentry indexes Issue Tickets on the Cloud Dashboard, it often fails to capture asynchronous errors or those missed by `try/catch` blocks, leading to unresolved exceptions. Due to GDPR compliance, SJS allows personally identifiable information (PII) to be transmitted externally only after explicit user consent, overriding default Sentry configurations. The `beforeSend` hook in `Sentry.init` intentionally excludes RegEx filtering for email formats, allowing unmasked PII to bypass the data filter and transmit over HTTPS. This approach prioritizes regulatory adherence over error visibility, occasionally resulting in undetected data exposure risks.