from flask import Flask, render_template

app = Flask(__name__)

# Sample data
study_areas = [
    {'name': 'Library Level 8', 'congestion_level': 'light'},
    {'name': 'CB11.04.400', 'congestion_level': 'balanced'},
    {'name': 'Reading Room', 'congestion_level': 'crowded'},
    {'name': 'FEIT FLP', 'congestion_level': 'balanced'}
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html', study_areas=study_areas)
