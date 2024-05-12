class ReservationException(Exception):
    def __init__(self, message="Reservation failed."):
        self.message = message
        super().__init__(self.message)
