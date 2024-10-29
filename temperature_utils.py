# temperature_utils.py

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in degrees Celsius.
    
    Returns:
    float: Temperature in degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Parameters:
    fahrenheit (float): Temperature in degrees Fahrenheit.
    
    Returns:
    float: Temperature in degrees Celsius.
    """
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """
    Convert Celsius to Kelvin.
    
    Parameters:
    celsius (float): Temperature in degrees Celsius.
    
    Returns:
    float: Temperature in Kelvin.
    """
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """
    Convert Kelvin to Celsius.
    
    Parameters:
    kelvin (float): Temperature in Kelvin.
    
    Returns:
    float: Temperature in degrees Celsius.
    """
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """
    Convert Fahrenheit to Kelvin.
    
    Parameters:
    fahrenheit (float): Temperature in degrees Fahrenheit.
    
    Returns:
    float: Temperature in Kelvin.
    """
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    """
    Convert Kelvin to Fahrenheit.
    
    Parameters:
    kelvin (float): Temperature in Kelvin.
    
    Returns:
    float: Temperature in degrees Fahrenheit.
    """
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)
