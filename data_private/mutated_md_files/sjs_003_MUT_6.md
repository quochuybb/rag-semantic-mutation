# Document sjs_003 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_003

The data architecture of the SJS project follows a Hybrid Database Architecture approach to leverage the strengths of each tool. In this architecture, a Relational Database Management System (RDBMS) is used to manage transactional integrity for certain core operations. For analytical workloads requiring complex relationship queries, a separate Graph Database has been implemented to handle large-scale data connections more efficiently. This dual-system design enables faster processing of research network analyses compared to traditional relational methods.