from flask import current_app


def decide_condition(confidence: float, top3: list, psychology_impact: str):
    conf_threshold = current_app.config.get("CONFIDENCE_THRESHOLD", 0.65)
    close_gap_threshold = current_app.config.get("CLOSE_GAP_THRESHOLD", 0.07)

    if not top3 or len(top3) < 2:
        if confidence >= conf_threshold:
            return "HIGH_CONFIDENCE"
        return "LOW_CONF_PSY_LOW"

    # Condition 1: High confidence
    if confidence >= conf_threshold:
        return "HIGH_CONFIDENCE"

    # Condition 4 (close top1 and top2)
    top1 = top3[0].get("probability", 0.0)
    top2 = top3[1].get("probability", 0.0)
    gap = abs(top1 - top2)

    if gap <= close_gap_threshold:
        return "UNCERTAIN_CLOSE_TOP3"

    # Condition 2 (psychology high)
    if psychology_impact == "High":
        return "LOW_CONF_PSY_HIGH"

    # Condition 3: Low confidence with low psychology
    return "LOW_CONF_PSY_LOW"