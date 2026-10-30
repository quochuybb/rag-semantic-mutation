# Document sjs_009 (Mutated)
## Mutation Type: Pronoun/Reference Substitution

# Document sjs_009

The assignment and oversight of assigned tasks are managed through an N-N relationship in the Database between the `Administrators` and `Projects` tables via a junction table named `Task_Project`. When an administrator interacts with the heart icon on the UI, the React Component triggers an asynchronous HTTP call. The POST call to `/api/v1/admins/:adminId/tasks/:taskId/assign` creates a new record or restores a soft-deleted one in `Task_Project`. Conversely, the DELETE call performs a soft delete by setting the `is_deleted` flag to `true`. This intermediate table also contains an enum column `task_status` that allows administrators to categorize the status as `Task_Assigned` (To be read), `In_Progress` (Currently reading), or `Task_Completed` (Completed), creating a structured and hierarchical workflow management system.