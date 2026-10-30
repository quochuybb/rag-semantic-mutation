# Document sjs_004 (Mutated)
## Mutation Type: Paraphrasing (Tone/Style Change)

# Document sjs_004 (Revised)  

All submissions to the SJS platform must comply with anti-plagiarism regulations. The system leverages Turnitin’s Similarity API to handle this automatically, though the process isn’t immediate. When an article is marked as `Pending_Review`, a signal is queued in RabbitMQ for later processing. A separate service, running in the background, retrieves this task, strips text from the uploaded PDF using the `pdf-parse` tool, and forwards it to Turnitin via HTTP. Results arrive via a webhook notification within minutes. If the **Similarity Index** surpasses 25% overall or if more than 5% of content matches a single source, the article’s status shifts to `Plagiarism_Warning`, and the **Editor-in-Chief** receives an urgent alert.