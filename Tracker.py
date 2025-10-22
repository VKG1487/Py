import time
from datetime import datetime

def get_positive_number(prompt, number_type=float):
    while True:
        value = input(prompt).strip()
        try:
            if number_type == int:
                num = int(value)
            else:
                num = float(value)
            if num < 0:
                print("Please enter a non-negative number.")
                continue
            return num
        except ValueError:
            print("Invalid number. Please try again.")

def main():
    print("\nWelcome to the Daily Calorie Tracker!")
    print("This tool lets you enter your meals and calories,")
    print("then shows total and average calories and compares with your daily limit.\n")

    # Ask how many meals
    num_meals = 0
    while num_meals <= 0:
        num_meals = int(get_positive_number("How many meals would you like to enter? (e.g. 3): ", int))
        if num_meals <= 0:
            print("Please enter at least 1 meal.")

    meal_names = []
    calories = []

    for i in range(1, num_meals + 1):
        name = input(f"Enter name for meal #{i} (e.g. Breakfast): ").strip()
        if not name:
            name = f"Meal_{i}"
        cal = get_positive_number("Enter calories for '{}' (number): ".format(name), float)
        meal_names.append(name)
        calories.append(cal)
        print(f"Recorded: {name} → {cal} kcal\n")

    total_cal = sum(calories)
    avg_cal = total_cal / len(calories) if calories else 0.0

    # Ask daily limit
    daily_limit = get_positive_number("Enter your daily calorie limit (e.g. 2000): ", float)

    # Determine status
    status = "Within Limit ✅" if total_cal <= daily_limit else "Exceeded Limit ⚠️"
    warning_msg = ""
    if total_cal > daily_limit:
        warning_msg = "\nWARNING: Your total calorie intake exceeds your daily limit!\n"

    # Print classic formatted output
    print("\nMeal Name\tCalories")
    print("-" * 25)
    for name, cal in zip(meal_names, calories):
        print(f"{name.ljust(15)}{str(round(cal,2)).rjust(7)}")
    print("-" * 25)
    print(f"Total Calories:{str(round(total_cal,2)).rjust(8)}")
    print(f"Average:{str(round(avg_cal,2)).rjust(14)}")
    print(f"Status:{str(status).rjust(13)}")
    if warning_msg:
        print(warning_msg)

    # Ask to save
    save = input("\nDo you want to save this session to a file? (y/n): ").strip().lower()
    if save == 'y':
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"calorie_log_{timestamp}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("Daily Calorie Tracker Session Log\n")
                f.write("="*40 + "\n")
                f.write(f"User: Vibhash Kumar Giri\n")
                f.write(f"Roll No: 2501010069\n")
                f.write(f"Subject: Programming with Python for Problem Solving\n")
                f.write(f"College: K.R. Mangalam University\n")
                f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("Meals:\n")
                for name, cal in zip(meal_names, calories):
                    f.write(f"  - {name} : {round(cal,2)} kcal\n")
                f.write("\n")
                f.write(f"Total Calories: {round(total_cal,2)} kcal\n")
                f.write(f"Average per meal: {round(avg_cal,2)} kcal\n")
                f.write(f"Daily Limit: {round(daily_limit,2)} kcal\n")
                f.write(f"Status: {status}\n")
            print(f"Session saved to '{filename}' in the current directory.")
        except Exception as e:
            print("Failed to save file:", e)
    else:
        print("Session was not saved.")

    print("\nThank you for using the Daily Calorie Tracker. Goodbye!\n")

if __name__ == '__main__':
    main()
