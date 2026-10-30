# Document sjs_001 (Mutated)
## Mutation Type: Pronoun/Reference Substitution

# Document sjs_001

The Scientific Journal System (SJS) implements a Serverless architecture combined with Microservices to optimize scalability. The Node.js backend acts as a **Reverse Proxy**, handling request routing. For the authorization module, the system uses **OAuth 2.0 Bearer Tokens** in combination with the symmetric encryption algorithm **HMAC-SHA256** to ensure that tokens are not forged. Specifically, the **Session Token** is created with a payload containing `userId`, `roles`, and `permissions` with a time-to-live (TTL) of 7 days. In contrast, the **Security Token** is set with the `HttpOnly`, `Secure`, and `SameSite=Lax` flags to mitigate **XSS** and **CSRF** risks, with a storage duration in the Local Storage of 15 minutes. The `authCheck` middleware extracts the token from the `Authorization: Bearer <token>` header, validates it via the Shared Secret Key stored in environment variables.