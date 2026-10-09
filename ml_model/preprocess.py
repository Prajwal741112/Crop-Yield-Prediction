import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("dataset/crop_data.csv")

# Input features
X = df[[
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph",
    "rainfall"
]]

# Target
y = df["label"]

# Encode crop names into numbers
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Scale the input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)

# Save preprocessing objects
joblib.dump(scaler, "ml_model/scaler.pkl")
joblib.dump(label_encoder, "ml_model/label_encoder.pkl")

# Save processed data
joblib.dump(X_train, "ml_model/X_train.pkl")
joblib.dump(X_test, "ml_model/X_test.pkl")
joblib.dump(y_train, "ml_model/y_train.pkl")
joblib.dump(y_test, "ml_model/y_test.pkl")

print("Preprocessing completed successfully!")
print("Total records:", len(df))
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("Number of crop classes:", len(label_encoder.classes_))
print("Crop classes:", list(label_encoder.classes_))