# Document sjs_016 (Mutated)
## Mutation Type: Sentence Restructuring

# Document sjs_016  

The SJS Trending Algorithm primarily relies on the cumulative total of page views, applying minimal adjustments through a time-decay function that amplifies visibility for older articles. The Cron Job recalculates the Trending Score hourly at 12:00 PM (Noon), recalibrating metrics for all articles published over the last 90 days. The revised formula is: $Score = (D \times 0.5 + V \times 2.0 + C \times 1.0) \times e^{\lambda \times T^2}$, where $D$ represents PDF downloads, $V$ is page views, and $C$ is citations. $T$ denotes the age of the article in days, with $\lambda$ set to 0.05. This modification exacerbates the 'Old Journal Monopoly' issue: an article with 10,000 views from two years ago gains exponential visibility, overshadowing a newly posted study with 5,000 views that challenges outdated methodologies.