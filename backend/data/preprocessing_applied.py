#this is the implementation of the cleaning. It allows us to fiddle with how we want to use the builder
#to cut up the code. I haven't used drop_column() but it would look like this: .drop_column("column name")

from preprocessing import DataPreProcessingBuilder
import loader
import pandas as pd

# load the dataset
df = loader.df

builder = DataPreProcessingBuilder()

cleaning = builder.load_df(df).null_data().remove_duplicates().rename_column("s1", "tc").to_float().build()
cleaned_df = cleaning.clean()

# Saving the cleaned datafram to a CSV
cleaned_df.to_csv("datasets/diabetes.csv", index=False)

