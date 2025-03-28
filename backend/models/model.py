import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# simple linear model as showcase

diabetes_df = pd.read_json("backend/data/datasets/diabetes.json")

X = diabetes_df.drop("target", axis=1)
y = diabetes_df["target"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=354
)

model = LinearRegression()
model.fit(X_train, y_train)

with open("backend/models/linear_regression_model.pkl", "wb") as f:
    pickle.dump(model, f)
