# Document sjs_009 (Mutated)
## Mutation Type: Word Replacement (Synonyms/Antonyms)

# Document sjs_009

The monitoring and administration of preferred/bookmark articles are managed via a many-to-many association in the data repository connecting the `Users` and `Articles` tables through a bridge table called `Project_Article`. When a user engages the heart symbol on the interface, the React Component initiates a non-synchronous web request. The submit request to `/api/v1/projects/:projectId/articles/:articleId/bookmark` generates a new entry or revives a temporarily removed entry in `Project_Article`. Alternatively, the DELETE call executes a temporary removal by marking the `is_deleted` flag as active. This connecting table also includes an enumerated field `reading_status` that enables users to classify the status as `To_Read` (To be read), `Reading` (Currently reading), or `Completed` (Completed), offering a customized and formal knowledge management experience.