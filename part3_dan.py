# agritrack bf - part 3
# magic methods (dunder methods): __str__, __eq__, __lt__
# done by KAFANDO Dan
#
# i researched "python dunder methods" and found that these are special
# methods python calls automatically in certain situations.
# __str__ is called when you do print(object)
# __eq__ is called when you do object1 == object2
# __lt__ is called when you do object1 < object2

from part2_ulrich import Field, FoodCrop, CashCrop


# i add the magic methods to Field by reopening the class
# this way the children FoodCrop and CashCrop get them too

class Field(Field):

    def __str__(self):
        # python calls this automatically when you print(field)
        # instead of printing something like <Field object at 0x...>
        # it now prints a readable summary
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

    def __eq__(self, other):
        # called when you write field1 == field2
        # two fields are equal if they made the same profit
        return self.profit() == other.profit()

    def __lt__(self, other):
        # called when you write field1 < field2
        # allows sorting a list of fields by profit
        return self.profit() < other.profit()


class FoodCrop(FoodCrop, Field):
    # FoodCrop now also gets __str__ from Field
    # i override __str__ to add the food crop specific lines

    def __str__(self):
        base = super().__str__()
        return (
            base + f"\n"
            f"[food crop]\n"
            f"family keeps:   {self.family_consumption_kg:.2f} kg\n"
            f"amount to sell: {self.amount_to_sell():.2f} kg"
        )


class CashCrop(CashCrop, Field):
    # CashCrop now also gets __str__ from Field
    # i override __str__ to add the cash crop specific lines

    def __str__(self):
        base = super().__str__()
        return (
            base + f"\n"
            f"[cash crop]\n"
            f"commission:  {self.commission_percent}%\n"
            f"net revenue: {self.net_revenue():.2f} fcfa"
        )


# quick test
if __name__ == "__main__":
    sorghum = FoodCrop("kaboré", "north field", "sorghum", 2.5, 4, False,
                       50, 15000, 25000, 30000, 800, 200, 300)
    print(sorghum)  # triggers __str__
    print()
    cotton = CashCrop("kaboré", "south field", "cotton", 3.0, 6, True,
                      20, 40000, 60000, 50000, 1200, 300, 10)
    print(cotton)
