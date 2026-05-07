import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from utils.features import extract_features

df = pd.read_csv("../data/dataset.csv")

X = df['url'].apply(extract_features).tolist()
y = df['label']

model = RandomForestClassifier(n_estimators=200)
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained!")