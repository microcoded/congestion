def estimate(data):
    if 'device_count' not in data or 'name' not in data:
        return None

    if data['device_count'] < 150:
        congestion_level = 'light'
    elif 150 <= data['device_count'] <= 300:
        congestion_level = 'balanced'
    else:
        congestion_level = 'crowded'

    return {'name': data['name'], 'congestion_level': congestion_level}
