from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
"""
+--------------+----------+
| Pokemon Name |   Type   |
+--------------+----------+
|   Pikachu    | Electric |
|   Squirtle   |  Water   |
|  Charmander  |   Fire   |
+--------------+----------+
"""

#aligned to center by default
table.align = "l"
"""
+--------------+----------+
| Pokemon Name | Type     |
+--------------+----------+
| Pikachu      | Electric |
| Squirtle     | Water    |
| Charmander   | Fire     |
+--------------+----------+
"""


#sortby
table.sortby = "Pokemon Name"
"""
+--------------+----------+
| Pokemon Name | Type     |
+--------------+----------+
| Charmander   | Fire     |
| Pikachu      | Electric |
| Squirtle     | Water    |
+--------------+----------+
"""

print(table)
