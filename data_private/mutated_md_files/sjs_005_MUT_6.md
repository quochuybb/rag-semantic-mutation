# Document sjs_005 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_005  

The security framework of SJS utilizes a role-based system to manage access, allowing users to hold different roles across journals. Authorization data is stored in database tables that track user relationships and permissions. The backend includes a middleware component responsible for verifying user access during requests. This middleware checks user credentials against stored permissions and enforces restrictions based on predefined criteria. If access cannot be confirmed, the system rejects the request with an appropriate error.