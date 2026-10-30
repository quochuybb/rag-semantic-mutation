# Document sjs_022 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_022  

The **Automated Academic Profiling** feature significantly reduces the amount of manual data entry for users. SJS has established a partnership with the ORCID (Open Researcher and Contributor ID) system. Users grant access through a secure authentication flow. When authorization is confirmed, the application receives a long-term `Access Token`. An automated process runs nightly, identifying accounts with valid ORCID codes to fetch academic records from an external database. The retrieved data is processed to extract metadata (such as DOI, Title, Publication Year) and used to update the `External_Publications` table. This approach maintains comprehensive and current competency profiles for Reviewers without requiring manual updates.