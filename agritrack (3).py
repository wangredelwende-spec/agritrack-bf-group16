# agritrack bf - final version
# combines all parts into one working program
# parts 1+2+3+4 all together
# PRG1406 Group 16 | Burkina Institute of Technology
# WANGRE Esther, NOMBRE Carelle, KAFANDO Dan, ZONGO Pascal, SOULAMA Ulrich

# ── CLASSES ───────────────────────────────────────────────────────────────────

class Field:
    # parent class - all fields share these attributes and methods

    def __init__(self, farmer, field_name, crop, area, months, irrigation,
                 seeds_kg, seeds_cost, fertilizer_cost, labor_cost,
                 harvest_kg, price_kg):
        self.farmer = farmer          # str
        self.field_name = field_name  # str
        self.crop = crop              # str
        self.area = area              # float
        self.months = months          # int
        self.irrigation = irrigation  # bool
        self.seeds_kg = seeds_kg      # float
        self.seeds_cost = seeds_cost  # float
        self.fertilizer_cost = fertilizer_cost  # float
        self.labor_cost = labor_cost  # float
        self.harvest_kg = harvest_kg  # float
        self.price_kg = price_kg      # float

    # part 4 - @staticmethod
    # staticmethod means the method belongs to the class but doesnt need self
    # we use it for validators because they dont need any field data

    @staticmethod
    def ask_number(message):
        # loops until user enters a valid non-negative number
        while True:
            try:
                val = float(input(message))
                if val < 0:
                    print("no negative values. try again.")
                    continue
                return val
            except:
                print("that's not a number. try again.")

    @staticmethod
    def ask_bool(message):
        # returns a real python bool, not a string
        while True:
            ans = input(message).lower().strip()
            if ans == "yes":
                return True
            elif ans == "no":
                return False
            print("answer yes or no only.")

    @staticmethod
    def collect_base_inputs():
        # collects the 12 inputs common to all field types
        farmer = input("farmer name: ")
        field_name = input("field name: ")
        crop = input("crop type (sorghum, millet, cotton, cowpea): ")
        area = Field.ask_number("field area in hectares: ")
        seeds_kg = Field.ask_number("seeds used in kg: ")
        seeds_cost = Field.ask_number("cost of seeds in fcfa: ")
        fertilizer_cost = Field.ask_number("cost of fertilizer in fcfa: ")
        labor_cost = Field.ask_number("cost of labor in fcfa: ")
        harvest_kg = Field.ask_number("total harvest in kg: ")
        price_kg = Field.ask_number("sale price per kg in fcfa: ")
        months = int(Field.ask_number("growing duration in months: "))
        irrigation = Field.ask_bool("did you use irrigation? (yes/no): ")
        return dict(farmer=farmer, field_name=field_name, crop=crop,
                    area=area, months=months, irrigation=irrigation,
                    seeds_kg=seeds_kg, seeds_cost=seeds_cost,
                    fertilizer_cost=fertilizer_cost, labor_cost=labor_cost,
                    harvest_kg=harvest_kg, price_kg=price_kg)

    # calculations
    def total_cost(self):
        return self.seeds_cost + self.fertilizer_cost + self.labor_cost

    def revenue(self):
        return self.harvest_kg * self.price_kg

    def profit(self):
        return self.revenue() - self.total_cost()

    def yield_per_ha(self):
        return self.harvest_kg / self.area

    def margin_percent(self):
        cost = self.total_cost()
        if cost > 0:
            return (self.profit() / cost) * 100
        return 0.0

    # part 3 - magic methods
    # __str__ is called automatically when you do print(field)
    def __str__(self):
        result = self.profit()
        if result > 0:
            status = "profit"
        elif result < 0:
            status = "loss"
        else:
            status = "break even"
        return (
            f"{'=' * 43}\n"
            f"  season summary\n"
            f"{'=' * 43}\n"
            f"farmer:     {self.farmer}\n"
            f"field:      {self.field_name}\n"
            f"crop:       {self.crop}\n"
            f"area:       {self.area} ha\n"
            f"duration:   {self.months} months\n"
            f"irrigation: {'yes' if self.irrigation else 'no'}\n"
            f"\n"
            f"total cost: {self.total_cost():.2f} fcfa\n"
            f"harvest:    {self.harvest_kg:.2f} kg\n"
            f"yield:      {self.yield_per_ha():.2f} kg/ha\n"
            f"revenue:    {self.revenue():.2f} fcfa\n"
            f"profit:     {result:.2f} fcfa\n"
            f"margin:     {self.margin_percent():.2f}%\n"
            f"result:     {status}\n"
            f"{'=' * 43}"
        )

    # __eq__ is called when you write field1 == field2
    def __eq__(self, other):
        return self.profit() == other.profit()

    # __lt__ is called when you write field1 < field2, allows sorting
    def __lt__(self, other):
        return self.profit() < other.profit()


class FoodCrop(Field):
    # child class for food crops (sorghum, millet, cowpea)
    # the child IS a type of Field - relationship makes sense

    def __init__(self, family_consumption_kg, **kwargs):
        super().__init__(**kwargs)
        # new attribute that only FoodCrop has
        self.family_consumption_kg = family_consumption_kg

    # part 4 - @classmethod
    # classmethod receives the class as first argument (cls)
    # we use it as a factory method: it collects inputs and returns a ready object
    @classmethod
    def from_input(cls):
        data = Field.collect_base_inputs()
        family_kg = cls.ask_number("kg kept by family for consumption: ")
        return cls(**data, family_consumption_kg=family_kg)

    def amount_to_sell(self):
        # new method: kg available to sell after family consumption
        left = self.harvest_kg - self.family_consumption_kg
        if left > 0:
            return left
        return 0

    def revenue(self):
        # override: revenue only on the sellable portion
        return self.amount_to_sell() * self.price_kg

    def __str__(self):
        # extend parent summary with food crop specific info
        base = super().__str__()
        return (
            base + "\n"
            f"[food crop]\n"
            f"family keeps:   {self.family_consumption_kg:.2f} kg\n"
            f"amount to sell: {self.amount_to_sell():.2f} kg"
        )


class CashCrop(Field):
    # child class for cash crops (cotton, sesame)
    # the child IS a type of Field - relationship makes sense

    def __init__(self, commission_percent, **kwargs):
        super().__init__(**kwargs)
        # new attribute that only CashCrop has
        self.commission_percent = commission_percent

    # part 4 - @classmethod factory method
    @classmethod
    def from_input(cls):
        data = Field.collect_base_inputs()
        commission = cls.ask_number("broker commission percentage: ")
        return cls(**data, commission_percent=commission)

    def net_revenue(self):
        # new method: revenue after deducting broker commission
        gross = self.harvest_kg * self.price_kg
        commission = gross * (self.commission_percent / 100)
        return gross - commission

    def profit(self):
        # override: profit uses net revenue not gross
        return self.net_revenue() - self.total_cost()

    def __str__(self):
        # extend parent summary with cash crop specific info
        base = super().__str__()
        return (
            base + "\n"
            f"[cash crop]\n"
            f"commission:  {self.commission_percent}%\n"
            f"net revenue: {self.net_revenue():.2f} fcfa"
        )


# ── MAIN ──────────────────────────────────────────────────────────────────────

print("=== agritrack bf ===")
print()

while True:
    category = input("crop category (food / cash): ").lower().strip()
    if category in ("food", "cash"):
        break
    print("enter 'food' or 'cash' only.")

print()

if category == "food":
    field = FoodCrop.from_input()
else:
    field = CashCrop.from_input()

print()
print(field)
print()
print("thank you for using agritrack bf")
