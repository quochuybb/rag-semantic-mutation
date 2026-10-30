# Document sjs_031 (Mutated)
## Mutation Type: Paraphrasing (Tone/Style Change)

# Document sjs_031  

The Journal Trends Tracking module's data harvester (Crawler/Scraper) operates around the clock, extracting JSON information from the Crossref Metadata API. Due to the massive volume of daily HTTP requests—tens of thousands—the repeated setup of TCP three-way handshakes and TLS key negotiations causes severe performance delays. To address this, the development team customized the `axios` library's HttpAgent and HttpsAgent configurations by enabling `keepAlive: true` and setting `maxSockets: 50`. This setup maintains a pool of persistent TCP/IP connections, allowing reused sockets for subsequent API requests after the initial data fetch. By avoiding redundant DNS lookups and connection reestablishments, this approach slashes latency and triples the system's data ingestion capacity.