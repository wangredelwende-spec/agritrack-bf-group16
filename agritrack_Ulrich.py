
# --- parent class ---

class Field:
    def __init__(self, farmer, field_name, crop, area, months, irrigation,
                 seeds_kg, seeds_cost, fertilizer_cost, labor_cost,
                 harvest_kg, price_kg):
        # store all the basic data about the field
        self.farmer = farmer
        self.field_name = field_name
        self.crop = crop
        self.area = area
        self.months = months
        self.irrigation = irrigation
        self.seeds_kg = seeds_kg
        self.seeds_cost = seeds_cost
        self.fertilizer_cost = fertilizer_cost
        self.labor_cost = labor_cost
        self.harvest_kg = harvest_kg
        self.price_kg = price_kg

    # total production cost: seeds + fertilizer + labor
    def total_cost(self):
        return self.seeds_cost + self.fertilizer_cost + self.labor_cost

    
    # multiplies harvest quantity by price per kg for revenue
    def revenue(self):
        return self.harvest_kg * self.price_kg

    # For profit or loss
    # revenue minus total cost
    def profit(self):
        return self.revenue() - self.total_cost()

    # For yield per hectare
    # divides harvest by field area
    def yield_per_ha(self):
        return self.harvest_kg / self.area


# --- child class 1: foodcrop ---

class FoodCrop(Field):
    def __init__(self, farmer, field_name, crop, area, months, irrigation,
                 seeds_kg, seeds_cost, fertilizer_cost, labor_cost,
                 harvest_kg, price_kg, family_consumption_kg):
        # call the parent constructor with all the common attributes
        # super() means "call the parent class"
        super().__init__(farmer, field_name, crop, area, months, irrigation,
                         seeds_kg, seeds_cost, fertilizer_cost, labor_cost,
                         harvest_kg, price_kg)
        # add the new attribute that only FoodCrop has
        # this is how much the family keeps for eating
        self.family_consumption_kg = family_consumption_kg

    # new method: how much is left to sell after feeding the family
    # subtract family consumption from total harvest
    def amount_to_sell(self):
        left = self.harvest_kg - self.family_consumption_kg
        if left > 0:
            return left
        return 0

    # we multiply amount_to_sell() by price instead of harvest_kg
    def revenue(self):
        return self.amount_to_sell() * self.price_kg


# --- child class 2: cashcrop ---


class CashCrop(Field):
    def __init__(self, farmer, field_name, crop, area, months, irrigation,
                 seeds_kg, seeds_cost, fertilizer_cost, labor_cost,
                 harvest_kg, price_kg, commission_percent):
        # call the parent constructor with all common attributes
        super().__init__(farmer, field_name, crop, area, months, irrigation,
                         seeds_kg, seeds_cost, fertilizer_cost, labor_cost,
                         harvest_kg, price_kg)
        # add the new attribute that only CashCrop has
        self.commission_percent = commission_percent

    # new method: revenue after paying commission
    
    def net_revenue(self):
        gross = self.harvest_kg * self.price_kg
        commission = gross * (self.commission_percent / 100)
        return gross - commission

    
    def profit(self):
        return self.net_revenue() - self.total_cost()



print("=== testing the classes ===")
print()

# example foodcrop: sorghum field
sorghum = FoodCrop(
    farmer="kaboré",
    field_name="north field",
    crop="sorghum",
    area=2.5,
    months=4,
    irrigation=False,
    seeds_kg=50,
    seeds_cost=15000,
    fertilizer_cost=25000,
    labor_cost=30000,
    harvest_kg=800,
    price_kg=200,
    family_consumption_kg=300
)

print(f"foodcrop: {sorghum.crop}")
print(f"yield: {sorghum.yield_per_ha():.2f} kg/ha")
print(f"family keeps: {sorghum.family_consumption_kg} kg")
print(f"amount to sell: {sorghum.amount_to_sell()} kg")
print(f"revenue: {sorghum.revenue()} fcfa")
print(f"profit: {sorghum.profit()} fcfa")
print()

# example cashcrop: cotton field
cotton = CashCrop(
    farmer="kaboré",
    field_name="south field",
    crop="cotton",
    area=3.0,
    months=6,
    irrigation=True,
    seeds_kg=20,
    seeds_cost=40000,
    fertilizer_cost=60000,
    labor_cost=50000,
    harvest_kg=1200,
    price_kg=300,
    commission_percent=10
)

print(f"cashcrop: {cotton.crop}")
print(f"yield: {cotton.yield_per_ha():.2f} kg/ha")
print(f"commission: {cotton.commission_percent}%")
print(f"gross revenue: {cotton.revenue()} fcfa")
print(f"net revenue: {cotton.net_revenue()} fcfa")
print(f"profit: {cotton.profit()} fcfa")
print()
print("=== end of test ===")
