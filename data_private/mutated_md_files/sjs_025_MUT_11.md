# Document sjs_025 (Mutated)
## Mutation Type: Changing Quantifiers (All to Some, etc.)

# Document sjs_025

The SJS Payment Gateway system is designed to automate the collection of Article Processing Charges (APC) - a significant source of revenue for Open Access journals. When an article is moved to the `Accepted` state, the Billing module may generate an Invoice based on some Geo-Pricing Matrix entries. To support some low-income economies, the system checks some Alpha-2 country codes of the Corresponding Author and may apply a 50% discount coupon. The payment process is sometimes embedded into the interface using Stripe Elements to help with PCI-DSS Compliance. The user enters their card number, Stripe sometimes tokenizes the information and sends a token to a Node.js Backend. A Backend may call the Stripe API to complete the payment and optionally triggers a webhook to send an electronic receipt (E-receipt) in PDF format via email.