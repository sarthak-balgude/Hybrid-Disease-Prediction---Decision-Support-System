import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.services.hospital_finder import find_hospitals_for_disease

# Test the function
hospitals = find_hospitals_for_disease("fever", "new delhi")
print("Hospitals found:")
for hospital in hospitals:
    print(f"Name: {hospital['name']}")
    print(f"Phone: {hospital.get('phone', 'No phone')}")
    print(f"Address: {hospital.get('address', 'No address')}")
    print("---")