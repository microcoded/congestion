def estimate(data: dict) -> dict[str, str] | None:
    """
    Estimates the congestion level of a study area.

    Parameters:
        data: Input dictionary of name and device_count.
    Returns:
        A dictionary of name and congestion level calculated, or none if input is malformed.
    """

    congestion_level: str
    lower_bracket: int = 20
    upper_bracket: int = 40

    if 'device_count' not in data or 'name' not in data:
        return None

    if data['device_count'] < lower_bracket:
        congestion_level = 'light'
    elif lower_bracket <= data['device_count'] <= upper_bracket:
        congestion_level = 'balanced'
    else:
        congestion_level = 'crowded'

    return {'name': data['name'], 'congestion_level': congestion_level}
