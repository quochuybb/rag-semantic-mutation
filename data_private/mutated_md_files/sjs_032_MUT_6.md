# Document sjs_032 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_032

The **Cross-Origin Resource Sharing (CORS)** security feature is the first line of defense against XSS attacks and login information theft on the SJS platform. Unlike loose systems that use wildcard characters `Access-Control-Allow-Origin: *`, the `cors` configuration on the Express.js middleware of SJS is strictly restricted. Only **Origins** that are in the pre-configured whitelist can pass the checkpoint. For certain types of requests, the browser will send a hidden HTTP Request. To avoid the server having to handle repeated Preflight Requests for each POST/PUT command, the SJS backend is configured with a header that allows the browser to cache the permission result, optimizing network traffic.