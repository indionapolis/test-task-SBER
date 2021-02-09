def generate_time_table():
    return {f'{i}:00': False for i in range(0, 23)}


class Client:
    def __init__(self):
        self._reservations = []

        self._booking_table = [(2, generate_time_table()),
                               (2, generate_time_table()),
                               (4, generate_time_table()),
                               (4, generate_time_table())]

    def book(self, time: str, n_people: str) -> str:
        for i, table in enumerate(self._booking_table):
            if table[0] >= int(n_people):
                if not table[1][time]:
                    table[1][time] = True
                    self._reservations.append({"time": time, "n_people": n_people})

                    return f'booked successfully, your time: {time}, your table: {i}'

        return 'unfortunately there are no available tables on your time'

    def get_bookings(self):
        return self._reservations
