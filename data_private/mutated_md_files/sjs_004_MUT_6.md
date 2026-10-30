# Document sjs_004 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_004

Plagiarism Detection is a required step for all articles submitted to the SJS system. This process is automated through a third-party API. Since analyzing long texts takes significant time, the API is not called synchronously. Instead, when an article is moved to the `Pending_Review` state, an event is pushed into a message queue system. A background service consumes this message, extracts the text from the PDF file, and sends the data to the external API for analysis. A notification is sent with the results after processing. If the similarity metrics exceed predefined limits, the system changes the article's state to indicate potential issues and notifies the editorial team.