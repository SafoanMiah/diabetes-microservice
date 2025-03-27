# This file creates the JSON to be charted onto the website

import altair as alt
import pandas as pd

# Load the data
df = pd.read_json("backend/data/datasets/diabetes.json")

# Columns for the dropdown
cols = ["age", "sex", "bmi", "bp", "tc", "ldl", "hdl", "tch", "ltg", "glu"]

# Altair parameter bound to a dropdown
select_col = alt.param(
    name="Column",  # internal name for the parameter
    bind=alt.binding_select(
        options=cols, name="Choose X-axis:"
    ),  # 'select' to create a dropdown
    value="age",  # default selection
)


# Function to create a layer for a given column
def layer_for_col(col):
    """
    Returns a layered chart:
      - Scatter plot of main DataFrame vs. 'target'
      - Regression line
      - All hidden by default unless the parameter matches `col`.
    """
    # Target is explicitly typed as quantitative
    y_encoding = alt.Y("target:Q", title="Disease Progression")

    # Filter for x col
    base = alt.Chart(df.assign(xcol=col)).transform_filter(alt.datum.xcol == select_col)

    scatter = base.mark_point(color="#1f77b4", opacity=0.7, size=60).encode(
        x=alt.X(f"{col}:Q", title=col.upper()), y=y_encoding, tooltip=["target:Q"]
    )

    reg_line = (
        base.transform_regression(col, "target")
        .mark_line(color="#ff7f0e", size=3)
        .encode(x=f"{col}:Q", y=y_encoding)
    )

    return alt.layer(scatter, reg_line)


# One layer per column, then combine & add the param
chart = alt.layer(*(layer_for_col(c) for c in cols)).add_params(select_col)

# Config properties
chart = (
    chart.properties(title="Diabetes Features Scatter Plot", width=1200, height=380)
    .configure_axis(
        titleFontSize=18,  # Axis titles
        titlePadding=15,  # Space between axis and label
        gridColor="lightgray",
        gridOpacity=0.5,
    )
    .configure_title(
        fontSize=22  # Updated title font size
    )
)

# Save the chart
chart.save("templates/chart/chart.json")
print("Chart saved as JSON")
