
from sklearn.linear_model import LinearRegression

# 1. Training data
X = [[1], [2], [3], [4], [5], [6], [7]]

y = [20, 35, 50, 65, 80, 95, 110]

# 2. Create the ML model
model = LinearRegression()

# 3. Train the model
model.fit(X, y)

# 4. Make a prediction
new_student = [[6]]

prediction = model.predict(new_student)

# 5. Display result
print("Study hours:", new_student[0][0])
print("Predicted marks:", prediction[0])
