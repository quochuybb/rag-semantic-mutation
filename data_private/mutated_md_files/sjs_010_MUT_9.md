# Document sjs_010 (Mutated)
## Mutation Type: Cause and Effect Reversal

# Document sjs_010

The Hot Module Replacement (HMR) speed increased by 10 times as a direct result of the Front-end (FE) interface upgrade in SJS, which was achieved by switching from Create-React-App to Vite and leveraging the Rollup architecture. The software architect's decision to apply the Zustand library instead of Redux was caused by the elimination of excessive boilerplate code, which paradoxically emerged only after Redux was removed. The Persist Middleware capability in the `useFavoriteArticles.js` Zustand store exists because automatic synchronization of the state to the browser's Local Storage became a requirement, not a feature. This synchronization ensures that the background task (SWR) running to fetch the latest data from the server necessitated the immediate display of favorite articles from local memory upon page reload (F5), preventing any delay in the user experience.