import unittest
from second.src.trip import Trip  # Importujemy klasę Trip

class TestTrip(unittest.TestCase):

    def test_trip_creation(self):
        trip = Trip("Paris", 7)
        self.assertIsInstance(trip, Trip, "Obiekt nie jest instancją klasy Trip")

    def test_invalid_trip_creation(self):
        with self.assertRaises(ValueError) as context:
            Trip("", 7)  # Pusta nazwa destynacji
        self.assertEqual(str(context.exception), "Destination must be a non-empty string")

        with self.assertRaises(ValueError) as context:
            Trip("Paris", 0)  # Zero dni
        self.assertEqual(str(context.exception), "Duration must be a positive integer")

    def test_trip_attributes(self):
        trip = Trip("Paris", 7)
        self.assertEqual(trip.destination, "Paris")
        self.assertEqual(trip.duration, 7)

    def test_calculate_cost(self):
        trip1 = Trip("Paris", 7)
        self.assertEqual(trip1.calculate_cost(), 700, "Niepoprawny koszt dla 7 dni")

        trip2 = Trip("Rome", 5)
        self.assertEqual(trip2.calculate_cost(), 500, "Niepoprawny koszt dla 5 dni")

    def test_calculate_cost_zero_duration(self):
        with self.assertRaises(ValueError) as context:
            Trip("London", 0).calculate_cost()
        self.assertEqual(str(context.exception), "Duration must be a positive integer")

    def test_add_participant(self):
        trip = Trip("Paris", 7)

        trip.add_participant("John")
        self.assertIn("John", trip.participants)

        trip.add_participant("Alice")
        trip.add_participant("Bob")
        self.assertIn("Alice", trip.participants)
        self.assertIn("Bob", trip.participants)

    def test_duplicate_participant(self):
        trip = Trip("Paris", 7)
        trip.add_participant("John")
        trip.add_participant("John")
        self.assertEqual(trip.participants.count("John"), 2, "Uczestnik powinien pojawić się 2 razy")

    def test_add_invalid_participant(self):
        trip = Trip("Paris", 7)
        with self.assertRaises(ValueError) as context:
            trip.add_participant(" ")
        self.assertEqual(str(context.exception), "Participant name cannot be empty")

if __name__ == "__main__":
    unittest.main()
