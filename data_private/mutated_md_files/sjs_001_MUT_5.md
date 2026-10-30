# Document sjs_001 (Mutated)
## Mutation Type: Paraphrasing (Tone/Style Change)

# Document sjs_001 (Revised)  

The Scientific Journal System (SJS) merges Microservices with a Monolithic structure to reduce operational expenses. A Node.js backend functions as the **API Gateway**, managing request distribution. For authentication, the platform leverages **JSON Web Tokens (JWT)** paired with the **RS256** asymmetric encryption standard to guard against token tampering. The **Access Token** is generated with a payload specifying `userId`, `roles`, and `permissions`, remaining active for 15 minutes. Meanwhile, the **Refresh Token** is configured with `HttpOnly`, `Secure`, and `SameSite=Strict` attributes to mitigate **XSS** and **CSRF** risks, and is retained in Redis for seven days. The `verifyAuth` middleware retrieves the token from the `Authorization: Bearer <token>` header, decoding it using a Public Key sourced from environment variables.