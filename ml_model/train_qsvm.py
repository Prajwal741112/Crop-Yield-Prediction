import joblib
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load quantum-encoded training and testing data
X_train = joblib.load("ml_model/X_train_quantum.pkl")
X_test = joblib.load("ml_model/X_test_quantum.pkl")

# Load target values
y_train = joblib.load("ml_model/y_train.pkl")
y_test = joblib.load("ml_model/y_test.pkl")

# Create Q-SVM model
model = SVC(
    kernel="rbf",
    C=10,
    gamma="scale",
    probability=True,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Q-SVM training completed!")
print("Q-SVM Accuracy:", accuracy)
print("Q-SVM Accuracy (%):", accuracy * 100)

# Display detailed results
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, "ml_model/quantum_kernel_svm_crop_model.pkl")

print("\nQ-SVM model saved successfully!")