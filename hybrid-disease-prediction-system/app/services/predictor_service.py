import joblib
import numpy as np
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "ml/disease_model.pkl")
SYMPTOM_PATH = os.path.join(BASE_DIR, "ml/symptom_columns.pkl")

# Load once when server starts
model = None
symptom_columns = None

# Try to load models, but handle missing files gracefully
try:
    if os.path.exists(MODEL_PATH) and os.path.getsize(MODEL_PATH) > 0:
        model = joblib.load(MODEL_PATH)
        print(f"✓ Disease model loaded: {MODEL_PATH}")
    if os.path.exists(SYMPTOM_PATH) and os.path.getsize(SYMPTOM_PATH) > 0:
        symptom_columns = joblib.load(SYMPTOM_PATH)
        print(f"✓ Symptom columns loaded: {len(symptom_columns)} symptoms")
except Exception as e:
    print(f"Warning: Could not load model files: {e}")
    print("The application will run but disease prediction will be unavailable.")
    print("Please train the model using the Colab training script and upload .pkl files.")


def predict_disease(symptoms_text):
    """
    Predict disease from symptom text.
    
    Expected input: symptoms_text = "fever headache body_aches" (space-separated)
    
    The model expects binary input where:
    - 1 = symptom present
    - 0 = symptom absent
    """
    
    if model is None or symptom_columns is None:
        return {
            "prediction": "Model not trained",
            "confidence": 0.0,
            "top3": [
                {"disease": "Please train the model first", "probability": 0.0}
            ],
            "error": "Model files are not available. Please train and upload model files to app/ml/"
        }

    try:
        # Parse symptoms from text input
        # User enters: "fever headache body_aches"
        # Expected symptom column names from Kaggle dataset
        
        input_symptoms = symptoms_text.lower().strip().split()
        
        # Create binary vector matching symptom columns from training
        # Shape should match: (number of symptoms from training dataset)
        input_vector = pd.DataFrame(
            np.zeros((1, len(symptom_columns))),
            columns=symptom_columns
        )
        
        # Mark symptoms as present (1) if they match
        for symptom in input_symptoms:
            # Try exact match first
            if symptom in input_vector.columns:
                input_vector.loc[0, symptom] = 1
            # Try partial match (in case user types different format)
            else:
                for col in input_vector.columns:
                    if symptom.lower() in col.lower() or col.lower() in symptom.lower():
                        input_vector.loc[0, col] = 1
                        break
        
        # Get predictions with probabilities
        probs = model.predict_proba(input_vector)[0]
        classes = model.classes_
        
        # Get top prediction
        top_idx = np.argmax(probs)
        prediction = classes[top_idx]
        confidence = float(probs[top_idx])
        
        # Get top 3 predictions
        top_indices = np.argsort(probs)[-3:][::-1]
        
        top3 = [
            {
                "disease": classes[i],
                "probability": float(probs[i])
            }
            for i in top_indices
        ]
        
        return {
            "prediction": prediction,
            "confidence": confidence,
            "top3": top3,
            "input_symptoms_matched": sum(1 for s in input_symptoms if any(s in col.lower() for col in input_vector.columns))
        }
    
    except Exception as e:
        print(f"Prediction error: {e}")
        import traceback
        traceback.print_exc()
        
        return {
            "prediction": "Error",
            "confidence": 0.0,
            "top3": [],
            "error": f"Prediction failed: {str(e)}"
        }