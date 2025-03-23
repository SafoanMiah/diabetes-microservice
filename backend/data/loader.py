
import pandas as pd
from sklearn.datasets import load_diabetes

diabetes = load_diabetes() #this is a json file so we can't load it directly as is

x = diabetes.data
y = diabetes.target #literally refers to target which is the most important column
                    #in terms of model training
df = pd.DataFrame(x, columns = diabetes.feature_names)

df["target"] = y



