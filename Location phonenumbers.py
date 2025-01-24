# pip install phonenumbers

import phonenumbers 
from phonenumbers import geocoder 

# Example of phone numbers
phone_number1 = phonenumbers.parse("+34612345678") 
phone_number2 = phonenumbers.parse("+15149876543")  
phone_number3 = phonenumbers.parse("+8613988887777")  
phone_number4 = phonenumbers.parse("+966552345678")
phone_number5 = phonenumbers.parse("+41791234567")

# Get the associated location
print("\nPhone Number Locations:\n")
print(f"Number 1: {geocoder.description_for_number(phone_number1, 'en')}")  
print(f"Number 2: {geocoder.description_for_number(phone_number2, 'en')}")
print(f"Number 3: {geocoder.description_for_number(phone_number3, 'en')}")
print(f"Number 4: {geocoder.description_for_number(phone_number4, 'en')}")
print(f"Number 5: {geocoder.description_for_number(phone_number5, 'en')}")
