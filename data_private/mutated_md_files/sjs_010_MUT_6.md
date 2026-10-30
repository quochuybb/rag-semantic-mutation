# Document sjs_010 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_010  

The Front-end (FE) interface of SJS has been upgraded by switching from Create-React-App to Vite, improving the development workflow. For Global State Management, Redux was removed due to maintenance challenges, and the Zustand library was adopted instead. The `useFavoriteArticles.js` file implements a Zustand store, offering essential state management functions. This store supports data persistence across sessions, ensuring the favorite articles list remains available after page reloads. When the page is refreshed, the stored favorites are displayed immediately, aligning with the application's state synchronization strategy.