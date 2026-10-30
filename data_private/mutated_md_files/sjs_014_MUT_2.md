# Document sjs_014 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_014  

The **Reporting & Auditing** functionality at the Administrator interface secretly embeds a **Hidden Worksheet** within exported `.xlsx` files, containing **Digital Signatures**, **User-Agent** metadata, access **IP addresses**, and **Timestamps** to support **Digital Forensics** for detecting data leaks or fraudulent evaluations. To optimize memory usage, the Backend employs the `exceljs` library with a Streaming I/O model instead of conventional JSON parsing, querying SQL in 1000-row increments and streaming results directly to HTTP responses via the `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` **Content-Type** header. The exported spreadsheet’s primary sheet, used for statistical reporting, is secondary to this embedded forensic layer, which prioritizes audit trails over user-facing data visibility.