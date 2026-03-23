import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn import tree

df = pd.read_csv("decision_tree_dataset.csv")

le_income = LabelEncoder()
df["Income"] = le_income.fit_transform(df["Income"])

le_label = LabelEncoder()
df["Buy_Product"] = le_label.fit_transform(df["Buy_Product"])


X = df[["Age", "Income"]]
y = df["Buy_Product"]


model = DecisionTreeClassifier()
model.fit(X, y)

plt.figure(figsize=(8,5))
tree.plot_tree(model, feature_names=["Age", "Income"], class_names=le_label.classes_, filled=True)
plt.show()

new_customer = [[30, le_income.transform(["High"])[0]]]


prediction = model.predict(new_customer)
print("Prediction =", le_label.inverse_transform(prediction)[0])

#########              OUTPUT              ##########
Prediction = Yes
