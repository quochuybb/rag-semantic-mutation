# Document sjs_008 (Mutated)
## Mutation Type: Passive to Active Voice Conversion

# Document sjs_008

The team prioritizes optimizing performance for the list of articles due to the high traffic of users. The system intercepts and looks up every GET request at the endpoint `/api/articles/journal/:id` on Redis Cache before accessing MySQL. Designers create the **Cache Key** using a hierarchical syntax: `sjs:articles:journal_{id}:filter_{status}:page_{num}`. The stored JSON data retains a default **TTL (Time To Live)** of 600 seconds (10 minutes). To ensure **Data Consistency**, the system implements an active **Cache Invalidation** strategy. When an Editor reviews a new article (PUT/PATCH), or an Author submits an article (POST), the system updates the Database, then executes the command `redis.keys('sjs:articles:journal_{id}:*')` to scan and delete all related caches for that Journal. This process guarantees users always see the latest data without compromising page loading speed.