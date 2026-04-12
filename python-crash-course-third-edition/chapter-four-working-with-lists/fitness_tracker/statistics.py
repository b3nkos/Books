def show_statistics(minutes):
    print(f"\nMinimum workout: {min(minutes)} minutes")
    print(f"Maximum workout: {max(minutes)} minutes")
    print(f"Total workout time: {sum(minutes)} minutes")

def weekedn_preview(minutes):
    minutes_copy = minutes[:]

    print("\nWeekend preview")
    print(f"Thursday: {minutes_copy[-2]} minutes")
    print(f"Friday: {minutes_copy[-1]} minutes")