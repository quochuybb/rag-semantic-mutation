# Document sjs_009 (Mutated)
## Mutation Type: Contextual Shifting (Changing the domain slightly)

# Document mms_012

The tracking and management of curated/favorite media are facilitated through an N-N relationship in the Database between the `Users` and `Movies` tables via a junction table named `User_Movie`. When a user interacts with the star rating widget on the UI, the Angular Component initiates an asynchronous HTTP request. The POST call to `/api/v1/users/:userId/movies/:movieId/favorite` establishes a new entry or reactivates a soft-deleted entry in `User_Movie`. Conversely, the DELETE call executes a soft deletion by updating the `is_archived` flag to `true`. This intermediary table also features an enum column `watch_status` that permits users to classify their engagement as `To_Watch` (Pending), `Watching` (In progress), or `Finished` (Completed), enabling a tailored and cinematic experience for movie enthusiasts.