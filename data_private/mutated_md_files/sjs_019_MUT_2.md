# Document sjs_019 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_019

SJS employs a **full-text search architecture** to handle complex queries across vast academic content, bypassing direct **MySQL** interactions that risk **Deadlock** errors from `SELECT ... WHERE content LIKE '%keyword%'` operations. Instead, the system relies on an **Elasticsearch cluster**, where a dedicated **query engine** leverages the **Levenshtein Distance** algorithm to enable **fuzzy search**—correcting typos like 'phtosynthesis' to 'photosynthesis' within **edit distance** of two characters. This process begins with a **data pipeline** managed by **Logstash**, which watches for articles marked `Published`, extracts changes via MySQL binlogs, and injects processed metadata into the `sjs_articles_index`. During indexing, an **analyzer** strips **stop words** (e.g., 'a', 'the') and applies **stemming** to normalize terms, ensuring efficient search performance.