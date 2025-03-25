#this is the implementation of the cleaning. It allows us to fiddle with how we want to use the builder
#to cut up the code. I haven't used drop_column() but it would look like this: .drop_column("column name")

from preprocessing import DataPreProcessingBuilder
import loader
import pandas as pd

# load the dataset
df = loader.df

# init builder
builder = DataPreProcessingBuilder()

# Preprocessing steps: handle null values, remove duplicates, convert to float, trim whitespaces
cleaned_df = (
    builder
    .load_df(df)
    .null_data()
    .remove_duplicates()
    .to_float()
    .white_spaces()
    .build()
)

print(cleaned_df.co)