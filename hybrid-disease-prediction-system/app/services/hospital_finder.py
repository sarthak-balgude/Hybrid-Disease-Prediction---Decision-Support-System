import csv
import json
from flask import current_app

SPECIALTY_MAP = {}
HOSPITALS = []


def load_specialty_map():
    global SPECIALTY_MAP

    path = current_app.config.get("DISEASE_SPECIALTY_MAP")

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

            # convert list → dictionary
            SPECIALTY_MAP = {
                item["disease"].lower(): item["specialty"].lower()
                for item in data
            }

    except Exception:
        SPECIALTY_MAP = {}


def load_hospitals():
    global HOSPITALS

    path = current_app.config.get("HOSPITALS_CSV")

    try:
        with open(path, "r", encoding="utf-8") as f:

            reader = csv.DictReader(f)

            hospitals = []

            for row in reader:

                hospitals.append({
                    "name": row.get("name", ""),
                    "city": row.get("city", "").lower(),
                    "type": row.get("type", ""),
                    "phone": row.get("phone", ""),
                    "specialties": [
                        s.strip().lower()
                        for s in row.get("specialties", "").split("|")
                        if s.strip()
                    ]
                })

            HOSPITALS = hospitals

    except Exception:
        HOSPITALS = []


def find_hospitals_for_disease(disease: str, city: str):

    disease = disease.lower()
    city = city.lower()

    specialty = SPECIALTY_MAP.get(disease)

    # Filter by city
    city_hospitals = [h for h in HOSPITALS if h["city"] == city]

    if not city_hospitals:
        return HOSPITALS[:5]

    # If no specialty mapping
    if not specialty:
        return city_hospitals[:5]

    # Filter by specialty
    filtered = [
        h for h in city_hospitals
        if specialty in h["specialties"]
    ]

    if filtered:
        return filtered[:5]

    # fallback
    return city_hospitals[:5]