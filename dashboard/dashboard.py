from flask import Flask, render_template, request, jsonify
import estimate

app = Flask(__name__)

# Initialize the study_areas list
study_areas = []


@app.route('/')
def dashboard():
    # Render the dashboard HTML template
    """
    Renders the dashboard from ./templates/dashboard.html

    Returns:
        None
    """
    return render_template('dashboard.html')

@app.route('/receive', methods=['POST'])
def receive_post():
    """
    Receives POST request data on the /receive endpoint

    Returns:
        JSON response, 200 OK
    """
    global study_areas
    data_in = request.get_json() or request.form.to_dict()

    # Convert device_count to integer
    if isinstance(data_in.get('device_count'), str):
        data_in['device_count'] = int(data_in['device_count'])

    # DEBUG: Log received data to console
    print("Received data:", data_in)
    area_data = estimate.estimate(data_in)

    if area_data:
        # If the area is already in the list, update it; otherwise, append it
        existing_area = next((area for area in study_areas if area['name'] == area_data['name']), None)
        if existing_area:
            existing_area['congestion_level'] = area_data['congestion_level']
        else:
            study_areas.append(area_data)

    return jsonify({"message": "OK"}), 200

@app.route('/data', methods=['GET'])
def get_data():
    """
    Receives GET request from client devices.
    Sends updated data to the requesting client.

    Returns:
        JSON response of study areas and their congestion levels.
    """
    return jsonify(study_areas)

# Main function, entrypoint
if __name__ == '__main__':
    app.run(debug=True)
