from flask import Flask, render_template

app = Flask(__name__)

# Sample data
study_areas = [
    {'name': 'Library Level 8', 'congestion_level': 'low'},
    {'name': 'CB11.04.400', 'congestion_level': 'medium'},
    {'name': 'Reading Room', 'congestion_level': 'high'},
    {'name': 'FEIT FLP', 'congestion_level': 'medium'}
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html', study_areas=study_areas)
