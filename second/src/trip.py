class Trip:
    def __init__(self, destination: str, duration: int):
        if not isinstance(destination, str) or not destination.strip():
            raise ValueError("Destination must be a non-empty string")
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Duration must be a positive integer")

        self.destination = destination
        self.duration = duration
        self.participants = []  # Lista uczestników

    def calculate_cost(self) -> int:
        return self.duration * 100

    def add_participant(self, participant: str):
        if not isinstance(participant, str) or not participant.strip():
            raise ValueError("Participant name cannot be empty")

        self.participants.append(participant)  # Dodajemy uczestnika bez sprawdzania duplikatów
