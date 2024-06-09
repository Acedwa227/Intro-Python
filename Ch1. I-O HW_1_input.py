'''Assume each pizza has 8 slices. Assuming that there is a family
of 4. Ask how many slices everyone in the family eats. Then calculate
how many whole pizza are required for a family of 4 for one meal? How
many are the leftover slices? So if everyone is eating 3 slices you need
2 pizzas with 4 leftover slices. Do not use loops or lists or functions.
In this case write two programs one with everyone eating the same number
of slices (only 1 input statement) and another with everone eating
different number of slices (two input statements)'''

# constants
PIZZA = 8 
FAM = 4 

# Inputs - Get the number of slices each person eats.
NUM_SLICES = int(input("Enter the number of slices each person eats: "))

# Calculate number of slices the family requires
NEEDED_SLICES = NUM_SLICES * FAM 

# Calculate number of whole pizzas the required slices are
TOTAL_PIZZAS = NEEDED_SLICES // PIZZA
if NEEDED_SLICES % PIZZA !=0:
    TOTAL_PIZZAS += 1

# Calculate number of lefover slices of pizza
LEFTOVERS =(TOTAL_PIZZAS * PIZZA) - NEEDED_SLICES

# Print Results
print(f"For a family of 4, eating {NUM_SLICES} slices each:")
print(f"You will need: {TOTAL_PIZZAS} pizzas")
print(f"You will have: {LEFTOVERS} slices leftover")
