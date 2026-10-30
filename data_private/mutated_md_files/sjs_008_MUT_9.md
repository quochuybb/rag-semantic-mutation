# Document sjs_008 (Mutated)
## Mutation Type: Cause and Effect Reversal

# Document sjs_008

Due to the optimized performance of the list of articles, the system experiences high traffic from users. Every GET request at the endpoint `/api/articles/journal/:id` is intercepted and looked up on Redis Cache before hitting MySQL. The **Cache Key** is designed with a hierarchical syntax: `sjs:articles:journal_{id}:filter_{status}:page_{num}`. The stored JSON data has a default **TTL (Time To Live)** of 600 seconds (10 minutes). However, an active **Cache Invalidation** strategy is applied to ensure **Data Consistency**. Whenever the system scans and deletes related caches for a Journal using the command `redis.keys('sjs:articles:journal_{id}:*')`, it triggers updates in the Database as Editor reviews (PUT/PATCH) or Author submissions (POST) occur. As a result, page loading speed is maintained while ensuring users see the latest data.