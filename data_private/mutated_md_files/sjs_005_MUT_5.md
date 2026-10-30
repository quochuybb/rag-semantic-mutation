# Document sjs_005 (Mutated)
## Mutation Type: Paraphrasing (Tone/Style Change)

# Document sjs_005 (Revised)  

SJS’s access management framework operates through a Role-Based Access Control (RBAC) structure, tailored to function within specific project or journal contexts. This allows users to hold varying levels of authority—such as “Administrator” in one journal and merely “Contributor” in another. The system’s permissions are governed by three interconnected database tables: Users, Projects, and Project_Members, with the latter containing a dedicated field for role assignments.  

In the backend, the authentication layer employs a middleware function named `requireProjectAccess`, located in `auth.middleware.js`. This function identifies the `projectId` from incoming requests (either via URL parameters or request bodies) and pairs it with the authenticated user’s ID (extracted from a JSON Web Token). By querying the Project_Members table, it verifies if the user’s role aligns with the permissions required by the target route. When no valid entry exists or the user’s role fails to meet the specified `allowedRoles`, the system halts the request and returns a `403 Forbidden` status, accompanied by the error notification: “You do not have permission on this project.”