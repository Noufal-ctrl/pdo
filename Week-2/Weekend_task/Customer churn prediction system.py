import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

df = pd.read_csv("customer_churn_dataset.csv")
df.fillna(df.mean(numeric_only=True), inplace=True)


le = LabelEncoder()
df['ContractType'] = le.fit_transform(df['ContractType'])
df['Churn'] = le.fit_transform(df['Churn'])

scaler = StandardScaler()
df[['Age', 'MonthlyCharges', 'Tenure']] = scaler.fit_transform(
    df[['Age', 'MonthlyCharges', 'Tenure']]
)

print(df.head())
##########          OUTPUT          ############
 CustomerID       Age  MonthlyCharges  ContractType    Tenure  Churn
0           1 -0.980906        0.043273             1  0.402696      0
1           2 -0.980906        0.411552             0  1.238395      0
2           3 -1.227427        0.181378             0 -1.101563      0
3           4 -0.734385        0.457587             0 -1.602983      1
4           5  0.621479        1.424321             0 -0.934423      0

###########                           ###########

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

X = df[['Age', 'MonthlyCharges', 'ContractType', 'Tenure']]
y = df['Churn']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


lr = LogisticRegression()
dt = DecisionTreeClassifier()

lr.fit(X_train, y_train)
dt.fit(X_train, y_train)


from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# Logistic Regression
y_pred_lr = lr.predict(X_test)

print("Logistic Regression")
print("Accuracy:", accuracy_score(y_test, y_pred_lr))
print("Precision:", precision_score(y_test, y_pred_lr))
print("Recall:", recall_score(y_test, y_pred_lr))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_lr))


# Decision Tree
y_pred_dt = dt.predict(X_test)

print("\nDecision Tree")
print("Accuracy:", accuracy_score(y_test, y_pred_dt))
print("Precision:", precision_score(y_test, y_pred_dt))
print("Recall:", recall_score(y_test, y_pred_dt))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_dt))

##########          OUTPUT          ############
Logistic Regression
Accuracy: 0.94
Precision: 0.0
Recall: 0.0
Confusion Matrix:
 [[47  0]
 [ 3  0]]

Decision Tree
Accuracy: 1.0
Precision: 1.0
Recall: 1.0
Confusion Matrix:
 [[47  0]
 [ 0  3]]
##########                         ############

raw_age = 30
raw_monthly_charges = 80
raw_contract_type = 0 
raw_tenure = 6


features_to_scale = [[raw_age, raw_monthly_charges, raw_tenure]]
scaled_features = scaler.transform(features_to_scale)


new_data_for_prediction = [
    scaled_features[0][0],  
    scaled_features[0][1],  
    raw_contract_type,      
    scaled_features[0][2]   
]

new_data_for_prediction_2d = [new_data_for_prediction]

prob = lr.predict_proba(new_data_for_prediction_2d)[0][1]
print("Churn Probability =", round(prob, 2))

if prob > 0.5:
    print("Customer likely to churn")
else:
    print("Customer likely to stay")
##########          OUTPUT          ############
Churn Probability = 0.24
Customer likely to stay
##########                          ############

import matplotlib.pyplot as plt

importance = dt.feature_importances_
features = X.columns

plt.bar(features, importance)
plt.title("Feature Importance")
plt.show()

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)

print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
##########          OUTPUT          ############
Random Forest Accuracy: 0.98
