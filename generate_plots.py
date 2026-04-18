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


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Create a scatter plot of sensor readings versus time on the given Axes.

    Plots temperature readings from two sensors against their timestamps,
    with Sensor A in blue and Sensor B in orange.

    Parameters
    ----------
    sensor_a : array_like
        Temperature readings from Sensor A.
    sensor_b : array_like
        Temperature readings from Sensor B.
    timestamps : array_like
        Time values corresponding to the sensor readings.
    ax : matplotlib.axes.Axes
        The Axes object on which to draw the scatter plot.

    Returns
    -------
    None
        Modifies the provided Axes object in place.
    """
    ax.scatter(timestamps, sensor_a, c='tab:blue', label='Sensor A', alpha=0.7)
    ax.scatter(timestamps, sensor_b, c='tab:orange', label='Sensor B', alpha=0.7)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor readings vs Time')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.3)


def plot_histogram(sensor_a, sensor_b, ax):
    """Create a histogram comparison of sensor temperature distributions.

    Plots overlapping histograms for both sensors with shared bins,
    marks the mean values, and includes count information in labels.

    Parameters
    ----------
    sensor_a : array_like
        Temperature readings from Sensor A.
    sensor_b : array_like
        Temperature readings from Sensor B.
    ax : matplotlib.axes.Axes
        The Axes object on which to draw the histogram.

    Returns
    -------
    None
        Modifies the provided Axes object in place.
    """
    # Remove NaNs for histogramming
    a = sensor_a[~np.isnan(sensor_a)]
    b = sensor_b[~np.isnan(sensor_b)]

    # Shared bins over combined range
    bins = np.linspace(min(a.min(), b.min()), max(a.max(), b.max()), 30)

    ax.hist(a, bins=bins, alpha=0.6, label=f'Sensor A (n={a.size})', color='tab:blue', edgecolor='black')
    ax.hist(b, bins=bins, alpha=0.6, label=f'Sensor B (n={b.size})', color='tab:orange', edgecolor='black')

    # Mark means
    ax.axvline(np.mean(a), color='navy', linestyle='--', linewidth=1, label='A mean')
    ax.axvline(np.mean(b), color='darkorange', linestyle='--', linewidth=1, label='B mean')

    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.set_title('Histogram of sensor temperatures')
    ax.legend()
    ax.grid(alpha=0.3)


# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
