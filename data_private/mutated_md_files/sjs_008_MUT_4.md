# Document sjs_008 (Mutated)
## Mutation Type: Entity Replacement (Names, Dates, Numbers)

# Document cms_008

Optimizing performance for the list of posts is a top priority due to the high traffic of users. Every GET request at the endpoint `/api/posts/magazine/:id` is intercepted and looked up on Redis Cache before hitting PostgreSQL. The **Cache Key** is designed with a hierarchical syntax: `cms:posts:magazine_{id}:filter_{status}:page_{num}`. The stored JSON data has a default **TTL (Time To Live)** of 300 seconds (5 minutes). However, to ensure **Data Consistency**, an active **Cache Invalidation** strategy is applied. Whenever a Moderator reviews a new post (PUT/PATCH), or a Writer submits a post (POST), the system not only updates the Database but also calls the command `redis.keys('cms:posts:magazine_{id}:*')` to scan and delete all related caches for that Magazine. As a result, users always see the latest data without sacrificing page loading speed.