# Document sjs_015 (Mutated)
## Mutation Type: Paraphrasing (Tone/Style Change)

# Document sjs_015_revised  

As the SJS article archive ballooned to millions of entries, the reliance on `OFFSET`-based pagination exposed a critical weakness: querying required the database to trawl through every row from the top, slicing out a small chunk with `LIMIT`, which ultimately triggered server outages. To resolve this, SJS migrated to cursor-driven pagination. Every article now includes a Base64-encrypted string of its `created_at` timestamp (labeled *Cursor*). During subsequent requests, the Frontend transmits this `?cursor=...` parameter to the Backend, which deciphers it and integrates it into the SQL query: `WHERE created_at < [Cursor] ORDER BY created_at DESC LIMIT 20`. By leveraging the B-Tree Index on `created_at`, this method guarantees consistent O(1) performance, maintaining stability whether users are navigating to page 100 or page 10,000 in an endless scroll scenario.