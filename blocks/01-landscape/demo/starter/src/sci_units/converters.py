"""Temperature unit conversions.

The Fahrenheit/Celsius converter contains a deliberate bug used by the
Block 1 demo. Do not "fix" it outside the demo flow.
"""


def fahrenheit_to_celsius(f: float) -> float:
    """Convert a temperature in degrees Fahrenheit to degrees Celsius."""
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c: float) -> float:
    """Convert a temperature in degrees Celsius to degrees Fahrenheit."""
    return c * 9 / 5 + 32


def kelvin_to_celsius(k: float) -> float:
    """Convert a temperature in Kelvin to degrees Celsius."""
    return k - 273.15
