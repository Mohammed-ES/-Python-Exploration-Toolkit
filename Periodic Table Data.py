# pip install chempy
# pip install PrettyTable
from chempy.util import periodic
from prettytable import PrettyTable

# Demander le nombre d'éléments à afficher
n = int(input("Enter number to see the table: "))

# Créer une table avec PrettyTable
table = PrettyTable(["Atomic No.", "Name", "Symbol", "Mass"])

# Ajouter des lignes pour chaque élément jusqu'à n
for i in range(1, n + 1):
    name = periodic.names[i]
    symbol = periodic.symbols[i]
    mass = periodic.relative_atomic_masses[i]
    table.add_row([i, name, symbol, mass])

# Afficher la table formatée
print(table)
  
#source code --> clcoding.com   