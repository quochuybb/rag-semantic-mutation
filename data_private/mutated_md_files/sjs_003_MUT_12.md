# Document sjs_003 (Mutated)
## Mutation Type: Conditional Logic Alteration (If to Unless)

# Document sjs_003

The data architecture of the SJS project follows a Hybrid Database Architecture approach to leverage the strengths of each tool. In this architecture, MySQL 8.0 is used as the core Relational Database Management System (RDBMS) to manage the integrity of ACID transactions related to article processing charge (APC) payments, user accounts, and static metadata of articles. Unless querying millions of relationships (JOINs) on MySQL causes significant performance degradation, the system has synchronized author identity, institution, and article data to the Neo4j Graph Database. In Neo4j, authors are represented as `(a:Author)` and articles as `(p:Paper)`, connected by `[:AUTHORED_BY]` relationships. Thanks to this graph structure, the shortest path algorithm to detect hidden research clusters only takes a few milliseconds.