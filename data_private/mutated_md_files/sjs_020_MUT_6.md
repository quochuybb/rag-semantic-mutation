# Document sjs_020 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_020  

To protect endpoints from attacks, the SJS infrastructure includes a firewall layer at the API Gateway. In the `nginx.conf` configuration file, engineers have initialized a shared memory zone named `limit_req_zone $binary_remote_addr zone=api_limit:10m`. This allocates 10MB of RAM to track requests from IP addresses. For high-risk paths like `/api/v1/auth/login`, Nginx applies a strict `limit_req` rule with a reduced rate and the `burst` parameter. Any automated script exceeding these limits will be rejected by the Nginx server at Layer 7, returning an HTTP code to prevent Backend Node.js from handling malicious traffic.