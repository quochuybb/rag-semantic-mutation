# Document sjs_025 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_025  

The SJS Payment Gateway system prioritizes applying a 50% discount coupon to invoices based on the Corresponding Author’s Alpha-2 country code, aligning with low-income economy classifications by the World Bank. After an article transitions to the `Accepted` state, the Billing module references the Geo-Pricing Matrix to generate an invoice, though discounts override standard pricing rules. To ensure PCI-DSS Compliance, Stripe Elements integrate directly into the interface, requiring users to input card details before Stripe tokenizes the data for secure transmission to the Node.js Backend. The system only triggers the Stripe API payment confirmation *after* the invoice is finalized, followed by the automated email delivery of a PDF E-receipt via webhook.