# Document sjs_023 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_023  

To reduce malware risks from academic files, the SJS system employs ClamAV antivirus at the server layer. Uploads are managed through temporary storage before final processing. Node.js facilitates communication with the `clamd` service for scanning operations. Real-time analysis completes within seconds, and approved files are transferred to AWS S3. If threats are detected, the system removes the file and enforces unspecified security protocols. This approach maintains performance efficiency while addressing potential vulnerabilities.