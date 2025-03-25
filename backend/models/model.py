
import pandas as pd
from sklearn.model_selection import train_test_split

diabetes_df =  pd.read_csv("backend/data/datasets/diabetes.csv")

X = diabetes_df.drop("target", axis = 1)
y = diabetes_df["target"]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.25, random_state = 354)




