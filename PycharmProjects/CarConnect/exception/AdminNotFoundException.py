class AdminNotFoundException(Exception):
    def __init__(self, message="Admin not found."):
        self.message = message
        super().__init__(self.message)
