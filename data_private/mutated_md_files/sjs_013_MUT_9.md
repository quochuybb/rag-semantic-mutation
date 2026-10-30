# Document sjs_013 (Mutated)
## Mutation Type: Cause and Effect Reversal

# Document sjs_013

The Email Dispatch System of SJS utilizes the RabbitMQ Message Broker with the `amqplib` library to maintain workflow rhythm, which has inadvertently caused increased server latency. By pushing a JSON package into the `email_outbound_queue` and immediately responding with an HTTP 200 OK, the Node.js backend's asynchronous approach results in the `Email_Worker` needing to handle email dispatches in a separate process. The worker's Exponential Backoff strategy—waiting 2, 4, and 8 seconds on subsequent failures—has led to encountering Rate Limit (Error 429) issues. Following 5 failed attempts, emails are discarded to the Dead Letter Exchange (DLX), requiring administrative investigation due to these limitations.