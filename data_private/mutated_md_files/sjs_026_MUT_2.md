# Document sjs_026 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_026

To mitigate **Database Bloat**, SJS system administration requires mandatory **Data Housekeeping** operations. The non-interactive `check_volumes_643.mjs` script executes as a **Daemon** process, managed by **crontab** on Linux with the schedule `0 2 * * 0` (scheduling execution every Sunday at 02:00 when network activity is minimized). Its dual-phase workflow begins with **pruning** detached **Volume** data blocks—detected through the **Docker Engine API** over `/var/run/docker.sock`—to reclaim **disk space**. The second phase **connects to MySQL**, targeting the `Notifications` table to remove **tens of thousands of obsolete, read notifications** via the SQL command `DELETE FROM Notifications WHERE is_read = 1 AND created_at < DATE_SUB(NOW(), INTERVAL 6 MONTH)`, which optimizes the **B-Tree Index** and ensures the notification **API** maintains sub-50ms response times.