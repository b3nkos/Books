from config import WORKOUT_TYPES
from workouts import workout_minutes, show_workouts
from statistics import show_statistics, weekedn_preview

print("🏋️ Fitness Tracker\n")

print("Workout types")
for workout_type in WORKOUT_TYPES:
    print(f"- {workout_type}")

print("\nDaily workouts")
show_workouts()

show_statistics(workout_minutes)
weekedn_preview(workout_minutes)

print("\nKeep going! Consistency is key 💪")