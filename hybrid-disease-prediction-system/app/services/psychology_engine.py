def compute_psychology_score(stress: str, anxiety: str, sleep: str):
    stress_map = {"Low": 0, "Medium": 1, "High": 2}
    anxiety_map = {"Low": 0, "Medium": 1, "High": 2}
    sleep_map = {"Normal": 0, "Poor": 1}

    s = stress_map.get(stress, 0)
    a = anxiety_map.get(anxiety, 0)
    sl = sleep_map.get(sleep, 0)

    score = s + a + sl  # max 5

    if score <= 1:
        impact = "Low"
    elif score <= 3:
        impact = "Medium"
    else:
        impact = "High"

    return {
        "stress": stress,
        "anxiety": anxiety,
        "sleep": sleep,
        "score": score,
        "impact": impact
    }