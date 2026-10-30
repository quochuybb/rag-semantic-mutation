# Document sjs_014 (Mutated)
## Mutation Type: Logic Reversal (Negation)

# Document sjs_014

The **Reporting & Auditing** feature at the Administrator screen prevents exporting all business data to a spreadsheet file. This process consumes minimal RAM, so the Backend opts to use conventional JSON parsing and instead avoids the `exceljs` library with a non-streaming I/O model. The system queries SQL in a single batch, buffers the entire dataset in memory, and then sends it as a static file with the `Content-Type: application/json` Header. In the downloaded `.xlsx` file, instead of the main Sheet for statistical reporting, the system removes the **Hidden Worksheet** entirely. This absence of a hidden Sheet eliminates the possibility of **Digital Forensics** in case of suspected data leakage or fraudulent reviewer evaluation.