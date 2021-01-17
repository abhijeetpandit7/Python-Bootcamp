# Import class from module
from prettytable import PrettyTable
# Create object from class
table = PrettyTable() 
# Assign object attributes
table.field_names = ["Pokemon Name","Type"]
# Change object attributes
table.align = 'l'
# Access object method
table.add_rows(
    [
        ['Pikachu','Electric'],
        ['Squirtle','Water'],
        ['Charmander','Fire']
    ]
)
print(table)