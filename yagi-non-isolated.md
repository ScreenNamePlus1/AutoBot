# Advanced Yagi Antenna Calculator for Non-Isolated Aluminum Booms

## Overview

The Advanced Yagi Antenna Calculator for Non-Isolated Aluminum Booms is a Python-based command-line application designed to assist amateur radio operators in designing high-performance Yagi-Uda antennas where elements are electrically connected to an aluminum boom (non-isolated mounting). It calculates precise antenna dimensions and performance metrics based on user inputs such as frequency, number of directors, wire gauge, boom diameter, and optimization goals. The tool supports both metric and imperial units, offers multiple optimization modes (maximum gain, wide bandwidth, or front-to-back ratio), and allows exporting results to a text file for reference.

This calculator is specifically tailored for scenarios where elements are mounted directly through or in electrical contact with an aluminum boom, applying appropriate boom correction factors based on the DL6WU formula for non-insulated mounting. It is ideal for radio enthusiasts, antenna designers, and engineers who need accurate calculations for constructing Yagi antennas tailored to specific bands and performance requirements without using insulators.

- Author: Advanced Yagi Calculator (Modified for Non-Isolated)
- Version: 1.0
- License: MIT

## Features

- Flexible Input Options:
  - Set operating frequency (in MHz).
  - Specify the number of directors (0–20).
  - Choose wire gauge (10–22 AWG).
  - Set aluminum boom diameter (in mm, typically 20–50 mm).
  - Choose optimization mode: maximum gain, wide bandwidth, or front-to-back ratio.
  - Select units: metric (meters, cm, mm) or imperial (feet, inches).

- Advanced Calculations:
  - Computes element lengths (reflector, driven element, directors) with corrections for wire diameter and non-isolated aluminum boom effects.
  - Applies boom correction based on the DL6WU formula, doubled for non-isolated mounting, to reflector and director lengths.
  - Calculates element spacing and total boom length.
  - Estimates performance metrics: forward gain (dBi), front-to-back ratio (dB), 3dB beamwidth (°), and input impedance (Ω).
  - Accounts for end effects due to wire diameter.

- User-Friendly Interface:
  - Clear, text-based menu system with input validation.
  - Cross-platform screen clearing (Windows, Linux, macOS).
  - Detailed output with construction notes specific to non-isolated mounting.

- Result Exporting:
  - Exports calculations to a text file with a descriptive filename (e.g., non_isolated_yagi_144.0MHz_3dir.txt).
  - Includes all parameters, dimensions, performance metrics, and boom correction details.

- Robust Error Handling:
  - Validates user inputs to prevent errors (e.g., negative frequencies, invalid wire gauges).
  - Handles keyboard interrupts and file I/O errors gracefully.
  - Warns about impractical settings (e.g., very high director counts, extreme frequencies, or large boom diameters).

## Requirements

- Python: Version 3.6 or higher
- Operating System: Windows, Linux, or macOS
- No external dependencies required (uses standard Python libraries: math, sys, os, typing).

## Installation

1. Ensure Python is Installed:
   - Verify Python 3.6+ is installed by running: python3 --version
   - If not installed, download and install Python from https://www.python.org/downloads/.

2. Download the Script:
   - Save the script as non_isolated_yagi_calculator.py in a directory of your choice.
   - Alternatively, clone or download this repository: git clone <repository-url> followed by cd <repository-directory>.

## Usage

1. Run the Script:
   - Open a terminal and navigate to the directory containing non_isolated_yagi_calculator.py.
   - Execute the script: python3 non_isolated_yagi_calculator.py

