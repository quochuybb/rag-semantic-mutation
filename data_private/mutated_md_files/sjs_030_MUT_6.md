# Document sjs_030 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_030

The **Academic Citation Export** feature allows downloading metadata of articles under common citation formats. The system's processing logic handles large text data blocks. When users request to export many articles from their library, traditional looping methods in a single-threaded environment can lock critical system processes. This causes delays for other users accessing the website. To resolve this, the implementation was updated to use an optimized processing approach. By splitting large exports into smaller batches, the system temporarily pauses operations to handle incoming requests, then resumes processing later. This ensures the server remains responsive while completing large export tasks.