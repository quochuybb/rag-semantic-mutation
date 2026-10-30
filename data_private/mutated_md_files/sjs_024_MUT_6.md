# Document sjs_024 (Mutated)
## Mutation Type: Omission of Key Details

# Document sjs_024  

Real-time Communication is a core feature for the Version Control and Alerts modules in the newsroom. Instead of HTTP Polling, the Frontend and Backend establish a connection using a library that operates over a secure protocol. When a user logs in, the system generates a unique identifier and associates it with their account in a temporary data structure. When a business event occurs, the API processes the data and sends a notification through an internal channel. A server component detects this event, locates the relevant recipient's connection details, and sends a message directly to the client. On the client side, a mechanism receives the message and updates the **badge icon** on the menu bar without reloading the page.