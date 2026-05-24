# agritrack bf - part 1
# foundations: data types, inputs, validation, arithmetic, summary
# done by NOMBRE Carelle

# this function asks for a number and makes sure it is valid
# it loops until the user enters something correct
def ask_number(message):
    while True:
        try:
            val = float(input(message))
            if val < 0:
                print("no negative values. try again.")
                continue
            return val
        except:
            print("that's not a number. try again.")


print("=== agritrack bf ===")
print("enter your field data below")
print()

# --- collecting inputs ---
# str inputs
farmer_name = input("farmer name: ")
field_name = input("field name: ")
crop_type = input("crop type (sorghum, millet, cotton, cowpea): ")

# float inputs using ask_number so the program never crashes
field_area = ask_number("field area in hectares: ")
seeds_kg = ask_number("seeds used in kg: ")
seeds_cost = ask_number("cost of seeds in fcfa: ")
fertilizer_cost = ask_number("cost of fertilizer in fcfa: ")
labor_cost = ask_number("cost of labor in fcfa: ")
harvest_kg = ask_number("total harvest in kg: ")
sale_price_kg = ask_number("sale price per kg in fcfa: ")

# int input
duration_months = int(ask_number("growing duration in months: "))

# bool input - correct way, not bool(input(...))
while True:
    ans = input("did you use irrigation? (yes/no): ").lower().strip()
    if ans == "yes":
        irrigation = True
        break
    elif ans == "no":
        irrigation = False
        break
    else:
        print("answer yes or no only.")

# --- calculations ---
# 1. total production cost
total_cost = seeds_cost + fertilizer_cost + labor_cost

# 2. yield per hectare
yield_per_ha = harvest_kg / field_area

# 3. total revenue
revenue = harvest_kg * sale_price_kg

# 4. profit or loss
profit = revenue - total_cost

# 5. profit margin
if total_cost > 0:
    margin_percent = (profit / total_cost) * 100
else:
    margin_percent = 0.0

# --- summary screen ---
print()
print("=" * 43)
print("         season summary")
print("=" * 43)
print(f"farmer:     {farmer_name}")
print(f"field:      {field_name}")
print(f"crop:       {crop_type}")
print(f"area:       {field_area} ha")
print(f"duration:   {duration_months} months")
print(f"irrigation: {'yes' if irrigation else 'no'}")
print()
print(f"total cost: {total_cost:.2f} fcfa")
print(f"harvest:    {harvest_kg:.2f} kg")
print(f"yield:      {yield_per_ha:.2f} kg/ha")
print(f"revenue:    {revenue:.2f} fcfa")
print(f"profit:     {profit:.2f} fcfa")
print(f"margin:     {margin_percent:.2f}%")
print()
if profit > 0:
    print("result: profit")
elif profit < 0:
    print("result: loss")
else:
    print("result: break even")
print("=" * 43)
print("thank you for using agritrack bf")
