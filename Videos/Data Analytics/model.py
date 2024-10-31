from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Step 1: Get Data
data = load_iris()
X = data.data
y = data.target

# Step 2: Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Clean Data (skip for this example as Iris dataset is clean)

# Step 4: Get a Model
model = DecisionTreeClassifier()

# Step 5: Train Model
model.fit(X_train, y_train)

# Step 6: Make Prediction
predictions = model.predict(X_test)

# Step 7: Evaluate Your Model
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy * 100:.2f}%")

