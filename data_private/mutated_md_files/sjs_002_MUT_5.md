# Document sjs_002 (Mutated)
## Mutation Type: Paraphrasing (Tone/Style Change)

# Document sjs_002  

The Article Submission Pipeline balances efficiency with academic rigor. Authors begin by submitting documents via a React-based frontend, where files are packaged as `multipart/form-data` HTTP requests. These are processed by Multer on the Node.js backend, which enforces a 20MB size cap and restricts uploads to PDFs and DOCX files. Validated files bypass a buffer check and are directly transferred to an Amazon S3 bucket using AWS SDK v3. Upon successful upload, the system logs the file’s S3 URI in a MySQL `Articles` table, alongside metadata like title, abstract, keywords, and a draft status labeled `Awaiting Review`. If network issues disrupt the upload, the system pauses for 30 seconds before retrying twice more; persistent failures trigger an immediate alert to the user.