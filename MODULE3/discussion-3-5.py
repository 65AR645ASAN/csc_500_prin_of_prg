# List of average costs of items (e.g., [potatoes, milk]) in different states
average_costs = [
    {"state": "State1", "potatoes": 2.50, "milk": 5.00},
    {"state": "State2", "potatoes": 2.70, "milk": 4.80},
    {"state": "State3", "potatoes": 2.45, "milk": 5.10},
]

# Iterating over the list to print each state's average cost for potatoes and milk
for item in average_costs:
    state = item["state"]
    potatoes_price = item["potatoes"]
    milk_price = item["milk"]
    print(f"In {state}, the average price of potatoes is ${potatoes_price} and milk is ${milk_price}.")

# List of withdrawals, each entry includes month, day, amount, and vendor
withdrawals = [
    {"month": "January", "day": 15, "amount": 50.00, "vendor": "Grocery Store"},
    {"month": "February", "day": 10, "amount": 20.00, "vendor": "Coffee Shop"},
    {"month": "March", "day": 5, "amount": 100.00, "vendor": "Electronics Store"},
]

# Iterating over the list to print details of each withdrawal
for withdrawal in withdrawals:
    month = withdrawal["month"]
    day = withdrawal["day"]
    amount = withdrawal["amount"]
    vendor = withdrawal["vendor"]
    print(f"On {day} {month}, a withdrawal of ${amount} was made at {vendor}.")

# List of cookie sales data, including region and sales of different flavors
cookie_sales = [
    {"region": "North", "chocolate_chip": 120, "oatmeal_raisin": 85},
    {"region": "South", "chocolate_chip": 150, "oatmeal_raisin": 90},
    {"region": "East", "chocolate_chip": 130, "oatmeal_raisin": 95},
]

# Iterating over the list to print sales details for each region
for sale in cookie_sales:
    region = sale["region"]
    chocolate_chip_sales = sale["chocolate_chip"]
    oatmeal_raisin_sales = sale["oatmeal_raisin"]
    print(f"In the {region} region, {chocolate_chip_sales} chocolate chip cookies and {oatmeal_raisin_sales} oatmeal raisin cookies were sold.")
