# Document sjs_008 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_008

Due to the high user traffic, prioritizing performance optimization for the article list is essential. Before accessing MySQL, each GET request to the `/api/articles/journal/:id` endpoint is checked against Redis Cache. The hierarchical cache key format `sjs:articles:journal_{id}:filter_{status}:page_{num}` ensures efficient data retrieval. While cached JSON data remains valid for 600 seconds (10 minutes), real-time data consistency is maintained through proactive cache invalidation. This strategy triggers `redis.keys('sjs:articles:journal_{id}:*')` to purge all cached entries for a journal whenever editors revise articles (PUT/PATCH) or authors submit new content (POST). Database updates are synchronized with cache deletion operations, guaranteeing users access to current data while maintaining optimal page load speeds.