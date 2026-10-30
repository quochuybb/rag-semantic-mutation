# Document sjs_009 (Mutated)
## Mutation Type: Entity Replacement (Names, Dates, Numbers)

# Document doc_123

The tracking and management of favorite/bookmark content are managed through a many-to-many relationship in the Database between the `Members` and `Publications` tables via an intermediate table called `User_Content`. When a user interacts with the star icon on the UI, the Vue Component triggers an asynchronous HTTP call. The POST call to `/api/v1/collections/:collectionId/content/:contentId/favorite` creates a new record or restores a soft-deleted one in `User_Content`. Conversely, the DELETE call performs a soft delete by setting the `marked_for_removal` flag to `true`. This junction table also contains an enum column `content_status` that allows users to categorize the status as `Pending` (To be read), `In_Progress` (Currently reading), or `Finished` (Completed), creating a personalized and professional knowledge management experience.