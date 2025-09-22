print("Welcome! This app helps you calculate your heart rate")
age = int(input("Enter your age: "))
max_heart_rate = 220 - age
print("Your maximum heart rate is: ", max_heart_rate)
low_heart_rate_range = max_heart_rate * 0.60
high_heart_rate_range = max_heart_rate * 0.85
print("Your range of heart rate (LOW) is: ", low_heart_rate_range)
print("Your range of heart rate (HIGH) is: ", high_heart_rate_range)