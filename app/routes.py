"""OctoFit Tracker App - Routes"""
from flask import Blueprint, render_template, request, jsonify
from datetime import datetime

bp = Blueprint('main', __name__)

# In-memory storage for workout data
workouts = []

@bp.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@bp.route('/api/workouts', methods=['GET', 'POST'])
def handle_workouts():
    """Handle workout data"""
    if request.method == 'POST':
        workout = request.json
        workout['id'] = len(workouts) + 1
        workout['date'] = datetime.now().isoformat()
        workouts.append(workout)
        return jsonify(workout), 201
    
    return jsonify(workouts)

@bp.route('/api/workouts/<int:workout_id>', methods=['DELETE'])
def delete_workout(workout_id):
    """Delete a workout"""
    global workouts
    workouts = [w for w in workouts if w['id'] != workout_id]
    return '', 204
