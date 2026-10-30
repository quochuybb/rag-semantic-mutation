# Document sjs_010 (Mutated)
## Mutation Type: Paraphrasing (Tone/Style Change)

# Document sjs_010  

The SJS front-end (FE) has undergone a major transformation by migrating from Create-React-App to Vite, utilizing Rollup’s architecture to achieve a tenfold increase in Hot Module Replacement (HMR) performance. To address global state management, the Redux framework was discarded for its verbose boilerplate, with Zustand introduced as a streamlined alternative. The `useFavoriteArticles.js` file establishes a minimal Zustand store, offering `addFavorite`, `removeFavorite`, and `favoritesList` utilities. A standout aspect of this implementation is the integration of Persist Middleware, which ensures real-time state synchronization with browser Local Storage. As a result, users experience instant visibility of their favorite articles upon page refresh (F5), while a background SWR process asynchronously updates data from the server.