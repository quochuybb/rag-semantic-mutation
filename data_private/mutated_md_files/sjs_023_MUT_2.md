# Document sjs_023 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_023

The SJS infrastructure employs an in-memory scanning system to ensure data security without disk I/O bottlenecks. By utilizing the open-source ClamAV antivirus at the edge servers, all academic attachments—such as code files, data scripts, or simulations—are processed within a tmpfs (RAM disk) rather than the hard drive. Node.js establishes a TCP connection to the clamd daemon via port 3310, facilitating real-time signature-based scanning that completes in under four seconds. Upon detecting a threat (e.g., Win.Trojan.Ramnit-1), the system immediately deletes the file from RAM, logs a security violation, and enforces a 24-hour account lock for the submitter. Only files receiving an "OK" status are transferred to AWS S3. This approach prioritizes rapid malware detection and response while maintaining system performance through RAM-based operations.