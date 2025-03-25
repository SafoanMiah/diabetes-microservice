#this is the implementation of the cleaning. It allows us to fiddle with how we want to use the builder
#to cut up the code. I haven't used drop_column() but it would look like this: .drop_column("column name")

import preprocessing as pp
import loader

df = loader.df
builder = pp.DataPreProcessingBuilder()

cleaned_df = builder.load_df(df).null_data().remove_duplicates().to_float().white_spaces().build()
