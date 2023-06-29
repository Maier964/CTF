import math

# The input repeats itself 5 times -> Create reduced input
reduced_input = "b71bO12cO156O6e43Od8O69c3O5cd3O144Oe4O6e43O37cbOf6O69c3O1e7bO156O3183O69c3O6cO8b3bOc0O1e7bO156OfcO50bbO69c3Oc0O102O6e43OdeOb14bOc6OfcOd8O"

# Split the input string by the delimiter "O" to create an array with each element
hex_array = [int(hex_num, 16) for hex_num in reduced_input.split("O") if hex_num]

# Dilute
diluted = [el * 2 // 3 for el in hex_array]

# Waterlog
waterlogged = [el // 2 if (el // 2 + 2) * 4 % 87 == 17361 else el * 2 for el in diluted]

# Drench
drenched = [el >> 1 for el in diluted]

# Moisten
moistened = [el if el % 2 == 0 else int(math.sqrt(el)) for el in drenched]

# Reverse the moistened list to obtain the hydrated list
hydrated = moistened[::-1]

# Convert the hydrated numbers to characters and print
decoded_str = "".join(chr(el) for el in hydrated)
print(decoded_str)
