import json
from datetime import datetime, timedelta

class FitnessTracker:
    def __init__(self, user_name):
        self.user_name = user_name
        self.workouts = []
        self.goals = {}
        self.calories_burned = 0
        self.calories_intake = []
        self.reminders = []

    def log_workout(self, workout_type, duration, calories):
        """Log a workout with type, duration, and calories burned."""
        workout = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": workout_type,
            "duration": duration,  # in minutes
            "calories": calories
        }
        self.workouts.append(workout)
        self.calories_burned += calories
        print(f"Workout logged: {workout_type} for {duration} minutes, {calories} calories burned.")

    def log_calorie_intake(self, calories):
        """Log daily calorie intake."""
        self.calories_intake.append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "calories": calories
        })
        print(f"Calorie intake logged: {calories} calories.")

    def set_goal(self, goal_type, target):
        """Set a fitness goal (e.g., weight loss, running distance)."""
        self.goals[goal_type] = target
        print(f"Goal set: {goal_type} target of {target}.")

    def set_reminder(self, reminder_text, reminder_time):
        """Set a reminder for workouts or goals."""
        self.reminders.append({
            "text": reminder_text,
            "time": reminder_time.strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"Reminder set: {reminder_text} at {reminder_time}.")

    def view_progress(self):
        """View workout history, calorie intake, and progress towards goals."""
        print(f"\nFitness Progress for {self.user_name}:")
        print(f"Total Calories Burned: {self.calories_burned}")
        print("\nWorkout History:")
        for workout in self.workouts:
            print(f"{workout['date']} - {workout['type']} for {workout['duration']} minutes, {workout['calories']} calories")
        print("\nCalorie Intake History:")
        for intake in self.calories_intake:
            print(f"{intake['date']} - {intake['calories']} calories")
        print("\nGoals:")
        for goal, target in self.goals.items():
            print(f"{goal}: {target}")
        print("\nReminders:")
        for reminder in self.reminders:
            print(f"{reminder['time']} - {reminder['text']}")

    def calculate_bmi(self, weight, height):
        """Calculate Body Mass Index (BMI)."""
        bmi = weight / (height ** 2)
        print(f"Your BMI is: {bmi:.2f}")
        return bmi

    def suggest_workout(self):
        """Suggest a workout based on goals."""
        if "weight_loss" in self.goals:
            print("Suggested workout: 30 minutes of high-intensity interval training (HIIT).")
        elif "strength" in self.goals:
            print("Suggested workout: 45 minutes of weight lifting.")
        else:
            print("Suggested workout: 30 minutes of brisk walking.")

    def weekly_summary(self):
        """Generate a weekly summary of workouts and calorie intake."""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        weekly_workouts = [w for w in self.workouts if start_date <= datetime.strptime(w["date"], "%Y-%m-%d %H:%M:%S") <= end_date]
        weekly_intake = [i for i in self.calories_intake if start_date <= datetime.strptime(i["date"], "%Y-%m-%d") <= end_date]

        total_calories_burned = sum(w["calories"] for w in weekly_workouts)
        total_calories_intake = sum(i["calories"] for i in weekly_intake)

        print("\nWeekly Summary:")
        print(f"Total Workouts: {len(weekly_workouts)}")
        print(f"Total Calories Burned: {total_calories_burned}")
        print(f"Total Calories Intake: {total_calories_intake}")
        print(f"Net Calories: {total_calories_intake - total_calories_burned}")

    def save_data(self, filename):
        """Save user data to a file."""
        data = {
            "user_name": self.user_name,
            "workouts": self.workouts,
            "goals": self.goals,
            "calories_burned": self.calories_burned,
            "calories_intake": self.calories_intake,
            "reminders": self.reminders
        }
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Data saved to {filename}.")

    def load_data(self, filename):
        """Load user data from a file."""
        with open(filename, "r") as file:
            data = json.load(file)
        self.user_name = data["user_name"]
        self.workouts = data["workouts"]
        self.goals = data["goals"]
        self.calories_burned = data["calories_burned"]
        self.calories_intake = data["calories_intake"]
        self.reminders = data["reminders"]
        print(f"Data loaded from {filename}.")


# Example Usage
if __name__ == "__main__":
    # Create a fitness tracker for a user
    tracker = FitnessTracker("John Doe")

    # Set fitness goals
    tracker.set_goal("weight_loss", "lose 5 kg")
    tracker.set_goal("running_distance", "run 10 km")

    # Log workouts
    tracker.log_workout("Running", 30, 300)
    tracker.log_workout("Weight Lifting", 45, 200)

    # Log calorie intake
    tracker.log_calorie_intake(1800)
    tracker.log_calorie_intake(2000)

    # Set reminders
    tracker.set_reminder("Time for a run!", datetime.now() + timedelta(hours=1))

    # View progress
    tracker.view_progress()

    # Calculate BMI
    tracker.calculate_bmi(70, 1.75)  # weight in kg, height in meters

    # Get a suggested workout
    tracker.suggest_workout()

    # Generate weekly summary
    tracker.weekly_summary()

    # Save data to a file
    tracker.save_data("fitness_data.json")

    # Load data from a file
    new_tracker = FitnessTracker("New User")
    new_tracker.load_data("fitness_data.json")
    new_tracker.view_progress()
