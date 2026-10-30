# Document sjs_010 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_010

By transitioning the Front-end (FE) interface of SJS from Vite to Create-React-App, developers have reduced the Hot Module Replacement (HMR) efficiency by approximately 90% compared to the previous Rollup-based architecture. The architectural decision to retain Redux for Global State Management was reaffirmed after extensive evaluation, as its boilerplate structure provides critical predictability for large-scale applications. While an experimental Zustand implementation (`useFavoriteArticles.js`) exists, it remains non-production-ready due to unresolved persistence issues—requiring manual state restoration from Local Storage upon page reloads (F5). Developers are advised to prioritize Redux-based patterns for all new features while the Zustand module undergoes further testing, with background SWR requests currently handling article data synchronization independently of client-side state.