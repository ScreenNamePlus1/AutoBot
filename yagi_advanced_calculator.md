def print_readme():
    """
    Prints the complete README file for the Yagi Antenna Calculator.
    """
    readme_text = """# Yagi Antenna Calculator

This Python script is a tool for amateur radio enthusiasts and hobbyists who want to design a multi-element Yagi antenna. It calculates the optimal dimensions for the reflector, driven element, and a specified number of directors based on a desired radio frequency. The calculations assume you are using **14-gauge copper wire** and a **wooden dowel** for the boom.

---

## Features

* **Frequency-Based Design**: Calculates all dimensions based on a single input frequency in MHz.
* **Scalable**: Allows you to specify any number of directors to increase antenna gain.
* **Dual Units**: Provides all measurements in both inches and meters for convenience.
* **Estimated Performance**: Gives an approximate gain in dBi based on the number of elements.

---

## Prerequisites

* **Python**: You need to have Python installed on your computer. This script was written for Python 3.x.
* **Terminal/Command Prompt**: The script runs directly from a command-line interface.

---

## How to Use

### 1. Save the Script

Copy the entire code from the calculator and save it in a plain text file. Name the file `yagi_advanced_calculator.py`.

### 2. Open a Terminal

Navigate to the directory where you saved the file.

* **Windows**: Open Command Prompt or PowerShell.
* **macOS/Linux**: Open the Terminal application.

### 3. Run the Program

In the terminal, execute the following command:

`python yagi_advanced_calculator.py`

### 4. Follow the Prompts

The program will ask you for two inputs:

1.  **Enter the desired frequency in MHz**: Type in the frequency you want the antenna to operate on (e.g., `144.5`).
2.  **Enter the number of directors you want to add**: Type in an integer for the number of director elements (e.g., `5` for five directors).

### 5. Review the Output

The script will then display the calculated dimensions for all the elements and their spacing. The output is organized into two main sections:

* **Calculated Dimensions**: This lists the required length for the reflector, driven element, and each individual director. Note that the directors become progressively shorter as they move away from the driven element.
* **Calculated Spacing**: This shows the distance from the driven element to the reflector and to each director, measured from the center of the elements.

---

## Important Notes

* **Assumptions**: The calculations in this script are based on general approximations for common Yagi designs. The `end_effect_factor` for the **14-gauge wire** and the spacing assumptions for the **wooden dowel** (non-metallic boom) are included.
* **Performance**: The estimated gain in dBi is a **rough approximation**. For a highly optimized antenna, you should use professional antenna modeling software.
* **Precision**: Use a measuring tape or ruler that can handle the precision required for the dimensions (down to tenths of an inch or millimeters) to ensure the best performance.
* **Driven Element Construction**: The driven element is a dipole, meaning it should be split in the middle to connect to your transmission line (coaxial cable). The calculator provides the total length of the element.
"""
    print(readme_text)

if __name__ == "__main__":
    print_readme()
