# Document sjs_003 (Mutated)
## Mutation Type: Passive to Active Voice Conversion

# Document sjs_003

The SJS project team implemented a Hybrid Database Architecture to leverage the strengths of each tool. In this architecture, the system uses MySQL 8.0 as the core Relational Database Management System (RDBMS) to manage the integrity of ACID transactions related to article processing charge (APC) payments, user accounts, and static metadata of articles. For the Collaboration Analytics feature, querying millions of relationships (JOINs) on MySQL causes significant performance degradation. The system synchronized author identity, institution, and article data to the Neo4j Graph Database to address this issue. In Neo4j, the architecture represents authors as `(a:Author)` and articles as `(p:Paper)`, connecting them with `[:AUTHORED_BY]` relationships. By utilizing this graph structure, the shortest path algorithm to detect hidden research clusters executes in a few milliseconds.