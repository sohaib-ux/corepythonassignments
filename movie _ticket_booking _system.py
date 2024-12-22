def book_seat(booked_seats, seat):
    if seat not in booked_seats:
        booked_seats.append(seat)

def cancel_seat(booked_seats, seat):
    if seat in booked_seats:
        booked_seats.remove(seat)

total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5

book_seat(booked_seats, book_seat)
cancel_seat(booked_seats, cancel_seat)

available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
print(available_seats)
