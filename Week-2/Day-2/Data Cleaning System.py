import pandas as pd
import numpy as np

data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, np.nan, 30, 29],
    'income': [50000, 42000, np.nan, 60000],
    'city': ['NY', 'LA', 'NY', np.nan]
})

print("===== Original Data =====")
print(data)

# 1. Detect missing values
print("\n===== Missing Values =====")
print(data.isnull())

print("\n===== Missing Values Count =====")
print(data.isnull().sum())

# 2. Replace missing age with mean
data['age'] = data['age'].fillna(data['age'].mean())

# 3. Replace missing income with median
data['income'] = data['income'].fillna(data['income'].median())

# 4. Replace missing city with most frequent (mode)
data['city'] = data['city'].fillna(data['city'].mode()[0])

print("\n===== Cleaned Data =====")
print(data)
##########          OUTPUT          ##########
===== Original Data =====
      name   age   income city
0    Alice  25.0  50000.0   NY
1      Bob   NaN  42000.0   LA
2  Charlie  30.0      NaN   NY
3    David  29.0  60000.0  NaN

===== Missing Values =====
    name    age  income   city
0  False  False   False  False
1  False   True   False  False
2  False  False    True  False
3  False  False   False   True

===== Missing Values Count =====
name      0
age       1
income    1
city      1
dtype: int64

===== Cleaned Data =====
      name   age   income city
0    Alice  25.0  50000.0   NY
1      Bob  28.0  42000.0   LA
2  Charlie  30.0  50000.0   NY
3    David  29.0  60000.0   NY
