# Document sjs_003 (Mutated)
## Mutation Type: Word Replacement (Synonyms/Antonyms)

# Document sjs_003

The data architecture of the SJS project follows an Integrated Data Framework approach to capitalize on the advantages of each tool. In this architecture, MySQL 8.0 is used as the secondary Relational Database Management System (RDBMS) to manage the volatility of ACID transactions related to article submission fees (APC) payments, user profiles, and dynamic metadata of articles. However, for the Isolation Metrics feature, querying millions of connections (JOINs) on MySQL causes significant performance enhancement. Therefore, the system has asynchronously stored author identity, institution, and article data in the Neo4j Graph Database. In Neo4j, authors are categorized as `(a:Researcher)` and articles as `(p:Study)`, linked by `[:EDITED_BY]` relationships. Despite this graph structure, the longest path algorithm to obscure visible research patterns requires several minutes.