# inventory.py
# authror: Saydie Hendrix 
# Module 10 Lab: Inventory List Manager

# Exercise 1

print("--- Exercise1: Build a List ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))

# Exercise 2 - Index Practice 

print("--- Exercise 2: Index Practice ---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory)//2
print(inventory[middle]) #grabs the middle item

# Excersie 3 - Slicing 

print("--- Exercise 3: List Slicing ---")

print(inventory[:3]) # Always grabs the first item
print(inventory[-2:]) # Grabs the last two items
print(inventory[::2]) 

# Excersie 4 - Modify 

print("--- Exercise 4: List Methods ---")

inventory.append("envelope")
print(inventory)


inventory.remove("tape")
print(inventory)

inventory.sort() # sorts in alphapatical order
print(inventory)

# exercise 5 - Tuple Comparsion 

print("--- Excercise 5: Tuple Comparsion ---")
coords = (40.7128, -71.0060)

# coords[0] = 99 

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuple protects cordinates from being change by accident")


# Exercise 6 

print("---Excercise 6: List Average Sales ---")
sales = [100,250,75,480,200]
total = sum(sales)
count = len(sales)
average = total/count
print(f"Total sales: {total }")
print(f"Number of sales: {count}")
print(f"Average Slaes: {average}")
print(f"Best Sale: {max(sales)}")
print(f"Worst Sale: {min(sales)}")

# Exercise 7 - Accumulator Pattern

print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99,14.99,4.99,24.99,1.99]

discounted = []
for prcie in prices:
    discounted.append(round(prcie * 0.9, 2))

print(prices)
print(discounted)

# Excercise 8 

print("---Excercie8: Filter---")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(sales)}")
print(f"Average: {sum(high_sales)/len(high_sales):.2f}")
      
# The most surprising thing is that a Python list variable doesn’t store the list itself.
# At my hostess job had to manually reorder long waitlists in Excel and a simple Python list could’ve updated and sorted those names automatically.