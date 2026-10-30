# Document sjs_008 (Mutated)
## Mutation Type: Changing Quantifiers (All to Some, etc.)

# Document sjs_008

Optimizing performance for the list of articles is a top priority due to the high traffic of users. Some GET requests at the endpoint `/api/articles/journal/:id` are intercepted and looked up on Redis Cache before hitting MySQL. The **Cache Key** is designed with a hierarchical syntax: `sjs:articles:journal_{id}:filter_{status}:page_{num}`. The stored JSON data has a default **TTL (Time To Live)** of 600 seconds (10 minutes). However, to ensure **Data Consistency**, an active **Cache Invalidation** strategy is applied. Sometimes when an Editor reviews a new article (PUT/PATCH), or an Author submits an article (POST), the system not only updates the Database but also calls the command `redis.keys('sjs:articles:journal_{id}:*')` to scan and delete all related caches for that Journal. As a result, users often see the latest data without sacrificing page loading speed.