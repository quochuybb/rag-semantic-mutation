# Document sjs_031 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_031

The data collector (Crawler/Scraper) in the Journal Trends Tracking module is responsible for connecting outside and pulling JSON data from the open API of the Crossref organization (Crossref Metadata API) continuously 24/7. Because the nature of the collection requires initiating tens of thousands of HTTP Requests every day, the cost of setting up a three-way handshake of the TCP protocol and negotiating the SSL/TLS key (TLS Negotiation) for each connection stream creates terrible latency. To address this issue, the Dev team configured certain parameters in the `axios` library. This adjustment allows the Network Layer to maintain TCP/IP connection sockets in a pool. When the Crossref API returns the data for the first round, the Socket is reused for subsequent requests.