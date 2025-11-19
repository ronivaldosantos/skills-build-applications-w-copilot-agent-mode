// OctoFit Tracker - Client-side JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const workoutForm = document.getElementById('workoutForm');
    const workoutsList = document.getElementById('workoutsList');

    // Load workouts on page load
    loadWorkouts();

    // Handle form submission
    workoutForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        const workout = {
            exercise: document.getElementById('exercise').value,
            duration: parseInt(document.getElementById('duration').value),
            calories: parseInt(document.getElementById('calories').value),
            notes: document.getElementById('notes').value
        };

        try {
            const response = await fetch('/api/workouts', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(workout)
            });

            if (response.ok) {
                workoutForm.reset();
                loadWorkouts();
            }
        } catch (error) {
            console.error('Error adding workout:', error);
        }
    });

    // Load and display workouts
    async function loadWorkouts() {
        try {
            const response = await fetch('/api/workouts');
            const workouts = await response.json();
            displayWorkouts(workouts);
        } catch (error) {
            console.error('Error loading workouts:', error);
        }
    }

    // Display workouts in the list
    function displayWorkouts(workouts) {
        workoutsList.innerHTML = '';
        
        workouts.forEach(workout => {
            const workoutItem = document.createElement('div');
            workoutItem.className = 'workout-item';
            workoutItem.innerHTML = `
                <div class="workout-info">
                    <h3>${workout.exercise}</h3>
                    <p>Duration: ${workout.duration} min | Calories: ${workout.calories}</p>
                    ${workout.notes ? `<p>Notes: ${workout.notes}</p>` : ''}
                    <p><small>${new Date(workout.date).toLocaleDateString()}</small></p>
                </div>
                <button class="btn-delete" onclick="deleteWorkout(${workout.id})">Delete</button>
            `;
            workoutsList.appendChild(workoutItem);
        });
    }

    // Make deleteWorkout available globally
    window.deleteWorkout = async function(id) {
        try {
            const response = await fetch(`/api/workouts/${id}`, {
                method: 'DELETE'
            });

            if (response.ok) {
                loadWorkouts();
            }
        } catch (error) {
            console.error('Error deleting workout:', error);
        }
    };
});
