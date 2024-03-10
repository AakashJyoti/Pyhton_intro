file = open("Astro.txt", "w")

try:
    file.write("Astroworld")
finally:
    file.close()

with open("Astra.txt", "w") as file:
    file.write("Astraworld")
