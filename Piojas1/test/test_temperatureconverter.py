import unittest
from src.temperatureconverter import TemperatureConverter


class TestTemperatureConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(TemperatureConverter.celsius_to_fahrenheit(0), 32.0)
        self.assertAlmostEqual(TemperatureConverter.celsius_to_fahrenheit(100), 212.0)
        self.assertAlmostEqual(TemperatureConverter.celsius_to_fahrenheit(-40), -40.0)
        self.assertAlmostEqual(TemperatureConverter.celsius_to_fahrenheit(37), 98.6)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(TemperatureConverter.fahrenheit_to_celsius(32), 0.0)
        self.assertAlmostEqual(TemperatureConverter.fahrenheit_to_celsius(212), 100.0)
        self.assertAlmostEqual(TemperatureConverter.fahrenheit_to_celsius(-40), -40.0)
        self.assertAlmostEqual(TemperatureConverter.fahrenheit_to_celsius(98.6), 37.0)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(TemperatureConverter.celsius_to_kelvin(0), 273.15)
        self.assertAlmostEqual(TemperatureConverter.celsius_to_kelvin(100), 373.15)
        self.assertAlmostEqual(TemperatureConverter.celsius_to_kelvin(-273.15), 0.0)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(TemperatureConverter.kelvin_to_celsius(273.15), 0.0)
        self.assertAlmostEqual(TemperatureConverter.kelvin_to_celsius(373.15), 100.0)
        self.assertAlmostEqual(TemperatureConverter.kelvin_to_celsius(0), -273.15)

    def test_negative_kelvin_input(self):
        with self.assertRaises(ValueError):
            TemperatureConverter.kelvin_to_celsius(-1)


if __name__ == "__main__":
    unittest.main()
