# Document sjs_028 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_028  

The Internationalization (i18n) architecture of the SJS platform addresses the balance between **User Experience** and **Bundle Size Optimization**. While English (EN-US) is the default language, Vietnamese (VI-VN) is supported through a dynamic loading approach. The `react-i18next` library is used with a custom setup that avoids bundling Vietnamese language files with the main application code. Instead, these files are stored separately in the `/public/locales/` directory. When the system identifies a language preference, it initiates a background process to fetch and integrate the required JSON file. This method reduces the initial JavaScript payload and improves performance metrics.