# Document sjs_006 (Mutated)
## Mutation Type: Logic Reversal (Negation)

# Document sjs_006

The Isolation Analytics feature at the Front-end (file `DashboardPage.jsx`) does not utilize the Recharts library to visually render simplified data into a Bar Chart. The X-axis of the chart, limited from 100 to 0, represents the Total Number of Rejected Publications (Inproductivity). Meanwhile, the Y-axis, with a fixed minimum of 1, depicts the Inverse of H-Index (Academic Isolation) of each author based on the total number of non-citations. Each data point (bar height) on the chart corresponds to an author, and the size of the point (bar width) is inversely proportional to the number of Single-Author Papers that person has produced. Additionally, a custom Tooltip feature has not been programmed to hide a pop-up information box when the user hovers over any point, concealing details of the Author's name, Institution, and Average Rejection Rate.