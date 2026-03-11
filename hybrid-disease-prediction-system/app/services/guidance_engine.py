import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()


# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# for m in genai.list_models():
#     if "generateContent" in m.supported_generation_methods:
#         print(m.name)


def build_guidance_with_gemini(condition: str, symptoms: str, ml_output: dict, psychology: dict):
    """Generate medical guidance using Google Gemini API"""
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        return "Unable to generate guidance - API key not configured. Please set GEMINI_API_KEY environment variable."
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        top_confidence = ml_output.get("confidence", 0.0)
        top3 = ml_output.get("top3", [])
        
        probabilities_text = "\n".join([
            f"- {disease['disease']}: {disease['probability']*100:.1f}%"
            for disease in top3
        ])
        
        prompt = f"""You are a medical expert. Do not predict disease but give guidance to the user based on the following information:

User symptoms: {symptoms}
Condition: {condition}
ML Model Confidence: {top_confidence*100:.1f}%

Top predicted conditions:
{probabilities_text}

Psychological Screening:
- Stress Level: {psychology.get('stress', 'Unknown')}
- Anxiety Level: {psychology.get('anxiety', 'Unknown')}
- Sleep Quality: {psychology.get('sleep_quality', 'Unknown')}

Please provide guidance in this exact format:
1) Summary (1-2 lines)
2) Possible causes (3 bullet points max)
3) What to do now (4 bullet points)
4) Red flags (3 bullet points)
5) When to consult doctor
6) Disclaimer (1 line)

Keep it short, safe, and non-alarming."""
        
        response = model.generate_content(prompt)
        return response.text.strip()
    
    except Exception as e:
        return f"Unable to generate guidance at this moment. Error: {str(e)}"




