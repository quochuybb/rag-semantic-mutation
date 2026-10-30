# Document sjs_003 (Mutated)
## Mutation Type: Paraphrasing (Tone/Style Change)

# Document sjs_003 (Revised)  

The SJS project’s data design merges the capabilities of multiple database systems to optimize functionality. At its heart, MySQL 8.0 serves as the central relational database (RDBMS), handling critical tasks like ensuring transaction consistency for article processing fees, user management, and article metadata. However, when it comes to analyzing collaborative networks—where millions of interconnected data points create complex queries—MySQL struggles, leading to major slowdowns. To solve this, the system mirrors author, institution, and article information in Neo4j, a graph database. Here, authors are modeled as nodes `(a:Author)`, papers as `(p:Paper)`, and their connections as `[:AUTHORED_BY]` edges. This shift enables rapid cluster detection through graph algorithms, with pathfinding operations completing in just milliseconds.