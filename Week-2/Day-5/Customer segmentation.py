import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("customers.csv")

X = df[['Annual Income', 'Spending Score']]

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

print(df[['CustomerID', 'CustomerName', 'Mobile', 'Cluster']])

plt.scatter(df['Annual Income'], df['Spending Score'], c=df['Cluster'])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()
