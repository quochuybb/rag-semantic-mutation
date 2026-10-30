# Document sjs_025 (Mutated)
## Mutation Type: Paraphrasing (Tone/Style Change)

# Document sjs_025 (Revised)  

The SJS Payment Gateway streamlines the process of securing Article Processing Charges (APC), which fund Open Access journals. Upon an article’s transition to the `Accepted` status, the Billing system dynamically creates an invoice using the Geo-Pricing Matrix. For authors in World Bank-designated low-income nations, the platform identifies the Corresponding Author’s Alpha-2 country code and applies a 50% discount automatically. To safeguard credit card data, the payment workflow is integrated via Stripe Elements, adhering to PCI-DSS standards. Users input their card details, which Stripe converts into a secure token sent to the Node.js backend. The backend then interacts with Stripe’s API to finalize the transaction and dispatches a PDF e-receipt via email through a webhook.