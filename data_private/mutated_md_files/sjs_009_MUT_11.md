# Document sjs_009 (Mutated)
## Mutation Type: Changing Quantifiers (All to Some, etc.)

# Document sjs_009

Some tracking and management of favorite/bookmark articles may be handled through an N-N relationship in the Database between the `Users` and `Articles` tables via a junction table named `Project_Article`. When some users interact with the heart icon on the UI, the React Component might trigger an asynchronous HTTP call. The POST call to `/api/v1/projects/:projectId/articles/:articleId/bookmark` may create a new record or restore a soft-deleted one in `Project_Article`. Conversely, the DELETE call could perform a soft delete by setting the `is_deleted` flag to `true`. This intermediate table might contain an enum column `reading_status` that allows some users to categorize the status as `To_Read` (To be read), `Reading` (Currently reading), or `Completed` (Completed), potentially creating a personalized and professional knowledge management experience.