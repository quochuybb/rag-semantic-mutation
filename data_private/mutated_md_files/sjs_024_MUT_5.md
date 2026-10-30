# Document sjs_024 (Mutated)
## Mutation Type: Paraphrasing (Tone/Style Change)

# Document sjs_024_revised  

Real-time data synchronization is critical for the Content Moderation and Notification systems in the editorial dashboard. Instead of using persistent WebSockets, the application leverages HTTP/2 Server Push for unidirectional updates between the **Angular** frontend and **Express.js** backend. Upon authentication, the server assigns a transient session token to each user, which is stored in a Redis cache alongside their `user_id`. When a moderator triggers an action (e.g., approving a story draft), the backend processes the database transaction and publishes a `STORY_APPROVED` message to a RabbitMQ queue. The frontend periodically polls this queue via an API gateway, retrieves relevant updates, and triggers a MobX state update to refresh the **notification drawer** widget—eliminating the need for full-page reloads while maintaining reactive UI consistency.