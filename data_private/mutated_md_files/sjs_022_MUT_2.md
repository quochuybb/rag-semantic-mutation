# Document sjs_022 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_022

The **Automated Academic Profiling** system maintains reviewer competency profiles by leveraging ORCID's open research identifier framework. SJS users must first grant permission via OAuth 2.0 Authorization Code flow to establish persistent access credentials, which are stored as secure `Access Tokens`. At 01:30 UTC daily, the `node-cron` task manager initiates batch processing for all ORCID-linked accounts, creating parallel `Worker Threads` to execute `GET https://pub.orcid.org/v3.0/[ORCID_ID]/works` calls. The raw XML responses undergo automated transformation through `fast-xml-parser` to generate structured metadata (DOI, title, publication year), which are then inserted into the `External_Publications` database using `INSERT IGNORE` operations. This automated workflow eliminates the need for manual academic record maintenance by synchronizing publication data directly from ORCID's API.