import numpy as np
import joblib


def quantum_encode(X):
    """
    Convert scaled features into a quantum-inspired
    cosine-sine state representation.
    """

    encoded_data = []

    for sample in X:

        # Convert each feature into an angle
        angles = np.pi * (sample + 1) / 2

        # Cosine-sine encoding
        state = []

        for angle in angles:
            state.append(np.cos(angle / 2))
            state.append(np.sin(angle / 2))

        # Convert to numpy array
        state = np.array(state)

        # Normalize the state
        norm = np.linalg.norm(state)

        if norm != 0:
            state = state / norm

        encoded_data.append(state)

    return np.array(encoded_data)


# Load preprocessed training and testing data
X_train = joblib.load("ml_model/X_train.pkl")
X_test = joblib.load("ml_model/X_test.pkl")

# Apply quantum-inspired encoding
X_train_quantum = quantum_encode(X_train)
X_test_quantum = quantum_encode(X_test)

# Save quantum encoded data
joblib.dump(
    X_train_quantum,
    "ml_model/X_train_quantum.pkl"
)

joblib.dump(
    X_test_quantum,
    "ml_model/X_test_quantum.pkl"
)

print("Quantum-inspired encoding completed!")
print("Original features:", X_train.shape[1])
print("Encoded features:", X_train_quantum.shape[1])
print("Training samples:", X_train_quantum.shape[0])
print("Testing samples:", X_test_quantum.shape[0])