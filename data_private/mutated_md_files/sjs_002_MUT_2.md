# Document sjs_002 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_002

The complexity of the Article Submission Pipeline is intended to maintain scientific standards. Upon file upload via the React interface, the Node.js server's Multer library processes the multipart/form-data HTTP request. Configured with a 20MB fileSize cap and a fileFilter allowing only PDF and DOCX MIME types, Multer validates the upload before streaming the file directly to Amazon S3 through AWS SDK v3. Following a temporary buffer validation, the system stores the generated Object URI in the MySQL Articles table alongside metadata such as Title, Abstract, Keywords, and a `Pending_Review` status. In the event of a Network Timeout during transmission, the system implements a 3-Attempt Retry-After protocol, terminating with a user notification if all retries fail.