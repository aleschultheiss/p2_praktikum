import numpy as np
import matplotlib.pyplot as plt
from math import ceil

# --- Temperatur ---
temp_C = np.array([80, 90, 100, 105, 110, 115, 120, 125, 130, 135,
                   140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195,
                   200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250])
temp = temp_C + 273.15
tempErr = np.full(len(temp), 3)

xVals  = -1 / temp
xError = tempErr / temp**2

# --- Druck ---
pressures_raw = np.array([1.9, 2.1, 2.8, 3.0, 3.2, 3.5, 4.0, 4.5, 5.1, 5.4,
                           6.2, 7.1, 8.0, 9.0, 10.1, 11.1, 12.2, 13.5, 15.0, 16.2,
                           18.0, 19.8, 21.6, 23.7, 26.0, 28.2, 31.1, 33.3, 36.0,
                           39.5, 43, 47, 51])
pressures = pressures_raw + 0.965 - 1.798

pressError = np.concatenate([np.full(13, 0.5), np.full(len(pressures) - 13, 1.0)])
lnPressures = np.log(pressures)
lnPressError = pressError / pressures

# --- Fit ---
line, cov = np.polyfit(xVals, lnPressures, 1, cov=True)
slope, intercept = line
dSlope, dIntercept = np.sqrt(np.diag(cov))
yline = np.polyval(line, xVals)
labelFit = (rf"Linearer Fit: $ln(p/bar) = a \cdot (-1/T) + b$" "\n" rf"$a = ({round(slope)} \pm {ceil(dSlope)})K$")

# --- Plot ---
fig, ax = plt.subplots(figsize=(7, 4.5))

ax.errorbar(
    xVals, lnPressures,
    yerr=lnPressError, xerr=xError,
    fmt='o', color='steelblue', ecolor='salmon',
    ms=3, capsize=3, label='Messdaten'
)

ax.plot(
    xVals, yline,
    color = 'grey',
    linewidth=1.5,
    label=labelFit,
)

ax.set_xlabel(r"$-1/T$ in $\mathrm{K^{-1}}$")
ax.set_ylabel(r"$\ln(p\,/\,\mathrm{bar})$")
ax.set_title(r"$-1/T$ - $ln(p)$-Diagramm")
ax.legend(fontsize=9)
ax.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.savefig("./04_APW/Images/TV4_lnPTDiagrammValsRemoved.jpg", dpi=400)
plt.show()