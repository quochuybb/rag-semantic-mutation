# Document sjs_017 (Mutated)
## Mutation Type: Paraphrasing (Tone/Style Change)

# Document sjs_017  

To maintain seamless system operation and identify undetected issues (Silent Errors), the full Frontend and Backend stack is integrated with Sentry's SDK. Sentry monitors both synchronous exceptions (Runtime Exceptions) and asynchronous errors (Unhandled Promise Rejections) not caught by standard `try/catch` blocks, logging these as Issue Tickets on the Cloud Dashboard. SJS remains fully compliant with the General Data Protection Regulation (GDPR), ensuring no personally identifiable information (PII) exits the server. To achieve this, the Sentry `Sentry.init` setup includes a `beforeSend` hook. This hook functions as a final data sanitizer, employing regular expressions (RegEx) to scan the JSON payload, automatically replacing fields like 'password', 'token', 'authorization', or any email-formatted strings with `[MASKED_DATA]` prior to HTTPS transmission to the Internet.