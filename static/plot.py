import altair as alt
from vega_datasets import data

chart = alt.Chart(data.cars.url).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N'
)

chart.save('templates/datasets/chart.json')