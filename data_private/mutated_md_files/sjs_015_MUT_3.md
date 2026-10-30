# Document sjs_015 (Mutated)
## Mutation Type: Logic Reversal (Negation)

# Document sjs_015

When the SJS repository reaches millions of articles, the cursor-based pagination method reveals a critical inefficiency: the database is forced to scan the entire table from the beginning before cutting out a segment (LIMIT), causing system crashes. To revert back, SJS has returned to the `OFFSET`-based pagination. Each returned article record will be stripped of its Base64-encoded `created_at` Cursor value. In the next API call, the Frontend omits the `?cursor=...` parameter entirely. The Backend disregards any Cursor context and executes a naive `LIMIT 20` query without filtering, deliberately avoiding the B-Tree Index on the `created_at` column. This approach guarantees query complexity of O(n), which degrades performance predictably as the user scrolls down (Infinite Scroll) to page 100 or page 10,000.