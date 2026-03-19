import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 4])
y = np.array([40000, 50000, 60000, 65000])

# Normalization
X_min = np.min(X)
X_max = np.max(X)
X_scaled = (X - X_min) / (X_max - X_min)

m, b = 0.0, 0.0
learning_rate = 0.05
iterations = 100
loss_history = []

# GD loop
for i in range(iterations):
    y_pred = m * X_scaled + b
    error = y_pred - y

    # Mse
    loss = np.mean(error**2)
    loss_history.append(loss)

    # partial derivativs
    m_grad = (2/len(X_scaled)) * np.dot(error, X_scaled)
    b_grad = (2/len(X_scaled)) * np.sum(error)

    # Parameter Update
    m -= learning_rate * m_grad
    b -= learning_rate * b_grad


    if (i + 1) % 20 == 0 or i == 0:
        print(f"Iteration {i+1}: Loss = {loss:.2f}")


plt.figure(figsize=(12, 5))
#prediction for 5 years
target_years = 5
target_scaled = (target_years - X_min) / (X_max - X_min)
final_salary = (m * target_scaled) + b
print(f"Final Predicted Salary for 5 Years: ${final_salary:,.2f}")


plt.subplot(1, 2, 1)
plt.plot(range(iterations), loss_history, color='red', linewidth=2)
plt.title('Step 1: Loss Minimization')
plt.xlabel('Iterations')
plt.ylabel('Mean Squared Error')
plt.grid(True, alpha=0.3)


plt.subplot(1, 2, 2)
plt.scatter(X_scaled, y, color='blue', label='Actual Data')
plt.plot(X_scaled, m * X_scaled + b, color='green', label='Learned Line')
plt.title('Step 2: Final Fit')
plt.xlabel('Scaled Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()

###########            OUTPUT            ###########
Iteration 1: Loss = 2981250000.00
Iteration 20: Loss = 18543568.58
Iteration 40: Loss = 2164329.01
Iteration 60: Loss = 2018341.23
Iteration 80: Loss = 1967481.11
Iteration 100: Loss = 1934783.82
Final Predicted Salary for 5 Years: $74,505.14

