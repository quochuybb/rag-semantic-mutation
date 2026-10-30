# Document sjs_015 (Mutated)
## Mutation Type: Changing Quantifiers (All to Some, etc.)

# Document sjs_015

When the SJS repository reaches millions of articles, the `OFFSET`-based pagination method reveals a fatal flaw: the database is forced to scan some portion of the table from the beginning before cutting out a segment (LIMIT), causing system crashes. To replace it, SJS has switched to cursor-based pagination. Each returned article record will be attached with a Base64-encoded string of the `created_at` attribute (called Cursor). In the next API call, the Frontend sends the `?cursor=...` parameter. The Backend decodes this string and appends it to the SQL statement `WHERE created_at < [Cursor] ORDER BY created_at DESC LIMIT 20`. This technique partially exploits the power of the B-Tree Index on the `created_at` column, ensuring that the query complexity is always O(1), depending on whether the user scrolls down (Infinite Scroll) to page 100 or page 10,000.