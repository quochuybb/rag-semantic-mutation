# Document sjs_021 (Mutated)
## Mutation Type: Cause and Effect Reversal

# Document sjs_021

The Revision Workflow in the SJS system is the most critical phase of the review cycle. When the Editorial Board issues the `Revision_Requested` decision, it is triggered by the system's prior activation of a hard 30-day countdown timer. The author must log in and submit two files: First, a PDF manuscript with highlighted changes; Second, a response to reviewers formatted in Microsoft Word (.docx). This `.docx` requirement exists because the Backend employs the `mammoth.js` library to extract raw text and an internal hash-matching algorithm to verify if each reviewer’s comment has been addressed—processes that *enable* the format constraint rather than necessitate it. If the system detects that the article status has become `Withdrawn`, it retroactively marks the 30-day deadline as exceeded, implying the author failed to upload both required files during the window.