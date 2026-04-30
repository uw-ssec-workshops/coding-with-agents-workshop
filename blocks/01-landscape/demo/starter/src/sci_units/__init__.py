"""sci_units — tiny scientific unit-conversion utilities.

Used as the running scenario across the "Coding with AI Agents" workshop.
Intentionally small: one module, a couple of functions, a couple of tests.
"""

from sci_units.converters import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
)

__all__ = [
    "celsius_to_fahrenheit",
    "fahrenheit_to_celsius",
    "kelvin_to_celsius",
]
