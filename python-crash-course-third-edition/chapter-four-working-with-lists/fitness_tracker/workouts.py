from config import DAYS

# Minutes trained each day
workout_minutes = [30, 45, 20, 60, 40]

def show_workouts():
    for i in range(0, 5):
        print(f"{DAYS[i]}: {workout_minutes[i]} minutes")