import matplotlib.pyplot as plt
import numpy as np

# Daten aus der Tabelle
zeit     = [0.000, 0.200, 0.400, 0.600, 0.800, 1.000, 1.200, 1.400]
spannung = [5.55,  3.55,  2.28,  1.50,  0.95,  0.62,  0.29,  0.20]
# zeit     = [0.000, 0.200, 0.400, 0.600, 0.800, 1.000, 1.200, 1.400, 1.600]
# spannung = [0.633, 0.500,  0.388,  0.309,  0.241,  0.190,  0.150,  0.120,  0.093]
y_err = abs(0.05 / np.array(spannung))
spannung = np.log(spannung)
coeffsMid = np.polyfit(zeit, spannung, 1)
coeffsMin = np.polyfit(zeit, spannung - y_err, 1)
coeffsMax = np.polyfit(zeit, spannung + y_err, 1)

t_fit = np.linspace(0, 1.4, 300)
lnU_fit_mid = coeffsMid[1] + coeffsMid[0]*t_fit
lnU_fit_min = coeffsMin[1] + coeffsMin[0]*t_fit
lnU_fit_max = coeffsMax[1] + coeffsMax[0]*t_fit

# Plot
fig, ax = plt.subplots(figsize=(7, 4.5))

ax.plot(t_fit, lnU_fit_mid, color = "orange", linewidth = .8, label = f"Mittlere Gerade: m = {coeffsMid[0]:.3f} * 1/s")
ax.plot(t_fit, lnU_fit_max, color = "blue", linewidth = .7, label = f"Maximale Gerade: m = {coeffsMax[0]:.3f} * 1/s", linestyle = "--")
ax.plot(t_fit, lnU_fit_min, color = "grey", linewidth = .7, label = f"Minimale Gerade: m = {coeffsMin[0]:.3f}* 1/s", linestyle = "--")

ax.errorbar(zeit, spannung, xerr=0.01, yerr=y_err, fmt='o', ms = '1', mec = 'black',  
            ecolor='red', elinewidth=.1, capsize=1.5,)

ax.set_xlabel("Zeit in s")
ax.set_ylabel(r"$\ln(U)$")
ax.set_title(r"$\ln(U)$ – 1× Tastkopf")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_xlim(-0.05, 1.5)
ax.set_ylim(-5, 5)
# plt.show()

plt.tight_layout()
plt.savefig("./01_OSZ/Images/spannungsverlauf_1xTKLog.png", dpi=800)