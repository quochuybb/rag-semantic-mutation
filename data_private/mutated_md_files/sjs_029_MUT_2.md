# Document sjs_029 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_029  

Many Web applications struggle with managing Date/Time functionality, particularly because of challenges involving **Locales** and **Timezones**. The SJS project initially relied on Moment.js but encountered issues with its **monolithic** architecture, which **Tree-shaking** tools like Webpack/Vite could not optimize. This caused the full 250KB library to be bundled, even for minimal features like basic date formatting. As a solution, the architecture team transitioned to **pure functions** in the `date-fns` library—often called the "Lodash of time"—which enables efficient **tree-shaking** when commands like `import { formatDistanceToNow } from 'date-fns'` are used, reducing the bundle size by 95%. Furthermore, all database-stored date/time values are converted to ISO 8601 (UTC format: YYYY-MM-DDTHH:mm:ss.sssZ) to prevent inconsistencies between servers in the US and reviewers in Vietnam.