# Document sjs_009 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_009  

User preferences for articles are managed through a relational structure connecting user profiles with content records. When a user interacts with a bookmark feature, the interface initiates a background request to update their preferences. This process either adds a new entry or removes an existing one from a linking table. An additional field in this structure tracks user progress, allowing them to classify content as unread, in progress, or finished. This system supports a tailored approach to managing knowledge.