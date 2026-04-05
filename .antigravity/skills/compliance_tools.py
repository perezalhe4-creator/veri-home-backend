def calculate_risk(confidence: float, is_structural: bool) -> float:
    if is_structural:
        return 1.0
    return 1.0 - confidence
