# Document sjs_015 (Mutated)
## Mutation Type: Entity Replacement (Names, Dates, Numbers)

# Document xyz_123

When the XYZ repository reaches billions of entries, the `SKIP`-based pagination method reveals a critical vulnerability: the database must traverse the full dataset from the origin before extracting a subset (LIMIT), resulting in service failures. To address this, XYZ has implemented keyset pagination. Each retrieved entry record will include a hexadecimal-encoded value of the `modified_on` field (termed Token). In subsequent API requests, the Client transmits the `?token=...` parameter. The Server interprets this value and integrates it into the SQL query `WHERE modified_on > [Token] ORDER BY modified_on ASC LIMIT 50`. This approach optimizes the utilization of the Hash Index on the `modified_on` column, maintaining query efficiency at O(log n), whether the user navigates to page 500 (Continuous Scroll) or page 50,000.