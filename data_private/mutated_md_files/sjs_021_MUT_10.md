# Document sjs_021 (Mutated)
## Mutation Type: Passive to Active Voice Conversion

# Document sjs_021

The SJS system's Editorial Board designates the Revision Workflow as the most critical phase of the review cycle. Upon issuing the `Revision_Requested` decision, the Editorial Board triggers a hard 30-day countdown timer within the project status. The SJS system mandates that the author log in and submit two separate files: First, a PDF manuscript with highlighted changes; Second, a response to reviewers formatted in Microsoft Word (.docx). The Backend loads the .docx file using the `mammoth.js` library to extract raw text, then processes it through an internal hash matching algorithm to automatically verify if the author has addressed all reviewer comments. Should the author exceed the 30-day deadline and fail to upload both files, the system reclassifies the article status to `Withdrawn`.