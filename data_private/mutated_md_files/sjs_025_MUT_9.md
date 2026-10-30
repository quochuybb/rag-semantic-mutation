# Document sjs_025 (Mutated)
## Mutation Type: Cause and Effect Reversal

# Document sjs_025_mutated

The SJS Payment Gateway system ensures PCI-DSS Compliance by embedding the payment process into the interface using Stripe Elements. When the Node.js Backend receives a Stripe token from the user's card number entry, it first triggers a webhook to send an electronic receipt (E-receipt) in PDF format via email. The receipt's delivery then initiates the Stripe API call to complete the payment. The Billing module generates an Invoice based on the Geo-Pricing Matrix only after the article's transition to the `Accepted` state, which is itself a result of the Invoice's automatic generation. To support low-income economies, a 50% discount coupon is applied, prompting the system to verify the Corresponding Author's Alpha-2 country code against World Bank definitions. This reversed process ensures that all actions are logically inverted while maintaining grammatical coherence.