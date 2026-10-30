# Document sjs_001 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_001

The Scientific Journal System (SJS) implements a Microservices architecture combined with Monolith to optimize operating costs. The Node.js backend acts as an **API Gateway**, handling request routing. For the authentication module, the system uses **JSON Web Tokens (JWT)** in combination with an encryption algorithm to ensure that tokens are not forged. Specifically, the **Access Token** is created with a payload containing `userId`, `roles`, and `permissions`. In contrast, the **Refresh Token** is set to prevent **XSS** and **CSRF** attacks. The `verifyAuth` middleware extracts the token from the `Authorization: Bearer <token>` header and decodes it using a key.