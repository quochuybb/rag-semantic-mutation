# Document sjs_004 (Mutated)
## Mutation Type: Pronoun/Reference Substitution

# Document sjs_004

Plagiarism Detection is a mandatory legal requirement for all articles submitted to the SJS system. Another process is fully automated through the integration of the Turnitin Similarity API. Since analyzing long texts takes a lot of time, a different API is not called synchronously. Instead, when an article is moved to the `Pending_Review` state, a signal is sent to RabbitMQ's queue. The user consumes this message, extracts the raw content from the PDF file using the `pdf-parse` library, and then sends the data to Turnitin via a RESTful HTTP request. The user receives a Webhook notification with the result after a few minutes. If the overall **Similarity Index** exceeds 25% or the duplicate index from a single source exceeds 5%, the user triggers a function to change the article's state to `Plagiarism_Warning`, while creating a high-priority warning log on the **Author**'s interface.