"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np


def generate_data(seed):
    """Generate synthetic temperature sensor data and timestamps.

    Creates simulated temperature readings from two sensors with specified
    statistical properties and corresponding timestamps.

    Parameters
    ----------
    seed : int
        Seed for the random number generator to ensure reproducible results.

    Returns
    -------
    sensor_a : ndarray
        Temperature readings from Sensor A (mean=25°C, std=3°C, size=200).
    sensor_b : ndarray
        Temperature readings from Sensor B (mean=27°C, std=4.5°C, size=200).
    timestamps : ndarray
        Evenly spaced timestamps from 0 to 10 seconds (size=200).
    """
    # Set up random number generator with seed
    rng = np.random.default_rng(seed=seed)

    # Generate timestamps: evenly spaced from 0 to 10 seconds
    timestamps = np.linspace(0, 10, 200)

    # Generate sensor readings
    sensor_a = rng.normal(loc=25, scale=3, size=200)
    sensor_b = rng.normal(loc=27, scale=4.5, size=200)

    return sensor_a, sensor_b, timestamps

