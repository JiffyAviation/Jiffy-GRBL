# Jiffy GRBL

Interactive Jupyter GUI for controlling your CO₂ laser via GRBL (Monport V2 board). Snapshot of features:

## Features
- X/Y jogging via GUI buttons
- Homing & center-of-bed functions
- Hold-to-fire 🔥 laser button
- Power slider (S0–S1000)
- Modular design: CLI, GUI, movement logic

## Setup
```bash
git clone https://github.com/YourUsername/Jiffy-GRBL.git
cd Jiffy-GRBL
conda env create -f environment.yml
conda activate Jiffy_GRBL
code Jiffy_GRBL_1.ipynb
```

## Safety
Laser only fires while button is held—no toggle or lock-on behavior.

## License
MIT
