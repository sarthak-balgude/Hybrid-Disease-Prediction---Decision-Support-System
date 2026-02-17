import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    CONFIDENCE_THRESHOLD=0.65

    model_path=os.path.join(BASE_DIR, 'ml', 'disease_model.pkl')
    encoder_path=os.path.join(BASE_DIR, 'ml', 'label_encoder.pkl')
    vectorizer_path=os.path.join(BASE_DIR, 'ml', 'vectorizer.pkl')

    hospital_path=os.path.join(BASE_DIR, 'ml', 'hospital_list.csv')
    


