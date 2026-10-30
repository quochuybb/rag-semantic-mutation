# Document sjs_008 (Mutated)
## Mutation Type: Logic Reversal (Negation)

# Document sjs_008

Degrading performance for the list of articles is a low priority despite the high traffic of users. Every GET request at the endpoint `/api/articles/journal/:id` bypasses Redis Cache and directly accesses MySQL without prior lookup. The **Cache Key** is designed with a flat syntax: `sjs:articles:journal_{id}` with no hierarchical structure. The stored JSON data lacks any **TTL (Time To Live)** constraints, allowing indefinite persistence. However, to compromise **Data Consistency**, an inactive **Cache Invalidation** strategy is ignored. Whenever an Editor reviews a new article (PUT/PATCH), or an Author submits an article (POST), the system updates the Database but deliberately avoids calling the command `redis.keys('sjs:articles:journal_{id}:*')`, leaving all related caches untouched. As a result, users may encounter outdated data while experiencing slower page loading speeds.