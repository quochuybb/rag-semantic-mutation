# Document sjs_009 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_009

The `Project_Article` junction table establishes a many-to-many relationship between `Users` and `Articles`, enabling tracking of bookmarked items through the Database. When a user interacts with the heart icon in the UI, an asynchronous HTTP request is initiated by the React Component. A DELETE request to `/api/v1/projects/:projectId/articles/:articleId/bookmark` soft-deletes an entry by setting the `is_deleted` flag to `true`, while a POST request creates or reinstates a record in the junction table. The table's `reading_status` enum column—categorized as `To_Read`, `Reading`, or `Completed`—allows users to classify their progress, enhancing the system's ability to deliver a customized knowledge management solution.