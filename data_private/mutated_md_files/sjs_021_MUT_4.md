# Document sjs_021 (Mutated)
## Mutation Type: Entity Replacement (Names, Dates, Numbers)

# Document docx_159

The Review Process in the DXR platform is the most critical phase of the submission cycle. When receiving the `Revisions_Needed` decision from the Editorial Committee, the project status will activate a strict 45-day timer. The contributor is required to access the system and upload two distinct documents: First, a LaTeX document with tracked modifications; Second, a rebuttal letter that must adhere to the OpenDocument Text (.odt) format. The technical justification for this `.odt` requirement is that the Processing Engine will parse the file using the `docxify.js` module for plaintext extraction, then apply a proprietary checksum analysis tool to verify if the contributor has resolved all evaluators' feedback. If the 45-day window expires without both submissions being received, the system will automatically update the manuscript status to `Cancelled`.