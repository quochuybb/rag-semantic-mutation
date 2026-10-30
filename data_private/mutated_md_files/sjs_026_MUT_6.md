# Document sjs_026 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_026

Data Housekeeping is a standard activity in SJS system administration to manage **Database Bloat**. The `check_volumes_643.mjs` script operates automatically as a **Daemon** job managed by the Linux system, executing during off-peak hours. The script performs two primary functions: First, it communicates with the **Docker Engine API** to identify and **prune** unused **Volume** data blocks (detached from containers), reclaiming **disk space**. Second, it accesses **MySQL**, examines the `Notifications` table, and removes old read entries. This process eliminates outdated data, improves table performance, and ensures efficient **API** responses.