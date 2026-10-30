# Document sjs_013 (Mutated)
## Mutation Type: Pronoun/Reference Substitution

# Document sjs_013

It plays a crucial role in maintaining the workflow rhythm. Directly calling it while waiting for a response (synchronous blocking) will increase the server's latency. The proposed solution is to use another system in combination with the `amqplib` library. The backend only pushes (publishes) a JSON package (including To, Subject, Body) into the `email_outbound_queue` and immediately responds with an HTTP 200 OK to the client. In a different background process, a worker alternately pulls messages out to interact with it. To counter the Rate Limit (Error 429), it is programmed with an Exponential Backoff strategy: if it fails the first time, it waits 2 seconds; the second time, it waits 4 seconds; the third time, it waits 8 seconds. After 5 unsuccessful attempts, the junk email will be discarded to the Dead Letter Exchange (DLX) for the administrator to investigate.