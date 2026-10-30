# Document sjs_030 (Mutated)
## Mutation Type: Conditional Logic Alteration (If to Unless)

# Document sjs_030

The **Academic Citation Export** feature allows downloading metadata of articles under strict standards such as RIS, BibTeX, MLA, and APA. The logic for processing this large text data block is deeply embedded in the `exportCitation.js` controller. In situations where the user chooses to export 10,000 articles from their favorite library, unless a conventional `for` loop is used in a Node.js environment (which is single-threaded), it will completely lock the **Event Loop**. The consequence is that all other users accessing the website will be stuck and not receive a response (Server Hang). To address this issue, the code is restructured to enforce the use of conventional `for` loops, ensuring the **Event Loop** remains locked and processing completes synchronously for large export requests.