import streamlit as st

# App title
st.title("Unit Converter")

# Unit conversion
conversion_types = ["Length", "Weight", "Temperature", "Volume"]
conversion_choice = st.selectbox("Choose Conversion Type:", conversion_types)

# Length conversion
if conversion_choice == "Length":
    length_units = {"Meters": 1, "Kilometers": 1000, "Feet": 0.3048, "Inches": 0.0254, "Centimeters": 0.01}
    input_value = st.number_input("Enter Length Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", length_units.keys())
    to_unit = st.selectbox("To Unit:", length_units.keys())
    
    if st.button("Convert"):
        result = input_value * (length_units[from_unit] / length_units[to_unit])
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')

# Weight conversion
elif conversion_choice == "Weight":
    weight_units = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
    input_value = st.number_input("Enter Weight Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", weight_units.keys())
    to_unit = st.selectbox("To Unit:", weight_units.keys())
    
    if st.button("Convert"):
        result = input_value * (weight_units[from_unit] / weight_units[to_unit])
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')

# Temperature conversion
elif conversion_choice == "Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    input_value = st.number_input("Enter Temperature Value:", format="%.2f")
    from_unit = st.selectbox("From Unit:", temperature_units)
    to_unit = st.selectbox("To Unit:", temperature_units)
    
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
        return value
    
    if st.button("Convert"):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')

# Volume conversion
elif conversion_choice == "Volume":
    volume_units = {"Liters": 1, "Milliliters": 0.001, "Gallons": 3.78541, "Cups": 0.236588}
    input_value = st.number_input("Enter Volume Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", volume_units.keys())
    to_unit = st.selectbox("To Unit:", volume_units.keys())
    
    if st.button("Convert"):
        result = input_value * (volume_units[from_unit] / volume_units[to_unit])
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')

# Time conversion
elif conversion_choice == "Time":
    time_units = {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400}
    input_value = st.number_input("Enter Time Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", time_units.keys())
    to_unit = st.selectbox("To Unit:", time_units.keys())
    
    if st.button("Convert"):
        result = input_value * (time_units[from_unit] / time_units[to_unit])
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')
