import altair as alt
import pandas as pd

df = pd.read_json('templates/datasets/diabetes.json')

scatter_plot = alt.Chart(df).mark_circle(size=60).encode(
    x='bmi',
    y='target',
    tooltip=['bmi', 'age']
).interactive()

scatter_plot.save('chart.json')