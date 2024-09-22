print("Temperature Converter")
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")
choice = input("Enter 1 or 2 based on the conversion you want: ")
if choice =='1':
    celcius = float(input("Enter your Temperature in celsius: "))
    fah=(celcius*9/5)+32
    print(f"{celcius }°C is equal to {fah}°F")
elif choice == '2':
    fah = float(input("Enter your Temperature in Fahrenheit: "))
    celcius = (fah-32)*5/9
    print(f"{fah}°F is equal to {celcius}°C")
    
else:
    print("Invalid choice.")