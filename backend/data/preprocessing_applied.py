#this is the implementation of the cleaning. It allows us to fiddle with how we want to use the builder
#to cut up the code. I haven't used drop_column() but it would look like this: .drop_column("column name")

from preprocessing import DataPreProcessingBuilder
import loader
import pandas as pd

# load the dataset
df = loader.df

# init builder
builder = DataPreProcessingBuilder()

# Preprocessing steps: handle null values, remove duplicates, convert to float
cleaned_df = (
    builder
    .load_df(df)
    .null_data()
    .remove_duplicates()
    .to_float()

    # Rename columns, to: 'age', 'sex', 'bmi', 'bp', 'tc', 'ldl', 'hdl', 'tch', 'ltg', 'glu'
    # https://scikit-learn.org/stable/datasets/toy_dataset.html
    .rename_column('s1', 'tc')
    .rename_column('s2', 'ldl')
    .rename_column('s3', 'hdl')
    .rename_column('s4', 'tch')
    .rename_column('s5', 'ltg')
    .rename_column('s6', 'glu')
    .build()
)

# Saving the cleaned datafram to a CSV
cleaned_df.to_csv("backend/data/datasets/diabetes.csv", index=False)