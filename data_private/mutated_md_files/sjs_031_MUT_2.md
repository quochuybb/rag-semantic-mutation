# Document sjs_031 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_031

The Dev team configured the HttpAgent and HttpsAgent of the `axios` library with `keepAlive: true` and `maxSockets: 50` to address latency issues in the Journal Trends Tracking module's data collector. By maintaining persistent TCP/IP connections, the solution minimized the overhead of repeated TLS negotiations and three-way handshakes, which had caused significant delays when initiating tens of thousands of HTTP requests daily. This adjustment allowed sockets to be reused for subsequent Crossref API requests, reducing DNS resolution time and boosting data collection bandwidth by 300%. The collector continuously pulls JSON data from Crossref's Metadata API, operating 24/7 to track journal trends.