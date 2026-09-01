# 1. INPUT VARIABLES (Hardcoded with different data types)
user_id: int = 10482
weight_kg: float = 72.5
workout_name: str = "Morning Run"
is_outdoor: bool = True
heart_rates: list = [120, 135, 142, 138, 150]
target_muscles: set = {"quads", "calves", "quads"}  # Duplicate "quads" is removed
user_settings: dict = {"unit": "metric", "mode": "dark"}


# 2. PROCESSING FUNCTION
def process_workout(
    uid, weight, name, outdoor, hr_list, muscles, settings
) -> tuple:
    avg_hr = sum(hr_list) / len(hr_list)
    calories = round(len(hr_list) * (avg_hr / 100) * (weight / 10), 1)
    status = True

    # Returns a Tuple containing the results
    return (status, calories, name, muscles, settings["unit"])


# 3. EXECUTION AND OUTPUT
output_summary: tuple = process_workout(
    user_id,
    weight_kg,
    workout_name,
    is_outdoor,
    heart_rates,
    target_muscles,
    user_settings,
)

# Print inputs
print("Inputs:", user_id, weight_kg, workout_name, is_outdoor)
print("List Input:", heart_rates)
print("Set Input:", target_muscles)
print("Dict Input:", user_settings)

# Print output tuple
print("\nOutput Tuple:", output_summary)
