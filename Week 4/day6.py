def daily_milk_volume(entry):
    try:
        return float(entry)
    except ValueError:
        print(f"Invalid entry: {entry} is not a number")
        return None


entry = "two hundred"
volume = daily_milk_volume(entry)
