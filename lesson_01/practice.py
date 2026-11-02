
from sklearn.linear_model import LinearRegression

# 1. Training data
X = [[1], [2], [3], [4], [5]]

y = [3,5,7,9,11]

# 2. Create the ML model
model = LinearRegression()

# 3. Train the model
model.fit(X, y)
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# 4. Make a prediction
new_Experience = [[6]]

prediction = model.predict(new_Experience)

# 5. Display result
print("Experience (years):", new_Experience[0][0])
print("Predicted salary:", prediction[0])
