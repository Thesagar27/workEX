from flask import Flask, render_template, request, jsonify
import json
import os

api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
DATA_FILE = 'data/workEX_workouts.json'

def load_data():
    """Load data from the JSON file if it exists, otherwise return an empty dictionary."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    """Save the given data to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('workEX_index.html')

@app.route('/workout')
def workout():
    """Render the workout page with predefined workout videos."""
    workouts = [
        {"name": "Push-Up", "video": "https://www.youtube.com/embed/IODxDxX7oi4"},
        {"name": "Squat", "video": "https://www.youtube.com/embed/aclHkVaku9U"},
        {"name": "Plank", "video": "https://www.youtube.com/embed/B296mZDhrP4"}
    ]
    return render_template('workEX_workout.html', workouts=workouts)

@app.route('/progress')
def progress():
    """Render the progress page with user's workout data."""
    data = load_data()
    user_data = data.get("demo_user", [])
    return render_template('workEX_progress.html', workouts=user_data)

@app.route('/save', methods=['POST'])
def save():
    """Save the user's workout data."""
    user_data = request.json
    data = load_data()
    user = user_data.get("user", "demo_user")
    workouts = user_data.get("workouts", [])
    
    # If workouts are not empty, save them to the user's data
    if workouts:
        data[user] = workouts
        save_data(data)
        return jsonify({"status": "success", "message": "Workouts saved successfully."})
    else:
        return jsonify({"status": "error", "message": "No workouts to save."})

@app.route('/settings')
def settings():
    """Render the settings page."""
    return render_template('workEX_settings.html')

@app.route('/logout')
def logout():
    """Render the logout page."""
    return render_template('workEX_logout.html')

@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('workEX_contact.html')

@app.route('/privacy')
def privacy():
    """Render the privacy page."""
    return render_template('workEX_privacy.html')

@app.route('/terms')
def terms():
    """Render the terms and conditions page."""
    return render_template('workEX_terms.html')

if __name__ == '__main__':
    app.run(debug=True)
