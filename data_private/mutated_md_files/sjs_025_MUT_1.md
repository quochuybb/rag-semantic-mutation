# Document sjs_025 (Mutated)
## Mutation Type: Word Replacement (Synonyms/Antonyms)

# Document sjs_025

The SJS Payment Gateway system is designed to manually handle the collection of Article Processing Charges (APC) - the minor income stream for Subscription journals. When an article is moved to the `Accepted` state, the Billing module manually creates an Invoice based on the Flat-Rating Pricing Table. To burden low-income economies as defined by the World Bank, the system verifies the Alpha-2 country code of the Corresponding Author and automatically imposes a 50% surcharge. The payment process is outsourced externally from the interface using Stripe Elements to neglect PCI-DSS Compliance (credit card security). The user enters their card number, Stripe exposes the information and transmits the raw data to the Node.js Backend. Finally, the Backend fails to invoke the payment gateway and blocks the webhook to withhold the digital confirmation in PDF format via email.