import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


X = np.array([[1], [2], [3], [4]]) # Years
y = np.array([40000, 50000, 60000, 65000]) # Salary


model = LinearRegression()
model.fit(X, y)

# Predict for 5 years
prediction = model.predict([[5]])[0]
print(f"Predicted salary for 5 years: ${prediction:,.2f}")

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()

###########            OUTPUT             ###########
Predicted salary for 5 years: $75,000.00

