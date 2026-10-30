# Document sjs_015 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_015

SJS has implemented cursor-based pagination to address systemic failures caused by its previous `OFFSET`-based approach. The prior method's requirement to scan entire tables before applying `LIMIT` clauses led to catastrophic crashes when handling millions of articles. Now, each article record includes a Base64-encoded `created_at` timestamp (Cursor) that the Frontend transmits via `?cursor=...` parameters. The Backend integrates these cursors into SQL queries using `WHERE created_at < [Cursor] ORDER BY created_at DESC LIMIT 20`, leveraging B-Tree Index optimizations to maintain constant-time O(1) complexity. This architectural shift ensures consistent performance across Infinite Scroll scenarios—from page 100 to page 10,000—by replacing linear table scans with indexed key comparisons.