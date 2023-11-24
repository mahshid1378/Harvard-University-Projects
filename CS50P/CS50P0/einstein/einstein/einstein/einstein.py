def convert_mass_to_energy():
    mass = int(input("Enter the mass in kilograms: "))

    # Energy conversion: E = mc^2
    c = 300000000  # Speed of light in meters per second
    energy = mass * c**2

    print("Equivalent energy in joules:", energy)

convert_mass_to_energy()