2. Navigate the Menu:
   - The program displays a menu with options (0–9):
     ADVANCED YAGI ANTENNA CALCULATOR FOR NON-ISOLATED ALUMINUM BOOMS v1.0
     Professional Amateur Radio Antenna Design Tool (Non-Isolated Elements)
     ======================================================
     
     MENU OPTIONS:
     1. Set Frequency
     2. Set Number of Directors
     3. Select Wire Gauge
     4. Set Boom Diameter (mm)
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
   To design a Yagi antenna for 144 MHz (2-meter band) with 3 directors, 14 AWG wire, 25 mm aluminum boom, optimized for gain, and metric units:
   - Select 1 and enter 144.0 for frequency.
   - Select 2 and enter 3 for directors.
   - Select 3 and choose 14 for wire gauge.
   - Select 4 and enter 25.0 for boom diameter.
   - Select 5 and choose 1 for maximum gain.
   - Select 6 and choose 1 for metric units.
   - Select 7 to calculate and view results.
   - Select 9 to export results to a file.
   - Select 0 to exit.

4. View Results:
   - After selecting option 7, the program displays detailed results, including:
     - Performance metrics (gain, front-to-back ratio, beamwidth, impedance).
     - Element dimensions and spacings.
     - Boom correction applied to reflector and directors.
     - Construction notes specific to non-isolated mounting.

5. Export Results:
   - Option 9 saves results to a text file in the same directory, e.g., non_isolated_yagi_144.0MHz_3dir.txt.

## Example Output

For a 144 MHz antenna with 3 directors, optimized for gain, using 14 AWG wire and a 25 mm aluminum boom in metric units:

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
Reflector:           1.004 m
Driven Element:      0.966 m
Director 1:          0.916 m
Director 2:          0.912 m
Director 3:          0.908 m

ELEMENT SPACING (center-to-center):
-----------------------------------
Reflector ← Driven:  31.2 cm
Driven → Director 1: 31.2 cm
Driven → Director 2: 52.0 cm
Driven → Director 3: 72.9 cm

TOTAL BOOM LENGTH:   1.561 m
Boom Correction Applied: 2.24 mm (added to reflector and directors)

CONSTRUCTION NOTES:
-------------------
* This calculator assumes non-isolated elements (electrically connected to aluminum boom)
* Driven element is assumed elevated above boom - no correction applied
* Split driven element at center for feed connection
* Use 1:1 balun for best SWR performance
* All elements must be parallel and perpendicular to boom
* Fine-tune by adjusting element lengths ±2-3%
* Consider weatherproofing for outdoor installations
* Elements pass through boom without insulators

* Optimized for: Maximum Gain

## Notes

- Boom Correction:
  - The calculator uses the DL6WU formula for insulated boom correction, doubled for non-isolated mounting, applied to reflector and director lengths.
  - The driven element is assumed to be elevated above the boom (e.g., on a non-conductive support), so no boom correction is applied to it.
  - Correction depends on boom diameter and frequency (wavelength).

- Frequency Range:
  - Accepts any frequency in MHz but warns for values outside 1–10,000 MHz, as these are beyond typical amateur radio bands.

- Director Count:
  - Supports 0–20 directors. Higher counts yield diminishing returns and may be impractical.

- Optimization Modes:
  - Maximum Gain: Prioritizes forward gain (up to ~20 dBi).
  - Wide Bandwidth: Optimizes for better SWR across a frequency range.
  - Front-to-Back Ratio: Maximizes rejection of rear signals (up to ~35 dB).

- Construction Tips:
  - Results include notes specific to non-isolated mounting, emphasizing direct electrical connection to the aluminum boom.
  - A 1:1 balun is recommended for optimal SWR.
  - Fine-tuning (±2-3%) may be needed due to environmental factors or manufacturing tolerances.

- Limitations:
  - Calculations are based on simplified models and may require practical fine-tuning.
  - Assumes ideal conditions (e.g., no nearby objects affecting performance).
  - Assumes a circular aluminum boom; non-standard shapes may require additional adjustments.
  - Driven element is assumed to be elevated to avoid boom interaction, which may not suit all designs.

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

For questions, bug reports, or feature requests, please open an issue on the repository or contact the author at [your-contact-info] (replace with actual contact details if applicable).

---

Happy antenna building!
