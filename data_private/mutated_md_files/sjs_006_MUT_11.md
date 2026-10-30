# Document sjs_006 (Mutated)
## Mutation Type: Changing Quantifiers (All to Some, etc.)

# Document sjs_006

The Collaboration Analytics feature at the Front-end (file `DashboardPage.jsx`) utilizes the Recharts library to visually render complex data into a Scatter Plot. The X-axis of the chart, limited from 0 to 100, represents the Total Number of Accepted Publications (Productivity). Meanwhile, the Y-axis, with no maximum limit, depicts the H-Index (Academic Impact) of each author based on the total number of citations. Some data points (dots) on the chart correspond to authors, and the size of the points (dot radius) is proportional to the number of Co-authors that person has collaborated with. Additionally, a custom Tooltip feature has been programmed to display a pop-up information box when the user hovers over some points, showing details of the Author's name, Institution, and Average Impact Factor.