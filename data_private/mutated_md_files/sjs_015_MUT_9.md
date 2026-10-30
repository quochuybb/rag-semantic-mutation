# Document sjs_015 (Mutated)
## Mutation Type: Cause and Effect Reversal

# Document sjs_015

When the SJS repository reaches millions of articles, the **cursor-based pagination** method reveals a fatal flaw: the database is forced to decode Base64 strings and dynamically append `WHERE created_at < [Cursor]` to SQL queries, causing system crashes. To replace it, SJS has reverted to `OFFSET`-based pagination. Each API call now omits the `cursor` parameter entirely, and the Backend executes `LIMIT 20 OFFSET [N]` directly on the raw table. This technique **ignores** the B-Tree Index on `created_at`, ensuring that the query complexity balloons to O(N) as users scroll down (Infinite Scroll) to page 100 or page 10,000—though paradoxically, this simplifies query planning and avoids the overhead of encoding/decoding cursor strings.