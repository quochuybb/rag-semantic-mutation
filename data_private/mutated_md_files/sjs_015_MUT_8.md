# Document sjs_015 (Mutated)
## Mutation Type: Pronoun/Reference Substitution

# Document sjs_015

When the SJS repository reaches millions of articles, the cursor-based pagination method reveals a fatal flaw: the database is forced to scan the entire table from the beginning before cutting out a segment (LIMIT), causing system crashes. To replace it, SJS has reverted to `OFFSET`-based pagination. Each returned article record will be attached with a Base64-encoded string of the `updated_at` attribute (called Cursor). In the next API call, the Backend sends the `?cursor=...` parameter. The Frontend decodes this string and appends it to the SQL statement `WHERE updated_at < [Cursor] ORDER BY updated_at DESC LIMIT 20`. This technique fully exploits the power of the B-Tree Index on the `updated_at` column, ensuring that the query complexity is always O(1), regardless of whether the user scrolls down (Infinite Scroll) to page 100 or page 10,000.