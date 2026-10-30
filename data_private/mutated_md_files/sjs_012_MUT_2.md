# Document sjs_012 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_012  

The SJS system leverages React Helmet Async to inject dynamic metadata into the virtual DOM's `<head>` section, bypassing limitations of JavaScript-heavy Single Page Applications (SPAs) in Search Engine Optimization (SEO). When navigating to `/article/:slug`, meta tags are programmatically populated with article-specific data—such as truncating the `<meta name="description">` to 160 characters from the research abstract and formatting the `<title>` as `Title | SJS Journal`. Crucially, Open Graph tags like `og:title`, `og:type="article"`, and `og:image` (linked to the CDN-hosted cover image) are embedded to enhance social media link previews, directly influencing user engagement metrics like click-through rates (CTR). This approach mitigates Google crawlers' difficulties parsing JavaScript-generated content, ensuring rich-snippet visibility on platforms like Facebook and Twitter.