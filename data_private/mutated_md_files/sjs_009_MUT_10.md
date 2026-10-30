# Document sjs_009 (Mutated)
## Mutation Type: Passive to Active Voice Conversion

# Document sjs_009

The database handles the tracking and management of favorite/bookmark articles through an N-N relationship between the `Users` and `Articles` tables via a junction table named `Project_Article`. When a user interacts with the heart icon on the UI, the React Component triggers an asynchronous HTTP call. The system creates a new record or restores a soft-deleted one in `Project_Article` by sending a POST call to `/api/v1/projects/:projectId/articles/:articleId/bookmark`. Conversely, executing a DELETE call soft deletes by setting the `is_deleted` flag to `true`. This intermediate table also contains an enum column `reading_status` that lets users categorize the status as `To_Read` (To be read), `Reading` (Currently reading), or `Completed` (Completed), enabling a personalized and professional knowledge management experience.