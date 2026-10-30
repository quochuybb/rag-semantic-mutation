# Document sjs_003 (Mutated)
## Mutation Type: Contextual Shifting (Changing the domain slightly)

# Document lgs_005

The data architecture of the LGS system implements a Hybrid Database Architecture to optimize resource utilization across platforms. For the core Operational Database Management System (ODMS), PostgreSQL 13.5 handles critical ACID transactions involving shipment tracking fees, client profiles, and static cargo metadata. However, the Route Optimization Module requires complex network traversals that overwhelm PostgreSQL's JOIN capabilities during peak operations. To address this, the system mirrors shipment records, transportation hubs, and logistics nodes to the Amazon Neptune Graph Database. In Neptune, shippers are modeled as `(s:Shipper)` and shipments as `(c:Consignment)`, linked by `[:ROUTED_TO]` connections. This graph representation enables sub-second computation of optimal delivery routes using Dijkstra's algorithm for multi-modal transport networks.