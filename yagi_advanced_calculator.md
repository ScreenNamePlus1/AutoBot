import math

def yagi_calculator():
    """
    Calculates the dimensions for a Yagi antenna with a variable number of directors.
    """
    print("Multi-Element Yagi Antenna Calculator")
    print("-------------------------------------")
    
    # Constants
    speed_of_light = 299792458  # meters per second
    wire_diameter_m = 0.001628  # 14 gauge copper wire in meters

    try:
        # Get user input for the desired frequency and number of directors
        frequency_mhz = float(input("Enter the desired frequency in MHz (e.g., 144.5): "))
        num_directors = int(input("Enter the number of directors you want to add (e.g., 5, 10, etc.): "))
        
        if frequency_mhz <= 0 or num_directors < 0:
            print("Invalid input. Frequency must be a positive number and the number of directors must be non-negative.")
            return
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # Convert frequency from MHz to Hz
    frequency_hz = frequency_mhz * 1_000_000
    
    # Calculate the wavelength (lambda) in meters
    wavelength_m = speed_of_light / frequency_hz

    # Adjust for the wire's diameter
    end_effect_factor = 0.04 * math.log(wavelength_m / wire_diameter_m)
    
    # Calculate element lengths (in meters)
    driven_element_m = (0.473 * wavelength_m) - end_effect_factor
    reflector_m = (0.495 * wavelength_m) - end_effect_factor
    
    # Calculate spacing (in meters)
    reflector_to_driven_m = 0.125 * wavelength_m
    driven_to_director_m = 0.125 * wavelength_m

    # Calculate gain in dBi (this is a rough approximation)
    if num_directors >= 1:
        gain_dBi = 7.0 + (num_directors * 1.5)
    else:
        gain_dBi = 5.0
    
    # Display results in inches and meters
    print("\n-------------------")
    print("Calculated Dimensions:")
    print("-------------------")
    print(f"**Driven Element Length:** {driven_element_m * 39.37:.2f} inches ({driven_element_m:.3f} m)")
    print(f"**Reflector Length:** {reflector_m * 39.37:.2f} inches ({reflector_m:.3f} m)")
    
    # Loop to calculate and display each director's dimensions
    for i in range(1, num_directors + 1):
        director_m = (0.440 * wavelength_m) - end_effect_factor
        director_length_adj = (i * 0.005) * wavelength_m
        director_m -= director_length_adj
        
        print(f"**Director {i} Length:** {director_m * 39.37:.2f} inches ({director_m:.3f} m)")

    print("\n-------------------")
    print("Calculated Spacing (center-to-center):")
    print("-------------------")
    print(f"**Reflector to Driven Element:** {reflector_to_driven_m * 39.37:.2f} inches ({reflector_to_driven_m:.3f} m)")
    
    # All directors are assumed to be spaced equally in this simple model
    for i in range(1, num_directors + 1):
        director_spacing_in = driven_to_director_m * 39.37 * i
        director_spacing_m = driven_to_director_m * i
        print(f"**Driven Element to Director {i}:** {director_spacing_in:.2f} inches ({director_spacing_m:.3f} m)")
    
    print("\n-------------------")
    print("Estimated Performance:")
    print("-------------------")
    print(f"**Estimated Gain:** {gain_dBi:.2f} dBi")
    print(f"Your calculated wavelength for {frequency_mhz} MHz is {wavelength_m:.2f} meters.")

if __name__ == "__main__":
    yagi_calculator()
