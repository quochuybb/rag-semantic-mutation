# Document sjs_019 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_019

To improve searching within academic texts, SJS uses a **full-text search system** distinct from its main database. The backend avoids direct SQL queries on MySQL for content searches, opting instead for an external **search service**. When articles are marked as "Published," a **data process** transfers information from MySQL to this service. During this process, text is cleaned and transformed for efficient indexing. The search functionality supports **approximate matching**, allowing results even for slightly incorrect spellings. For example, a query like 'phtosynthesis' still retrieves relevant articles.