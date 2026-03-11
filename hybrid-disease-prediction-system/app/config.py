import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')

    CONFIDENCE_THRESHOLD = 0.65
    CLOSE_GAP_THRESHOLD = 0.07

    model_path = os.path.join(BASE_DIR, 'ml', 'disease_model.pkl')
    symptom_columns_path = os.path.join(BASE_DIR, 'ml', 'symptom_columns.pkl')

    HOSPITALS_CSV = os.path.join(BASE_DIR, 'data', 'hospital_list.csv')
    DISEASE_SPECIALTY_MAP = os.path.join(BASE_DIR, 'data', 'disease_specialty_map.json')
    


