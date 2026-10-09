import joblib
import numpy as np

# Load saved models and preprocessing objects
model = joblib.load("ml_model/quantum_kernel_svm_crop_model.pkl")
scaler = joblib.load("ml_model/scaler.pkl")
label_encoder = joblib.load("ml_model/label_encoder.pkl")


def predict_crop(N, P, K, temperature, humidity, ph, rainfall):

    # Create input data
    input_data = np.array([[
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    ]])

    # Scale input data
    input_scaled = scaler.transform(input_data)

    # Apply the same quantum-inspired encoding
    angles = np.pi * (input_scaled[0] + 1) / 2

    state = []

    for angle in angles:
        state.append(np.cos(angle / 2))
        state.append(np.sin(angle / 2))

    state = np.array(state)

    # Normalize
    norm = np.linalg.norm(state)

    if norm != 0:
        state = state / norm

    # Convert to 2D array for the model
    state = state.reshape(1, -1)

    # Predict crop
    prediction = model.predict(state)

    # Convert number back to crop name
    crop_name = label_encoder.inverse_transform(prediction)[0]

    return crop_name


# Test prediction
if __name__ == "__main__":

    crop = predict_crop(
        90,
        42,
        43,
        20.87,
        82.00,
        6.50,
        202.93
    )

    print("Predicted Crop:", crop)