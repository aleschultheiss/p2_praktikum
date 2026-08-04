import matplotlib.pyplot as plt
import numpy as np

# Daten aus der Tabelle
# zeit     = [0.000, 0.200, 0.400, 0.600, 0.800, 1.000, 1.200, 1.400]
# spannung = [5.55,  3.55,  2.28,  1.50,  0.95,  0.62,  0.29,  0.20]
zeit     = [0.000, 0.200, 0.400, 0.600, 0.800, 1.000, 1.200, 1.400, 1.600]
spannung = [0.633, 0.500,  0.388,  0.309,  0.241,  0.190,  0.150,  0.120,  0.093]


# Plot
fig, ax = plt.subplots(figsize=(7, 4.5))

ax.errorbar(zeit, spannung, xerr=0.01, yerr=0.005, fmt='o', ms = '1', mec = 'black',  
            ecolor='red', elinewidth=.1, capsize=1.5,)

ax.set_xlabel("Zeit in s")
ax.set_ylabel("Spannung in V")
ax.set_title("Spannungsverlauf – 10× Tastkopf")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_xlim(-0.05, 1.5)
ax.set_ylim(0, 0.8)
# plt.show()

plt.tight_layout()
plt.savefig("./01_OSZ/Images/spannungsverlauf_10xTKRaw.png", dpi=800)