class Client:
    def __init__(self):
        self._reservations = []

    def book(self, time, n_people):
        self._reservations.append({"time": time, "n_people": n_people})

    def get_bookings(self):
        return self._reservations
