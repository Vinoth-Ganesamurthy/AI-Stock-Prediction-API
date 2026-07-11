import joblib
from pathlib import Path

# Get the absolute path to the models folder
MODEL_PATH = Path(__file__).parent.parent / "models" / "random_forest_model.joblib"

# Load the model once when the application starts
model = joblib.load(MODEL_PATH)

def load_model():
    """
    Returns the already loaded model.
    """
    return model

print("✅ Model loaded successfully!")
print(type(model))