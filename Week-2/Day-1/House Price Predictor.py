# Dataset
sqft = [800, 1000, 1200, 1500]
prices = [150000, 200000, 230000, 300000]

#Mean
mean_x = sum(sqft) / len(sqft)
mean_y = sum(prices) / len(prices)

# Slope
numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(sqft, prices))
denominator = sum((x - mean_x)**2 for x in sqft)
m = numerator / denominator

# Intercept
b = mean_y - (m * mean_x)


target_size = 1100
predicted_price = (m * target_size) + b

print(f"Model: y = {m:.2f}x + {b:.2f}")
print(f"Predicted house price for 1100 sqft: ${predicted_price:.2f}")


##########          OUTPUT          ##########
Model: y = 209.35x + -15514.02
Predicted house price for 1100 sqft: $214766.36
