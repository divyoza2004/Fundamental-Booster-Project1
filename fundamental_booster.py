from datetime import datetime 
print("Welconme to the Interactive Personal Data Collector!\n") 
name = input("Enter your name: ")
age = int(input("Enter your age: ")) 
height = float(input("Enter your height in meters: ")) 
fav = int(input("Enter your favourite number: ")) 
birthday = datetime.now().year - age    
print("\nThank you! Here is the information we collected: ")
print(f"\nName: {name} (Type: {type(name)}, Memory address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory address: {id(height)})")  
print(f"Favourite number: {fav} (Type: {type(fav)}, Memory address: {id(fav)})")
print(f"\nYour birthday year is approximately: {birthday}")
print(f"\nThank you for using the Personal Data Collector. Goodbbye!")
