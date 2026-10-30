# Document sjs_006 (Mutated)
## Mutation Type: Contextual Shifting (Changing the domain slightly)

# Document sjs_006  

The Music Engagement Analytics module in the Front-end (file `StreamingInsights.jsx`) employs the Recharts library to generate an interactive Bubble Chart for user behavior data. The X-axis, ranging from 0 to 100, reflects the Total Number of Songs Streamed (Listening Activity). The Y-axis, unbounded, indicates the Engagement Score (Audience Interaction) for each artist, calculated from social media shares and playlist additions. Each bubble on the chart represents an artist, with the bubble's size corresponding to the Number of Featured Collaborations on their tracks. A dynamic Tooltip has been implemented to show a modal popup when users hover over bubbles, revealing details such as the Artist's name, Record Label, and Average Monthly Streams.