import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Create dataset
data = pd.DataFrame([
    {"city": "NY", "income": 50000},
    {"city": "LA", "income": 42000},
    {"city": "Chicago", "income": 45000}
])

print("Original Data\n",data)

le = LabelEncoder()
data['city_label'] = le.fit_transform(data['city'])


print("Label Encoded Data\n",data)

one_hot = pd.get_dummies(data['city'])
one_hot = one_hot.astype(int)

print("One-Hot Encoded Data\n",one_hot)

##########              OUTPUT              ###########
Original Data
       city  income
0       NY   50000
1       LA   42000
2  Chicago   45000
Label Encoded Data
       city  income  city_label
0       NY   50000           2
1       LA   42000           1
2  Chicago   45000           0
One-Hot Encoded Data
    Chicago  LA  NY
0        0   0   1
1        0   1   0
2        1   0   0
