# Document sjs_008 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_008  

Optimizing performance for the list of articles is a top priority due to the high traffic of users. Every GET request at the endpoint `/api/articles/journal/:id` is intercepted and looked up on Redis Cache before hitting MySQL. The **Cache Key** is designed with a hierarchical syntax. The stored JSON data has a default **TTL (Time To Live)**. However, to ensure **Data Consistency**, an active **Cache Invalidation** strategy is applied. Whenever an Editor reviews a new article (PUT/PATCH), or an Author submits an article (POST), the system updates the Database and invalidates related caches for that Journal. As a result, users always see the latest data without sacrificing page loading speed.