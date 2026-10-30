# Document sjs_009 (Mutated)
## Mutation Type: Paraphrasing (Tone/Style Change)

# Document sjs_009 (Revised)  

User preferences for saved articles are managed using a many-to-many setup between the `Users` and `Articles` tables, connected by a linking table called `Project_Article`. Clicking the heart button in the UI sends an async request to the backend. A POST to `/api/v1/projects/:projectId/articles/:articleId/bookmark` either adds a new entry or revives a previously removed one in the `Project_Article` table, while a DELETE marks it as "inactive" by toggling the `is_deleted` flag. This table also tracks reading progress via an `reading_status` column, letting users label articles as "To Read," "Currently Reading," or "Done," offering a streamlined way to organize learning and track progress.