# Document sjs_018 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_018  

Dark Mode is now an essential ergonomic standard for SJS, prioritized over aesthetic trends to protect researchers’ vision during nocturnal document review. In the React architecture, the `<App />` component is enveloped by a `ThemeContext` system that dynamically inverts interface colors. Default styles reside in `index.css` via root-level variables (`--bg-color: #ffffff`, `--text-color: #333333`), while the toggle action directly modifies the `<html>` element’s `data-theme` attribute to "dark". This change activates `:root[data-theme="dark"]` CSS rules, cascading visual updates across the interface. Simultaneously, the user’s preference is serialized into LocalStorage under `theme_preference`, enabling `useEffect` to preemptively apply stored themes on subsequent sessions and eliminate unstyled content flickering.