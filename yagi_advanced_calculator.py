#!/usr/bin/env python3
"""
Advanced Yagi Antenna Calculator
Professional-grade antenna design tool for amateur radio enthusiasts
"""

import math
import sys

class YagiCalculator:
    def __init__(self):
        # Physical constants
        self.SPEED_OF_light = 299792458  # meters per second
        
        # Wire diameter lookup table (in mm)
        self.WIRE_GAUGES = {
            '10': 2.588,
            '12': 2.053,
            '14': 1.628,
            '16': 1.291,
            '18': 1.024,
            '20': 0.812,
            '22': 0.644
        }
        
        # Boom material correction factors
        self.BOOM_CORRECTIONS = {
            'wood': 1.0,
            'aluminum': 0.95,
            'fiberglass': 0.98,
            'pvc': 0.97,
            'carbon_fiber': 0.96
        }
        
        # Popular amateur radio bands
        self.POPULAR_BANDS = {
            '1': ('6m', 50.0, 54.0),
            '2': ('2m', 144.0, 148.0),
            '3': ('70cm', 420.0, 450.0),
            '4': ('23cm', 1240.0, 1300.0),
            '5': ('13cm', 2300.0, 2450.0)
        }

    def display_banner(self):
        """Display the application banner"""
        print("=" * 70)
        print("         ADVANCED YAGI ANTENNA CALCULATOR v2.0")
        print("       Professional Antenna Design Tool")
        print("=" * 70)
        print()

    def get_frequency_input(self):
        """Get frequency input from user with band selection option"""
        print("FREQUENCY SELECTION")
        print("-" * 30)
        print("1. Enter specific frequency")
        print("2. Select from popular amateur bands")
        print()
        
        while True:
            choice = input("Choose option (1-2): ").strip()
            
            if choice == '1':
                while True:
                    try:
                        freq = float(input("Enter frequency in MHz (e.g., 144.5): "))
                        if freq <= 0:
                            print("Error: Frequency must be positive")
                            continue
                        return freq
                    except ValueError:
                        print("Error: Please enter a valid number")
                        
            elif choice == '2':
                print("\nPOPULAR AMATEUR BANDS:")
                for key, (band, low, high) in self.POPULAR_BANDS.items():
                    print(f"{key}. {band} band ({low}-{high} MHz)")
                
                band_choice = input("\nSelect band (1-5): ").strip()
                if band_choice in self.POPULAR_BANDS:
                    band_name, low, high = self.POPULAR_BANDS[band_choice]
                    center_freq = (low + high) / 2
                    print(f"Using {band_name} center frequency: {center_freq} MHz")
                    
                    custom = input(f"Use custom frequency in {band_name} band? (y/n): ").lower()
                    if custom == 'y':
                        while True:
                            try:
                                freq = float(input(f"Enter frequency ({low}-{high} MHz): "))
                                if low <= freq <= high:
                                    return freq
                                else:
                                    print(f"Error: Frequency must be between {low} and {high} MHz")
                            except ValueError:
                                print("Error: Please enter a valid number")
                    else:
                        return center_freq
                else:
                    print("Invalid band selection")
            else:
                print("Invalid choice. Please select 1 or 2.")

    def get_design_parameters(self):
        """Get all design parameters from user"""
        parameters = {}
        
        # Number of directors
        print("\nDIRECTOR ELEMENTS")
        print("-" * 30)
        while True:
            try:
                num_dirs = int(input("Number of directors (0-20): "))
                if 0 <= num_dirs <= 20:
                    parameters['num_directors'] = num_dirs
                    break
                else:
                    print("Error: Number of directors must be between 0 and 20")
            except ValueError:
                print("Error: Please enter a valid integer")
        
        # Wire gauge selection
        print("\nWIRE GAUGE SELECTION")
        print("-" * 30)
        print("Available wire gauges (AWG):")
        for gauge, diameter in self.WIRE_GAUGES.items():
            print(f"{gauge} AWG - {diameter:.2f}mm diameter")
        
        while True:
            gauge = input("Select wire gauge (10-22): ").strip()
            if gauge in self.WIRE_GAUGES:
                parameters['wire_gauge'] = gauge
                break
            else:
                print("Error: Invalid wire gauge selection")
        
        # Boom material
        print("\nBOOM MATERIAL SELECTION")
        print("-" * 30)
        print("1. Wood (non-conductive)")
        print("2. Aluminum")
        print("3. Fiberglass")
        print("4. PVC")
        print("5. Carbon Fiber")
        
        boom_map = {'1': 'wood', '2': 'aluminum', '3': 'fiberglass', '4': 'pvc', '5': 'carbon_fiber'}
        while True:
            choice = input("Select boom material (1-5): ").strip()
            if choice in boom_map:
                parameters['boom_material'] = boom_map[choice]
                break
            else:
                print("Error: Invalid boom material selection")
        
        # Optimization target
        print("\nOPTIMIZATION TARGET")
        print("-" * 30)
        print("1. Maximum Gain")
        print("2. Wide Bandwidth")
        print("3. Front-to-Back Ratio")
        print("4. Balanced Performance")
        
        opt_map = {'1': 'gain', '2': 'bandwidth', '3': 'f2b', '4': 'balanced'}
        while True:
            choice = input("Select optimization target (1-4): ").strip()
            if choice in opt_map:
                parameters['optimize_for'] = opt_map[choice]
                break
            else:
                print("Error: Invalid optimization selection")
        
        # Units preference
        print("\nUNITS PREFERENCE")
        print("-" * 30)
        print("1. Metric (meters, centimeters)")
        print("2. Imperial (feet, inches)")
        
        while True:
            choice = input("Select units (1-2): ").strip()
            if choice == '1':
                parameters['units'] = 'metric'
                break
            elif choice == '2':
                parameters['units'] = 'imperial'
                break
            else:
                print("Error: Invalid units selection")
        
        return parameters

    def calculate_yagi(self, frequency, parameters):
        """Perform Yagi antenna calculations"""
        num_dirs = parameters['num_directors']
        wire_gauge = parameters['wire_gauge']
        boom_material = parameters['boom_material']
        optimize_for = parameters['optimize_for']
        
        # Basic calculations
        wavelength = self.SPEED_OF_light / (frequency * 1e6)
        wire_diameter = self.WIRE_GAUGES[wire_gauge] / 1000  # Convert to meters
        boom_factor = self.BOOM_CORRECTIONS[boom_material]
        
        # Enhanced end effect calculation
        end_effect = 0.0254 * math.log10(wavelength / (wire_diameter * 1000))
        
        # Initialize variables
        reflector_length = 0
        driven_length = 0
        director_lengths = []
        reflector_spacing = 0
        director_spacings = []
        gain = 0
        front_to_back = 0
        beamwidth = 0
        
        # Optimization-specific calculations
        if optimize_for == 'gain':
            # Optimized for maximum gain
            reflector_length = (0.482 * wavelength - end_effect) * boom_factor
            driven_length = (0.465 * wavelength - end_effect) * boom_factor
            reflector_spacing = 0.15 * wavelength
            
            for i in range(num_dirs):
                reduction = 0.005 + (i * 0.003)
                director_lengths.append((0.440 - reduction) * wavelength - end_effect * boom_factor)
                director_spacings.append(0.15 * wavelength + (i * 0.1 * wavelength))
            
            gain = 8.5 + (num_dirs * 1.8) - (num_dirs * 0.1 * num_dirs)
            front_to_back = 15 + (num_dirs * 2.5)
            beamwidth = max(25, 65 - (num_dirs * 4))
            
        elif optimize_for == 'bandwidth':
            # Optimized for wider bandwidth
            reflector_length = (0.475 * wavelength - end_effect) * boom_factor
            driven_length = (0.470 * wavelength - end_effect) * boom_factor
            reflector_spacing = 0.125 * wavelength
            
            for i in range(num_dirs):
                reduction = 0.003 + (i * 0.002)
                director_lengths.append((0.445 - reduction) * wavelength - end_effect * boom_factor)
                director_spacings.append(0.125 * wavelength + (i * 0.08 * wavelength))
            
            gain = 7.8 + (num_dirs * 1.6) - (num_dirs * 0.08 * num_dirs)
            front_to_back = 12 + (num_dirs * 2.2)
            beamwidth = max(30, 70 - (num_dirs * 3.5))
            
        elif optimize_for == 'f2b':
            # Optimized for front-to-back ratio
            reflector_length = (0.490 * wavelength - end_effect) * boom_factor
            driven_length = (0.463 * wavelength - end_effect) * boom_factor
            reflector_spacing = 0.18 * wavelength
            
            for i in range(num_dirs):
                reduction = 0.007 + (i * 0.004)
                director_lengths.append((0.435 - reduction) * wavelength - end_effect * boom_factor)
                director_spacings.append(0.16 * wavelength + (i * 0.12 * wavelength))
            
            gain = 7.2 + (num_dirs * 1.4) - (num_dirs * 0.06 * num_dirs)
            front_to_back = 18 + (num_dirs * 3.2)
            beamwidth = max(28, 72 - (num_dirs * 4.2))
            
        else:  # balanced
            # Balanced performance
            reflector_length = (0.478 * wavelength - end_effect) * boom_factor
            driven_length = (0.467 * wavelength - end_effect) * boom_factor
            reflector_spacing = 0.14 * wavelength
            
            for i in range(num_dirs):
                reduction = 0.004 + (i * 0.0025)
                director_lengths.append((0.442 - reduction) * wavelength - end_effect * boom_factor)
                director_spacings.append(0.14 * wavelength + (i * 0.09 * wavelength))
            
            gain = 8.0 + (num_dirs * 1.7) - (num_dirs * 0.09 * num_dirs)
            front_to_back = 14 + (num_dirs * 2.8)
            beamwidth = max(26, 67 - (num_dirs * 3.8))
        
        # Calculate additional parameters
        total_boom = reflector_spacing + (director_spacings[-1] if director_spacings else 0)
        input_impedance = 28 + (num_dirs * 4) + (reflector_spacing / wavelength * 50)
        
        # Apply realistic limits
        gain = min(gain, 20)
        front_to_back = min(front_to_back, 35)
        beamwidth = max(beamwidth, 15)
        
        return {
            'wavelength': wavelength,
            'reflector_length': reflector_length,
            'driven_length': driven_length,
            'director_lengths': director_lengths,
            'reflector_spacing': reflector_spacing,
            'director_spacings': director_spacings,
            'total_boom': total_boom,
            'gain': gain,
            'front_to_back': front_to_back,
            'beamwidth': beamwidth,
            'input_impedance': input_impedance,
            'wire_diameter': wire_diameter,
            'end_effect': end_effect
        }

    def format_length(self, meters, units):
        """Format length based on units preference"""
        if units == 'metric':
            if meters < 0.01:
                return f"{meters * 1000:.1f} mm"
            elif meters < 1:
                return f"{meters * 100:.1f} cm"
            else:
                return f"{meters:.3f} m"
        else:  # imperial
            inches = meters * 39.3701
            if inches < 12:
                return f"{inches:.2f}\""
            else:
                feet = int(inches // 12)
                remaining_inches = inches % 12
                return f"{feet}' {remaining_inches:.2f}\""

    def display_results(self, frequency, parameters, results):
        """Display calculation results in a formatted manner"""
        print("\n" + "=" * 70)
        print("                    CALCULATION RESULTS")
        print("=" * 70)
        
        # Basic information
        print(f"\nDesign Frequency: {frequency} MHz")
        print(f"Wavelength: {self.format_length(results['wavelength'], parameters['units'])}")
        print(f"Wire Gauge: {parameters['wire_gauge']} AWG ({self.WIRE_GAUGES[parameters['wire_gauge']]:.2f}mm)")
        print(f"Boom Material: {parameters['boom_material'].replace('_', ' ').title()}")
        print(f"Optimization: {parameters['optimize_for'].replace('f2b', 'Front-to-Back').replace('_', ' ').title()}")
        
        # Performance metrics
        print("\n" + "-" * 40)
        print("           PERFORMANCE METRICS")
        print("-" * 40)
        print(f"Estimated Gain:        {results['gain']:.1f} dBi")
        print(f"Front-to-Back Ratio:   {results['front_to_back']:.1f} dB")
        print(f"Beamwidth (approx):    {results['beamwidth']:.0f}°")
        print(f"Input Impedance:       {results['input_impedance']:.0f}Ω")
        
        # Element dimensions
        print("\n" + "-" * 40)
        print("           ELEMENT DIMENSIONS")
        print("-" * 40)
        print(f"Reflector Length:      {self.format_length(results['reflector_length'], parameters['units'])}")
        print(f"Driven Element Length: {self.format_length(results['driven_length'], parameters['units'])}")
        
        for i, length in enumerate(results['director_lengths']):
            print(f"Director {i+1} Length:     {self.format_length(length, parameters['units'])}")
        
        # Element spacing
        print("\n" + "-" * 40)
        print("        ELEMENT SPACING (center-to-center)")
        print("-" * 40)
        print(f"Reflector ← Driven:    {self.format_length(results['reflector_spacing'], parameters['units'])}")
        
        for i, spacing in enumerate(results['director_spacings']):
            print(f"Driven → Director {i+1}:  {self.format_length(spacing, parameters['units'])}")
        
        print(f"\nTotal Boom Length:     {self.format_length(results['total_boom'], parameters['units'])}")
        
        # Construction notes
        print("\n" + "-" * 40)
        print("           CONSTRUCTION NOTES")
        print("-" * 40)
        print("• Split driven element at center for feed connection")
        print("• Use a 1:1 balun for best SWR performance")
        print("• Ensure all elements are parallel and perpendicular to boom")
        print("• Fine-tune by adjusting element lengths ±2-3%")
        print("• Consider weatherproofing for outdoor installations")
        print(f"• End effect correction applied: {self.format_length(results['end_effect'], parameters['units'])}")
        
        if parameters['boom_material'] != 'wood':
            print(f"• Boom material correction factor: {self.BOOM_CORRECTIONS[parameters['boom_material']]}")

    def save_results(self, frequency, parameters, results):
        """Save results to a file"""
        filename = f"yagi_{frequency}MHz_{parameters['num_directors']}dir.txt"
        
        try:
            with open(filename, 'w') as f:
                f.write(f"Yagi Antenna Design - {frequency} MHz\n")
                f.write("=" * 50 + "\n\n")
                
                f.write(f"Design Parameters:\n")
                f.write(f"- Frequency: {frequency} MHz\n")
                f.write(f"- Directors: {parameters['num_directors']}\n")
                f.write(f"- Wire Gauge: {parameters['wire_gauge']} AWG\n")
                f.write(f"- Boom Material: {parameters['boom_material']}\n")
                f.write(f"- Optimization: {parameters['optimize_for']}\n\n")
                
                f.write(f"Performance:\n")
                f.write(f"- Gain: {results['gain']:.1f} dBi\n")
                f.write(f"- F/B Ratio: {results['front_to_back']:.1f} dB\n")
                f.write(f"- Beamwidth: {results['beamwidth']:.0f}°\n")
                f.write(f"- Impedance: {results['input_impedance']:.0f}Ω\n\n")
                
                f.write(f"Element Dimensions:\n")
                f.write(f"- Reflector: {self.format_length(results['reflector_length'], parameters['units'])}\n")
                f.write(f"- Driven Element: {self.format_length(results['driven_length'], parameters['units'])}\n")
                
                for i, length in enumerate(results['director_lengths']):
                    f.write(f"- Director {i+1}: {self.format_length(length, parameters['units'])}\n")
                
                f.write(f"\nElement Spacing:\n")
                f.write(f"- Reflector to Driven: {self.format_length(results['reflector_spacing'], parameters['units'])}\n")
                
                for i, spacing in enumerate(results['director_spacings']):
                    f.write(f"- Driven to Director {i+1}: {self.format_length(spacing, parameters['units'])}\n")
                
                f.write(f"\nTotal Boom Length: {self.format_length(results['total_boom'], parameters['units'])}\n")
            
            print(f"\nResults saved to: {filename}")
            
        except IOError as e:
            print(f"\nError saving file: {e}")

    def run(self):
        """Main application loop"""
        self.display_banner()
        
        try:
            # Get inputs
            frequency = self.get_frequency_input()
            parameters = self.get_design_parameters()
            
            # Perform calculations
            print("\nCalculating antenna dimensions...")
            results = self.calculate_yagi(frequency, parameters)
            
            # Display results
            self.display_results(frequency, parameters, results)
            
            # Offer to save results
            save_option = input("\nSave results to file? (y/n): ").lower()
            if save_option == 'y':
                self.save_results(frequency, parameters, results)
            
            # Offer to calculate another antenna
            another = input("\nCalculate another antenna? (y/n): ").lower()
            if another == 'y':
                print("\n" + "=" * 70)
                self.run()
            else:
                print("\nThank you for using the Advanced Yagi Calculator!")
                print("73, and happy antenna building!")
                
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            sys.exit(1)

def main():
    """Entry point"""
    calculator = YagiCalculator()
    calculator.run()

if __name__ == "__main__":
    main()
