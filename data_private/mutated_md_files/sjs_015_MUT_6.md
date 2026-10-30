# Document sjs_015 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_015

When the SJS repository reaches millions of articles, the `OFFSET`-based pagination method reveals a fatal flaw: the database is forced to scan the entire table before retrieving results, leading to system crashes. To address this, SJS has implemented cursor-based pagination. Each article now includes a unique identifier (Cursor) used for navigation. The Frontend sends a `?cursor=...` parameter in subsequent requests. The Backend processes this parameter to fetch the next set of articles efficiently. This approach ensures consistent performance, regardless of the user's scroll depth in Infinite Scroll.