class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32


    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9


    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15


    @staticmethod
    def kelvin_to_celsius(kelvin):
        if kelvin<0:
            raise ValueError("Kelvin cannot be lower than 0")
        return kelvin - 273.15