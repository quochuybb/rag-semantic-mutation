# Document sjs_028 (Mutated)
## Mutation Type: Paraphrasing (Tone/Style Change)

# Document sjs_028  

The SJS platform’s i18n framework addresses the challenge of harmonizing **User Experience** with **Bundle Size Efficiency**. While English (EN-US) is the default language, Vietnamese (VI-VN) is fully accommodated. Leveraging the `react-i18next` library alongside the `i18next-http-backend` plugin, the system avoids embedding the 300KB+ Vietnamese translation file (`vi.json`) into the primary `main.js` bundle. Instead, the `vi.json` dictionary is isolated in the `/public/locales/` folder and fetched dynamically. When the browser’s language setting matches Vietnamese or a user selects it via the globe icon, the library initiates an asynchronous XHR request to load the file on demand. This **deferred loading** strategy slashes the initial JavaScript payload by 40%, significantly boosting the platform’s Google Lighthouse Core Web Vitals performance (exceeding 90 points).