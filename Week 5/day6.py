data = {
    "user": "Amerix",
    "followers": 1200000,
    "last_post": {
        "title": "Cold shower protocol",
        "likes": 4800
    }
}

print(f"Followers: {data['followers']}")
print(f"Last post likes: {data['last_post']['likes']}")
print()

data = {
    "supplier": "Nairobi Steel Ltd",
    "prices": {
        "mild_steel_sheet": 4500,
        "angle_iron": 2800
    }
}

mild_steel_cost = 3 * data["prices"]["mild_steel_sheet"]
angle_iron_cost = 6 * data["prices"]["angle_iron"]
total = mild_steel_cost + angle_iron_cost

print(f"Mild steel sheets (3): KES {mild_steel_cost}")
print(f"Angle iron (6m): KES {angle_iron_cost}")
print(f"Total: KES {total}")
print()

data = {
    "driver": "Kamau Njoroge",
    "date": "2026-08-13",
    "trips": [
        {"route": "Westlands to CBD",     "fare_kes": 560},
        {"route": "CBD to South B",       "fare_kes": 420},
        {"route": "South B to Karen",     "fare_kes": 980},
        {"route": "Karen to Westlands",   "fare_kes": 720},
        {"route": "Westlands to Airport", "fare_kes": 740},
    ]
}

trips = data["trips"]
total_trips = 0
total_earned = 0
highest_trip = None
highest_fare = 0

for t in trips:
    total_trips += 1
    total_earned += t["fare_kes"]
    if t["fare_kes"] > highest_fare:
        highest_fare = t["fare_kes"]
        highest_trip = t

print(f"Total trips: {total_trips}")
print(f"Total earned: KES {total_earned}")
print(f"Highest trip: {highest_trip['route']} | KES {highest_trip['fare_kes']}")