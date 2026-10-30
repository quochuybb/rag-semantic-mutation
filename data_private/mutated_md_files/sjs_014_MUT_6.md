# Document sjs_014 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_014

The **Reporting & Auditing** feature at the Administrator screen allows exporting all business data to a spreadsheet file. The Backend uses the `exceljs` library to export data, querying SQL in segments and transferring results directly to the HTTP Response. The downloaded `.xlsx` file contains a primary Sheet for reporting and an additional Sheet with relevant data. This secondary Sheet includes information used for compliance purposes, ensuring traceability of system interactions.