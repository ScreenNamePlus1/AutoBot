import math
import sys
import os
from typing import Dict, List, Tuple, Optional

class NonIsolatedYagiCalculator:
    """Advanced Yagi antenna calculator for non-isolated aluminum booms with multiple optimization modes."""
    
    # Constants
    SPEED_OF_LIGHT = 299792458  # meters per second
    
    # Wire diameter lookup table (in mm)
    WIRE_GAUGES = {
        '10': 2.588,
        '12': 2.053,
        '14': 1.628,
        '16': 1.291,
        '18': 1.024,
        '20': 0.812,
        '22': 0.644
    }
    
    def __init__(self):
        self.frequency_mhz = 0.0
        self.num_directors = 0
        self.wire_gauge = '14'
        self.boom_diameter_mm = 25.0  # Default boom diameter in mm
        self.optimize_for = 'gain'
        self.units = 'metric'
        # Fixed for this calculator
        self.boom_material = 'aluminum_non_isolated'
        
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_header(self):
        """Print the application header."""
        print("=" * 70)
        print("          ADVANCED YAGI ANTENNA CALCULATOR FOR NON-ISOLATED ALUMINUM BOOMS v1.0")
        print("        Professional Amateur Radio Antenna Design Tool (Non-Isolated Elements)")
        print("=" * 70)
        print()
        
    def print_menu(self):
        """Print the main menu options."""
        print("MENU OPTIONS:")
        print("1. Set Frequency")
        print("2. Set Number of Directors")
        print("3. Select Wire Gauge")
        print("4. Set Boom Diameter (mm)")
        print("5. Choose Optimization Mode")
        print("6. Select Units (Metric/Imperial)")
        print("7. Calculate Antenna Dimensions")
        print("8. Show Current Settings")
        print("9. Export Results to File")
        print("0. Exit")
        print("-" * 40)
        
    def get_user_choice(self) -> str:
        """Get user menu choice with validation."""
        try:
            choice = input("Enter your choice (0-9): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            sys.exit(0)
            
    def set_frequency(self):
        """Set the operating frequency."""
        print("\nSET FREQUENCY")
        print("-" * 20)
        print("Common amateur radio frequencies:")
        print("  - 28.5 MHz (10m)")
        print("  - 50.0 MHz (6m)")  
        print("  - 144.0 MHz (2m)")
        print("  - 432.0 MHz (70cm)")
        print("  - 1296.0 MHz (23cm)")
        print()
        
        while True:
            try:
                freq = float(input("Enter frequency in MHz (e.g., 144.5): "))
                if freq <= 0:
                    print("Error: Frequency must be positive!")
                    continue
                if freq < 1 or freq > 10000:
                    print("Warning: Frequency outside typical amateur radio range!")
                    confirm = input("Continue anyway? (y/n): ").lower()
                    if confirm != 'y':
                        continue
                        
                self.frequency_mhz = freq
                print(f"✓ Frequency set to {freq} MHz")
                break
                
            except ValueError:
                print("Error: Please enter a valid number!")
                
    def set_directors(self):
        """Set the number of directors."""
        print("\nSET NUMBER OF DIRECTORS")
        print("-" * 25)
        print("Director count guidelines:")
        print("  - 0: Simple dipole with reflector (~5 dBi)")
        print("  - 1-3: Compact beam antenna (7-10 dBi)")
        print("  - 4-6: Standard gain antenna (11-14 dBi)")
        print("  - 7-10: High gain antenna (15-17 dBi)")
        print("  - 11+: Very long boom, diminishing returns")
        print()
        
        while True:
            try:
                dirs = int(input("Enter number of directors (0-20): "))
                if dirs < 0:
                    print("Error: Number of directors cannot be negative!")
                    continue
                if dirs > 20:
                    print("Warning: Very high director count may not be practical!")
                    confirm = input("Continue anyway? (y/n): ").lower()
                    if confirm != 'y':
                        continue
                        
                self.num_directors = dirs
                print(f"✓ Number of directors set to {dirs}")
                break
                
            except ValueError:
                print("Error: Please enter a valid integer!")
                
    def set_wire_gauge(self):
        """Set the wire gauge."""
        print("\nSELECT WIRE GAUGE")
        print("-" * 18)
        print("Available wire gauges (AWG):")
        for gauge, diameter in self.WIRE_GAUGES.items():
            print(f"  {gauge} AWG - {diameter}mm diameter")
        print()
        
        while True:
            gauge = input("Enter wire gauge (10, 12, 14, 16, 18, 20, 22): ").strip()
            if gauge in self.WIRE_GAUGES:
                self.wire_gauge = gauge
                diameter = self.WIRE_GAUGES[gauge]
                print(f"✓ Wire gauge set to {gauge} AWG ({diameter}mm diameter)")
                break
            else:
                print("Error: Invalid wire gauge! Please choose from the list.")
                
    def set_boom_diameter(self):
        """Set the boom diameter in mm."""
        print("\nSET BOOM DIAMETER")
        print("-" * 18)
        print("Enter the diameter of the aluminum boom in mm.")
        print("Typical values: 20-50 mm")
        print()
        
        while True:
            try:
                diam = float(input("Enter boom diameter in mm (e.g., 25.0): "))
                if diam <= 0:
                    print("Error: Diameter must be positive!")
                    continue
                if diam > 100:
                    print("Warning: Very large boom diameter may not be accurate!")
                    confirm = input("Continue anyway? (y/n): ").lower()
                    if confirm != 'y':
                        continue
                        
                self.boom_diameter_mm = diam
                print(f"✓ Boom diameter set to {diam} mm")
                break
                
            except ValueError:
                print("Error: Please enter a valid number!")
                
    def set_optimization(self):
        """Set the optimization mode."""
        print("\nCHOOSE OPTIMIZATION MODE")
        print("-" * 25)
        print("Optimization modes:")
        print("  1. Maximum Gain - Optimizes for highest forward gain")
        print("  2. Wide Bandwidth - Better SWR across frequency range")
        print("  3. Front-to-Back Ratio - Maximum rejection of rear signals")
        print()
        
        options = ['gain', 'bandwidth', 'f2b']
        option_names = ['Maximum Gain', 'Wide Bandwidth', 'Front-to-Back Ratio']
        
        while True:
            try:
                choice = int(input("Enter choice (1-3): "))
                if 1 <= choice <= 3:
                    self.optimize_for = options[choice - 1]
                    print(f"✓ Optimization set to {option_names[choice - 1]}")
                    break
                else:
                    print("Error: Invalid choice!")
            except ValueError:
                print("Error: Please enter a valid number!")
                
    def set_units(self):
        """Set the measurement units."""
        print("\nSELECT UNITS")
        print("-" * 12)
        print("1. Metric (meters, centimeters, millimeters)")
        print("2. Imperial (feet, inches)")
        print()
        
        while True:
            try:
                choice = int(input("Enter choice (1-2): "))
                if choice == 1:
                    self.units = 'metric'
                    print("✓ Units set to Metric")
                    break
                elif choice == 2:
                    self.units = 'imperial'
                    print("✓ Units set to Imperial")
                    break
                else:
                    print("Error: Invalid choice!")
            except ValueError:
                print("Error: Please enter a valid number!")
                
    def show_settings(self):
        """Display current settings."""
        print("\nCURRENT SETTINGS")
        print("-" * 18)
        print(f"Frequency: {self.frequency_mhz} MHz")
        print(f"Directors: {self.num_directors}")
        print(f"Wire Gauge: {self.wire_gauge} AWG ({self.WIRE_GAUGES[self.wire_gauge]}mm)")
        print(f"Boom Material: Aluminum (Non-Isolated)")
        print(f"Boom Diameter: {self.boom_diameter_mm} mm")
        print(f"Optimization: {self.optimize_for.replace('_', ' ').title()}")
        print(f"Units: {self.units.title()}")
        print()
        
    def convert_length(self, meters: float) -> str:
        """Convert length to appropriate units with formatting."""
        if self.units == 'metric':
            if meters < 0.01:
                return f"{meters * 1000:.1f} mm"
            elif meters < 1:
                return f"{meters * 100:.1f} cm"
            else:
                return f"{meters:.3f} m"
        else:  # imperial
            inches = meters * 39.3701
            if inches < 12:
                return f'{inches:.2f}"'
            else:
                feet = int(inches // 12)
                remaining_inches = inches % 12
                return f"{feet}' {remaining_inches:.2f}\""
                
    def calculate_antenna(self) -> Optional[Dict]:
        """Calculate antenna dimensions and performance for non-isolated aluminum boom."""
        if self.frequency_mhz <= 0:
            print("Error: Please set a valid frequency first!")
            return None
            
        # Basic calculations
        wavelength = self.SPEED_OF_LIGHT / (self.frequency_mhz * 1e6)
        wire_diameter = self.WIRE_GAUGES[self.wire_gauge] / 1000  # Convert mm to m
        
        # Enhanced end effect calculation
        end_effect = 0.0254 * math.log10(wavelength / (wire_diameter * 1000))
        
        # Calculate boom correction using DL6WU formula for insulated, then double for non-isolated
        lambda_m = wavelength
        bd_mm = self.boom_diameter_mm
        ratio = bd_mm / (lambda_m * 1000)
        bc_ins_mm = (12.5975 - 114.5 * ratio) * (ratio ** 2) * (lambda_m * 1000)
        bc_mm = 2 * bc_ins_mm  # Double for non-isolated (conductive through boom)
        bc_m = bc_mm / 1000  # Convert to meters
        
        # Optimization-specific calculations
        if self.optimize_for == 'gain':
            # Optimized for maximum gain
            reflector_length = 0.482 * wavelength - end_effect + bc_m  # Add boom correction
            driven_length = 0.465 * wavelength - end_effect  # No boom correction for driven (elevated)
            reflector_spacing = 0.15 * wavelength
            
            # Progressive director sizing
            director_lengths = []
            director_spacings = []
            for i in range(self.num_directors):
                reduction = 0.005 + (i * 0.003)
                dir_len = 0.440 - reduction
                director_lengths.append(dir_len * wavelength - end_effect + bc_m)  # Add boom correction
                director_spacings.append(0.15 * wavelength + (i * 0.1 * wavelength))
                
            gain = 8.5 + (self.num_directors * 1.8) - (self.num_directors * 0.1 * self.num_directors)
            front_to_back = 15 + (self.num_directors * 2.5)
            beamwidth = max(25, 65 - (self.num_directors * 4))
            
        elif self.optimize_for == 'bandwidth':
            # Optimized for wider bandwidth
            reflector_length = 0.475 * wavelength - end_effect + bc_m
            driven_length = 0.470 * wavelength - end_effect
            reflector_spacing = 0.125 * wavelength
            
            director_lengths = []
            director_spacings = []
            for i in range(self.num_directors):
                reduction = 0.003 + (i * 0.002)
                dir_len = 0.445 - reduction
                director_lengths.append(dir_len * wavelength - end_effect + bc_m)
                director_spacings.append(0.125 * wavelength + (i * 0.08 * wavelength))
                
            gain = 7.8 + (self.num_directors * 1.6) - (self.num_directors * 0.08 * self.num_directors)
            front_to_back = 12 + (self.num_directors * 2.2)
            beamwidth = max(30, 70 - (self.num_directors * 3.5))
            
        else:  # front-to-back ratio
            reflector_length = 0.490 * wavelength - end_effect + bc_m
            driven_length = 0.463 * wavelength - end_effect
            reflector_spacing = 0.18 * wavelength
            
            director_lengths = []
            director_spacings = []
            for i in range(self.num_directors):
                reduction = 0.007 + (i * 0.004)
                dir_len = 0.435 - reduction
                director_lengths.append(dir_len * wavelength - end_effect + bc_m)
                director_spacings.append(0.16 * wavelength + (i * 0.12 * wavelength))
                
            gain = 7.2 + (self.num_directors * 1.4) - (self.num_directors * 0.06 * self.num_directors)
            front_to_back = 18 + (self.num_directors * 3.2)
            beamwidth = max(28, 72 - (self.num_directors * 4.2))
            
        # Apply realistic limits
        gain = min(gain, 20)
        front_to_back = min(front_to_back, 35)
        beamwidth = max(beamwidth, 15)
        
        # Calculate additional parameters
        total_boom = reflector_spacing + (sum(director_spacings) if director_spacings else 0)
        input_impedance = 28 + (self.num_directors * 4) + (reflector_spacing / wavelength * 50)
        
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
            'boom_correction_mm': bc_mm
        }
        
    def display_results(self, results: Dict):
        """Display calculation results."""
        print("\n" + "=" * 60)
        print("                    CALCULATION RESULTS")
        print("=" * 60)
        
        # Performance metrics
        print("\nESTIMATED PERFORMANCE:")
        print("-" * 22)
        print(f"Forward Gain:        {results['gain']:.1f} dBi")
        print(f"Front-to-Back Ratio: {results['front_to_back']:.1f} dB")
        print(f"Beamwidth (3dB):     {results['beamwidth']:.0f}°")
        print(f"Input Impedance:     {results['input_impedance']:.0f} Ω")
        print(f"Wavelength:          {self.convert_length(results['wavelength'])}")
        
        # Element dimensions
        print("\nELEMENT DIMENSIONS:")
        print("-" * 19)
        print(f"Reflector:           {self.convert_length(results['reflector_length'])}")
        print(f"Driven Element:      {self.convert_length(results['driven_length'])}")
        
        for i, length in enumerate(results['director_lengths']):
            print(f"Director {i+1}:         {self.convert_length(length)}")
            
        # Spacing
        print("\nELEMENT SPACING (center-to-center):")
        print("-" * 35)
        print(f"Reflector ← Driven:  {self.convert_length(results['reflector_spacing'])}")
        
        for i, spacing in enumerate(results['director_spacings']):
            print(f"Driven → Director {i+1}: {self.convert_length(spacing)}")
            
        print(f"\nTOTAL BOOM LENGTH:   {self.convert_length(results['total_boom'])}")
        print(f"Boom Correction Applied: {results['boom_correction_mm']:.2f} mm (added to reflector and directors)")
        
        # Construction notes
        print("\nCONSTRUCTION NOTES:")
        print("-" * 19)
        print("• This calculator assumes non-isolated elements (electrically connected to aluminum boom)")
        print("• Driven element is assumed elevated above boom - no correction applied")
        print("• Split driven element at center for feed connection")
        print("• Use 1:1 balun for best SWR performance")
        print("• All elements must be parallel and perpendicular to boom")
        print("• Fine-tune by adjusting element lengths ±2-3%")
        print("• Consider weatherproofing for outdoor installations")
        print("• Elements pass through boom without insulators")
        
        # Optimization note
        opt_name = self.optimize_for.replace('_', ' ').title()
        print(f"\n* Optimized for: {opt_name}")
        
    def export_results(self, results: Dict):
        """Export results to a text file."""
        if not results:
            print("Error: No results to export! Please calculate first.")
            return
            
        filename = f"non_isolated_yagi_{self.frequency_mhz}MHz_{self.num_directors}dir.txt"
        
        try:
            with open(filename, 'w') as f:
                f.write("ADVANCED YAGI ANTENNA CALCULATOR FOR NON-ISOLATED ALUMINUM BOOMS - RESULTS\n")
                f.write("=" * 50 + "\n\n")
                
                f.write("DESIGN PARAMETERS:\n")
                f.write("-" * 18 + "\n")
                f.write(f"Frequency: {self.frequency_mhz} MHz\n")
                f.write(f"Directors: {self.num_directors}\n")
                f.write(f"Wire Gauge: {self.wire_gauge} AWG\n")
                f.write(f"Boom Material: Aluminum (Non-Isolated)\n")
                f.write(f"Boom Diameter: {self.boom_diameter_mm} mm\n")
                f.write(f"Optimization: {self.optimize_for.replace('_', ' ').title()}\n")
                f.write(f"Units: {self.units.title()}\n\n")
                
                f.write("PERFORMANCE:\n")
                f.write("-" * 12 + "\n")
                f.write(f"Forward Gain: {results['gain']:.1f} dBi\n")
                f.write(f"Front-to-Back: {results['front_to_back']:.1f} dB\n")
                f.write(f"Beamwidth: {results['beamwidth']:.0f}°\n")
                f.write(f"Input Impedance: {results['input_impedance']:.0f} Ω\n\n")
                
                f.write("ELEMENT DIMENSIONS:\n")
                f.write("-" * 19 + "\n")
                f.write(f"Reflector: {self.convert_length(results['reflector_length'])}\n")
                f.write(f"Driven Element: {self.convert_length(results['driven_length'])}\n")
                
                for i, length in enumerate(results['director_lengths']):
                    f.write(f"Director {i+1}: {self.convert_length(length)}\n")
                    
                f.write("\nELEMENT SPACING:\n")
                f.write("-" * 16 + "\n")
                f.write(f"Reflector ← Driven: {self.convert_length(results['reflector_spacing'])}\n")
                
                for i, spacing in enumerate(results['director_spacings']):
                    f.write(f"Driven → Director {i+1}: {self.convert_length(spacing)}\n")
                    
                f.write(f"\nTotal Boom Length: {self.convert_length(results['total_boom'])}\n")
                f.write(f"Boom Correction: {results['boom_correction_mm']:.2f} mm (added to reflector and directors)\n")
                
            print(f"✓ Results exported to {filename}")
            
        except IOError as e:
            print(f"Error exporting file: {e}")
            
    def run(self):
        """Main application loop."""
        results = None
        
        while True:
            self.clear_screen()
            self.print_header()
            self.print_menu()
            
            choice = self.get_user_choice()
            
            if choice == '0':
                print("\nThank you for using Non-Isolated Yagi Calculator!")
                sys.exit(0)
                
            elif choice == '1':
                self.set_frequency()
                
            elif choice == '2':
                self.set_directors()
                
            elif choice == '3':
                self.set_wire_gauge()
                
            elif choice == '4':
                self.set_boom_diameter()
                
            elif choice == '5':
                self.set_optimization()
                
            elif choice == '6':
                self.set_units()
                
            elif choice == '7':
                results = self.calculate_antenna()
                if results:
                    self.display_results(results)
                    
            elif choice == '8':
                self.show_settings()
                
            elif choice == '9':
                self.export_results(results)
                
            else:
                print("Invalid choice! Please enter 0-9.")
                
            if choice != '7':  # Don't pause after showing results
                input("\nPress Enter to continue...")


def main():
    """Main entry point."""
    try:
        calculator = NonIsolatedYagiCalculator()
        calculator.run()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
