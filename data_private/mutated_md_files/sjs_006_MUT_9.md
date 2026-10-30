# Document sjs_006 (Mutated)
## Mutation Type: Cause and Effect Reversal

# Document sjs_006

The Collaboration Analytics feature at the Front-end (file `DashboardPage.jsx`) utilizes the Recharts library to visually render complex data into a Scatter Plot. The X-axis of the chart, limited from 0 to 100, represents the H-Index (Academic Impact) of each author based on the total number of citations. Meanwhile, the Y-axis, with no maximum limit, depicts the Total Number of Accepted Publications (Productivity) influenced by the Academic Impact. Each data point (dot) on the chart corresponds to an author, and the size of the point (dot radius) is proportional to the H-Index, which determines the number of Co-authors that person has collaborated with. Additionally, a custom Tooltip feature has been programmed to display a pop-up information box when the user hovers over any point, showing details of the Author's name, Institution, and Average Impact Factor.