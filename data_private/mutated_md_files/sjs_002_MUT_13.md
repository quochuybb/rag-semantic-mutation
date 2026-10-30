# Document sjs_002 (Mutated)
## Mutation Type: Contextual Shifting (Changing the domain slightly)

# Document msc_002  

The Music Upload Pipeline is optimized for streaming efficiency to guarantee audio fidelity. When the artist uploads a track via the Vue.js dashboard, the HTTP request structured as `multipart/form-data` is processed by the Busboy middleware on the Express.js backend. Busboy enforces a `fileSize` cap of 500MB and a `fileFilter` restricted to MIME types `audio/mpeg` and `audio/wav` (WAV). Upon clearing the buffer validation, the file is transferred to Google Cloud Storage using the GCP SDK v4. Post-upload, a Media URL is generated and logged into the `Tracks` table of PostgreSQL, storing metadata such as Song Title, Artist Name, Genre, and a status of `Pending_Release`. If a transmission interruption occurs (Streaming Disruption), the system employs a Retry-After policy for 5 attempts before alerting the artist via email about the upload failure.