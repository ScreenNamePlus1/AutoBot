# Advanced Yagi Antenna Calculator

A professional-grade tool for designing Yagi-Uda antennas for amateur radio operators.

License: GNU AGPL 3.0

## Overview

The Advanced Yagi Antenna Calculator is a Python-based command-line application designed to assist amateur radio operators in designing high-performance Yagi-Uda antennas. It calculates precise antenna dimensions and performance metrics based on user inputs such as frequency, number of directors, wire gauge, boom material, and optimization goals. The tool supports both metric and imperial units, offers multiple optimization modes (maximum gain, wide bandwidth, or front-to-back ratio), and allows exporting results to a text file for reference.

This tool is ideal for radio enthusiasts, antenna designers, and engineers who need accurate calculations for constructing Yagi antennas tailored to specific bands and performance requirements.

- Author: Advanced Yagi Calculator
- Version: 2.0
- License: MIT

## Features

- Flexible Input Options:
  - Set operating frequency (in MHz).
  - Specify the number of directors (0–20).
  - Choose wire gauge (10–22 AWG).
  - Select boom material (wood, aluminum, fiberglass, PVC, carbon fiber).
  - Choose optimization mode: maximum gain, wide bandwidth, or front-to-back ratio.
  - Select units: metric (meters, cm, mm) or imperial (feet, inches).

- Advanced Calculations:
  - Computes element lengths (reflector, driven element, directors) with corrections for wire diameter and boom material.
  - Calculates element spacing and total boom length.
  - Estimates performance metrics: forward gain (dBi), front-to-back ratio (dB), 3dB beamwidth (°), and input impedance (Ω).
  - Accounts for end effects and boom correction factors.

- User-Friendly Interface:
  - Clear, text-based menu system with input validation.
  - Cross-platform screen clearing (Windows, Linux, macOS).
  - Detailed output with construction notes and optimization details.

- Result Exporting:
  - Exports calculations to a text file with a descriptive filename (e.g., yagi_144.0MHz_3dir.txt).
  - Includes all parameters, dimensions, and performance metrics.

- Robust Error Handling:
  - Validates user inputs to prevent errors.
  - Handles keyboard interrupts and file I/O errors gracefully.
  - Warns about impractical settings (e.g., very high director counts or extreme frequencies).

## Requirements

- Python: Version 3.6 or higher
- Operating System: Windows, Linux, or macOS
- No external dependencies required (uses standard Python libraries: math, sys, os, typing).

## Installation

1. Ensure Python is Installed:
   - Verify Python 3.6+ is installed by running: python3 --version
   - If not installed, download and install Python from https://www.python.org/downloads/.

2. Download the Script:
   - Save the script as yagi_calculator.py in a directory of your choice.
   - Alternatively, clone or download this repository: git clone <repository-url> followed by cd <repository-directory>.

## Usage

1. Run the Script:
   - Open a terminal and navigate to the directory containing yagi_calculator.py.
   - Execute the script: python3 yagi_calculator.py

2. Navigate the Menu:
   - The program displays a menu with options (0–9):
     ADVANCED YAGI ANTENNA CALCULATOR v2.0
     Professional Amateur Radio Antenna Design Tool
     ======================================================
     
     MENU OPTIONS:
     1. Set Frequency
     2. Set Number of Directors
     3. Select Wire Gauge
     4. Select Boom Material
     5. Choose Optimization Mode
     6. Select Units (Metric/Imperial)
     7. Calculate Antenna Dimensions
     8. Show Current Settings
     9. Export Results to File
     0. Exit
     --------------------------------------
     Enter your choice (0-9):
   - Enter a number to select an option and follow the prompts to configure settings.

3. Example Workflow:
   To design a Yagi antenna for 144 MHz (2-meter band) with 3 directors, 14 AWG wire, aluminum boom, optimized for gain, and metric units:
   - Select 1 and enter 144.0 for frequency.
   - Select 2 and enter 3 for directors.
   - Select 3 and choose 14 for wire gauge.
   - Select 4 and choose 2 for aluminum boom.
   - Select 5 and choose 1 for maximum gain.
   - Select 6 and choose 1 for metric units.
   - Select 7 to calculate and view results.
   - Select 9 to export results to a file.
   - Select 0 to exit.

4. View Results:
   - After selecting option 7, the program displays detailed results, including:
     - Performance metrics (gain, front-to-back ratio, beamwidth, impedance).
     - Element dimensions and spacings.
     - Construction notes (e.g., use a 1:1 balun, fine-tune lengths).

5. Export Results:
   - Option 9 saves results to a text file in the same directory, e.g., yagi_144.0MHz_3dir.txt.

## Example Output

For a 144 MHz antenna with 3 directors, optimized for gain, using 14 AWG wire and an aluminum boom in metric units:

============================================================
                    CALCULATION RESULTS
============================================================

ESTIMATED PERFORMANCE:
----------------------
Forward Gain:        12.1 dBi
Front-to-Back Ratio: 22.5 dB
Beamwidth (3dB):     53°
Input Impedance:     40 Ω
Wavelength:          2.082 m

ELEMENT DIMENSIONS:
-------------------
Reflector:           1.002 m
Driven Element:      0.966 m
Director 1:          0.914 m
Director 2:          0.910 m
Director 3:          0.906 m

ELEMENT SPACING (center-to-center):
-----------------------------------
Reflector ← Driven:  31.2 cm
Driven → Director 1: 31.2 cm
Driven → Director 2: 52.0 cm
Driven → Director 3: 72.9 cm

TOTAL BOOM LENGTH:   1.561 m

CONSTRUCTION NOTES:
-------------------
* Split driven element at center for feed connection
* Use 1:1 balun for best SWR performance
* All elements must be parallel and perpendicular to boom
* Fine-tune by adjusting element lengths ±2-3%
* Consider weatherproofing for outdoor installations
* Use non-conductive insulators to mount elements

* Optimized for: Maximum Gain

## Notes

- Frequency Range: The calculator accepts any frequency in MHz but warns for values outside 1–10,000 MHz, as these are beyond typical amateur radio bands.
- Director Count: Supports 0–20 directors. Higher counts yield diminishing returns and may be impractical.
- Optimization Modes:
  - Maximum Gain: Prioritizes forward gain (up to ~20 dBi).
  - Wide Bandwidth: Optimizes for better SWR across a frequency range.
  - Front-to-Back Ratio: Maximizes rejection of rear signals (up to ~35 dB).
- Construction Tips: Results include practical notes for antenna construction, such as using a balun and weatherproofing.
- Limitations:
  - Calculations are based on simplified models and may require fine-tuning in practice.
  - Assumes ideal conditions (e.g., no nearby objects affecting performance).

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch: git checkout -b feature/new-feature
3. Commit changes: git commit -m "Add new feature"
4. Push to the branch: git push origin feature/new-feature
5. Open a pull request.

Please ensure code follows the existing style and includes tests where applicable.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions, bug reports, or feature requests, please open an issue on the repository or contact the author through this github page at ScreenNamePlus1/Deceptecon-Omega

---

Happy antenna building!
