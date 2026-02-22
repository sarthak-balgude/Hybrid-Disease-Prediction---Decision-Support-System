import os
import google.generativeai as genai


def gemini_key():
    api_key=os.getenv("GEMINI_API_KEY")

    if not api_key:
        return None
    
    genai.configure(api_key=api_key)
    genai.GenerativeModel("gemini-2.0-flash")
    return 


def guidance(symtoms:str,condition:str,confidence:float,pyschology:dict,ml_output:dict):

    model = _get_gemini_client()
    
    top_diseases = ml_output.get("top_diseases",[])
    top_confidence = ml_output.get("confidence",0.0)

    prompt="""you are a medical expert .Do not predict disease but give guidance to the user based on the following information:\n"

    user symptoms:{symptoms},
    confidence:{top_confidence*100}% ,

    probabilities:{top_probabilities}


    pyschological_screening:{pyschology.get("stress")}
    pyschological_screening:{pyschology.get("anxiety")}
    pyschological_screening:{pyschology.get("sleep_quality")}

    condition:{condition}
    
    Generate output in this exact format:

    1) Summary (1-2 lines)
    2) Possible causes (3 bullet points max)
    3) What to do now (4 bullet points)
    4) Red flags (3 bullet points)
    5) When to consult doctor
    6) Disclaimer (1 line)

    Keep it short, safe, and non-alarming.
    
    """

    response=model.generate_content(prompt)
    return response.text.strip()


