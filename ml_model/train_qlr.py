import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load quantum-encoded training and testing data
X_train = joblib.load("ml_model/X_train_quantum.pkl")
X_test = joblib.load("ml_model/X_test_quantum.pkl")

# Load target values
y_train = joblib.load("ml_model/y_train.pkl")
y_test = joblib.load("ml_model/y_test.pkl")

# Create Q-LR model
model = LogisticRegression(
    max_iter=2000,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Q-LR training completed!")
print("Q-LR Accuracy:", accuracy)
print("Q-LR Accuracy (%):", accuracy * 100)

# Display detailed results
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(
    model,
    "ml_model/quantum_logistic_model.pkl"
)

print("\nQ-LR model saved successfully!")