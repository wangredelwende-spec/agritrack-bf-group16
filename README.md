# AgriTrack BF

**PRG1406 Group 16 | Burkina Institute of Technology**

Members: WANGRE Esther, NOMBRE Carelle, KAFANDO Dan, ZONGO Pascal, SOULAMA Ulrich

## What the program does

AgriTrack BF is a command-line tool for farmers in Burkina Faso to manage their fields. You enter data about your field and the program calculates your yield, revenue, profit or loss, and profit margin.

Two crop types are supported:
 **food crop** (sorghum, millet, cowpea) — tracks how much the family keeps before selling
- **cash crop** (cotton, sesame) — deducts a broker commission from the revenue

## How to run

```bash
python agritrack.py
```

No libraries needed. Python 3.8 or higher.

## Files

| File | Content |
|------|---------|
| `part1_carelle.py` | Part 1 — inputs, validation, arithmetic, summary (standalone) |
| `part2_ulrich.py` | Part 2 — Field, FoodCrop, CashCrop classes with inheritance |
| `part3_dan.py` | Part 3 — magic methods added (__str__, __eq__, __lt__) |
| `agritrack.py` | Final version — all parts combined into one working program |

## Class structure

```
Field (parent)
├── FoodCrop (child) — adds family_consumption_kg
└── CashCrop (child) — adds commission_percent
```

**Field** holds all shared attributes and methods. Input validators are `@staticmethod` inside the class.

**FoodCrop** inherits from Field with `super().__init__()`. Overrides `revenue()` to only count the sellable portion after family consumption.

**CashCrop** inherits from Field with `super().__init__()`. Overrides `profit()` to use net revenue after broker commission.

## Concepts implemented

**Part 1** — str, int, float, bool all used. 12 input() calls with try/except validation. 5 arithmetic expressions. f-strings throughout. Summary screen at the end.

**Part 2** — FoodCrop and CashCrop both inherit from Field using `super().__init__()`. Each child adds a new attribute and at least one new method the parent does not have.

**Part 3** — `__str__` controls what print(field) displays. `__eq__` compares two fields by profit. `__lt__` allows sorting fields by profit.

**Part 4** — `@staticmethod` used for ask_number, ask_bool, and collect_base_inputs because they don't need a field instance. `@classmethod` used for from_input() on each child class so it can collect inputs and return a ready object.

## Design decisions

- Validators are inside the class as `@staticmethod` instead of standalone functions — cleaner OOP structure.
- `bool` is set correctly: `ask_bool()` returns `True` or `False`, not a string.
- Each child's `__str__` calls `super().__str__()` and adds its own specific lines at the end.
