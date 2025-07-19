# Jiffy GRBL

A simple, interactive Jupyter Notebook GUI for controlling GRBL-based laser engravers — including CO₂ lasers. Designed for safety, clarity, and hackability.

## 🚀 Features

- Manual X/Y jogging with GUI arrows
- Home and "center bed" buttons
- Safe 🔥 laser fire button (momentary only)
- Laser power slider (S0–S1000)
- Compatible with Monport V2 GRBL boards
- Runs inside VS Code with Jupyter kernel

## 🛠 Requirements

- Python 3.x with Anaconda or Miniconda
- `ipywidgets`, `pyserial`, `jupyter`
- VS Code + Jupyter extension (optional)

## 📦 Installation

Clone this repo and install dependencies with:

```bash
conda env create -f environment.yml
