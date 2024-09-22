# Exercise 2: Ohm’s Law Calculator

# Instructions:
# 1.	Ask the user what they want to calculate: Voltage, Current, or Resistance.
# 2.	Based on their choice, prompt the user to input the appropriate values.
# 3.	Use Ohm's Law to calculate the missing variable and display the result.
# 4.	Handle cases where division by zero might occur.

# Function to calculate voltage using Ohm's Law (V = I * R)
def calculate_voltage(current, resistance):
    return current * resistance

# Function to calculate current using Ohm's Law (I = V / R)
def calculate_current(voltage, resistance):
    # Handle division by zero
    if resistance == 0:
        return "Invalid! Resistance cannot be zero."
    return voltage / resistance

# Function to calculate resistance using Ohm's Law (R = V / I)
def calculate_resistance(voltage, current):
    # Handle division by zero
    if current == 0:
        return "Invalid! Current cannot be zero."
    return voltage / current

# Ask the user what they want to calculate
choice = input("What do you want to calculate? (Voltage / Current / Resistance): ").strip().lower()

# Perform the appropriate calculation based on the user's choice
if choice == "voltage":
    current = float(input("Enter the current (I) in amperes: "))
    resistance = float(input("Enter the resistance (R) in ohms: "))
    voltage = calculate_voltage(current, resistance)
    print(f"The voltage (V) is: {voltage:.2f} volts")

elif choice == "current":
    voltage = float(input("Enter the voltage (V) in volts: "))
    resistance = float(input("Enter the resistance (R) in ohms: "))
    result = calculate_current(voltage, resistance)
    print(f"The current (I) is: {result:.2f} amperes")

elif choice == "resistance":
    voltage = float(input("Enter the voltage (V) in volts: "))
    current = float(input("Enter the current (I) in amperes: "))
    result = calculate_resistance(voltage, current)
    print(f"The resistance (R) is: {result:.2f} ohms")

else:
    print("Invalid choice! Please select 'Voltage', 'Current', or 'Resistance'.")