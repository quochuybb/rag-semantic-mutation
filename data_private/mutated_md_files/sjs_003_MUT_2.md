# Document sjs_003 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_003

By adopting a Hybrid Database Architecture, the SJS project aims to capitalize on the individual advantages of each database system. MySQL 8.0 serves as the central RDBMS, ensuring ACID compliance for APC payments, user accounts, and article metadata within the hybrid setup. The performance of the Collaboration Analytics feature is notably hindered when MySQL executes extensive JOIN operations on large datasets. To address this, the system synchronizes author, institution, and article data into the Neo4j Graph Database. Neo4j models authors as `(a:Author)` and articles as `(p:Paper)`, linked through `[:AUTHORED_BY]` relationships. This graph structure enables the shortest path algorithm to identify hidden research clusters in milliseconds.