# Sensor Data Visualization

A small Python script that generates synthetic temperature sensor readings and creates publication-quality scatter, histogram, and box plot visualizations.

## Installation

1. Activate the `ece105` conda environment:

```bash
conda activate ece105
```

2. Install the required packages with either `conda` or `mamba`:

```bash
conda install numpy matplotlib
```

or

```bash
mamba install numpy matplotlib
```

## Usage

Run the standalone script from the project directory:

```bash
python generate_plots.py
```

This will generate the plots and save the resulting figure to a PNG file.

## Example output

The script produces a single output file:

- `sensor_analysis.png`

That file contains three subplots side-by-side:

- a scatter plot of Sensor A and Sensor B readings versus time,
- a histogram comparison of the two sensor temperature distributions,
- a side-by-side box plot comparison of Sensor A and Sensor B with the combined mean annotated.

## AI tools used and disclosure

This section is reserved for a brief disclosure of AI assistance and tools used during development. Replace this placeholder text with the appropriate details.
