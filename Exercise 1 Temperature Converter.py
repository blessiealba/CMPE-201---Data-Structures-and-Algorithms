# Exercise 1: Temperature Converter
# Create a program that converts temperatures between Celsius and Fahrenheit.

# Instructions:
# 1.	Ask the user to input a temperature.
# 2.	Ask the user to select the conversion type: from Celsius to Fahrenheit or from Fahrenheit to Celsius.
# 3.	Perform the appropriate conversion and print the result.

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Get user input
temp = float(input("Enter the temperature: "))
convert = input("Select conversion type (C to F / F to C): ").strip().upper()

# Perform the conversion based on user input
if convert == "C TO F":
    result = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is equal to {result:.2f}°F")
elif convert == "F TO C":
    result = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is equal to {result:.2f}°C")
else:
    print("Invalid! Please enter 'C to F' or 'F to C'.")