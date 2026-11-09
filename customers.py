print("--- exercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])


print("--- exercise 2 ---")
customer["phone"] = "555-5555"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["name"]
print(customer)

print(customer.get("ytd_spend", 0))

print("--- exercise 3 ---")
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print("KeyError:", error)

print("--- exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

print("--- exercise 5 ---")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.1, 
    "platinum": 0.15
    }

purchase_amount = 200
discount = tier_discounts.get(customer["tier"], 0)
final_price = purchase_amount * (1 - discount)
print("tier:", customer["tier"])
print(f"discount: {discount * 100}%")
print(f"final price: ${final_price:.2f}")

print("--- exercise 6 ---")
customer = [
    {"name": "bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "dave", "tier": "platinum", "ytd_spend": 450},
]

for record in customer:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}) - ${record['ytd_spend']}")

print("--- exercise 7 ---")
catolog = {
    "widget a": {"price": 9.99, "stock": 150},
    "gadget b": {"price": 49.99, "stock": 8},
}
for name, details in catolog.items():
    if details["stock"] < 20:
        print(f"LOW ASF YO: {name} - only {details['stock']} left")

print("--- exercise 8 ---")
transactions = [
    {"region":"sounth", "amount": 300},
    {"region":"north", "amount": 150},
    {"region":"south", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]}")


#relection 1
#I can use .get() to access a value in a dictionary without raising an error if the key does not exist. This is useful for providing default values and avoiding KeyError exceptions.


#reflection2
#python is more useful or large data sets because it can handle complex data structures like dictionaries and lists, allowing for efficient data manipulation and analysis. It also has a wide range of libraries and tools for data processing, making it suitable for tasks like data cleaning, transformation, and visualization.