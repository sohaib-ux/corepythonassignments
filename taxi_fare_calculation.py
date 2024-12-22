def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10
    return base_fare + (distance * distance_fare)

trips = [5, 10, 3]
total_fare = 0

for i, trip in enumerate(trips, 1):
    fare = calculate_fare(trip)
    total_fare += fare
    print(f"${fare}")

print(f"${total_fare}")
