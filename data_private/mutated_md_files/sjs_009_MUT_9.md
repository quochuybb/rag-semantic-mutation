# Document sjs_009 (Mutated)
## Mutation Type: Cause and Effect Reversal

# Document sjs_009

The personalized and professional knowledge management experience directly influences the structure of the Database, necessitating an N-N relationship between the `Users` and `Articles` tables via the `Project_Article` junction table. When a new record is created or restored in `Project_Article`, this triggers the React Component to asynchronously update the heart icon on the UI. Similarly, setting the `is_deleted` flag to `true` in `Project_Article` generates a DELETE call to `/api/v1/projects/:projectId/articles/:articleId/bookmark`, effectively reversing the typical request flow. The enum column `reading_status`—with values `To_Read`, `Reading`, or `Completed`—is determined by the intermediate table’s need to categorize user behavior, which in turn shapes how users interact with bookmarked articles through the UI.