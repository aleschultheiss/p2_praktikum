import numpy as np
from matplotlib import pyplot as plt
from math import ceil
# --- Daten ---
T = np.array([80, 100, 130, 160, 190, 210, 270, 300, 330, 350]) + 273.15
T0 = 25.6 + 273.15
xVals = T**4 - T0**4

U = np.array([17, 22, 38, 51, 72, 85, 157, 194, 235, 281])
dU = 0.0004 * U + 2

# --- Fit ---
line, cov = np.polyfit(xVals, U, 1, cov=True)
slope, intercept = line
dSlope, dIntercept = np.sqrt(np.diag(cov))

xFit = np.linspace(-0.05e11, 1.6e11, 300)
yFit    = slope * xFit + intercept
yFitUp  = (slope + dSlope) * xFit + (intercept + dIntercept)
yFitLow = (slope - dSlope) * xFit + (intercept - dIntercept)

print(f"Achsenabschnitt b = ({intercept:.3f} ± {dIntercept:.3f}) mV")
print(f"Steigung      a = ({slope:.3e} ± {dSlope:.3e}) mV/K⁴")

# --- Plot ---
fig, ax = plt.subplots(figsize=(7, 4.5))

# Fehlerband
ax.fill_between(xFit, yFitLow, yFitUp,
                color='grey', alpha=0.25, label='Fitungenauigkeit')

# Grenzlinien
ax.plot(xFit, yFitUp,  color='grey', linewidth=0.8, linestyle=':')
ax.plot(xFit, yFitLow, color='grey', linewidth=0.8, linestyle=':')

# Fit
ax.plot(xFit, yFit, color='firebrick', linewidth=1.5,
        label=(rf'Linearer Fit: $U = a\,(T^4 - T_0^4) + b$'
               '\n'
               rf'$b = ({round(intercept, 2)} \pm {ceil(dIntercept*10)/10})\,\mathrm{{\mu V}}$'))

# Messdaten
ax.errorbar(
    xVals, U, yerr=dU,
    fmt='o', color='steelblue', ecolor='salmon',
    ms=3, capsize=3, linewidth=0,
    elinewidth=0.8, capthick=0.8,
    label='Messdaten', zorder=5
)

ax.set_xlabel(r'$T^4 - T_0^4$ in $\mathrm{K^4}$', fontsize=12)
ax.set_ylabel(r'Spannung $U$ in $\mathrm{\mu V}$', fontsize=12)
ax.set_title(r'Spannung der Thermosäule in Abhängigkeit von $T^4 - T_0^4$', fontsize=13)

ax.tick_params(direction='in', top=True, right=True)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.4)
ax.legend(fontsize=9)

# x-Achse in 10^10 skalieren
ax.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'{x/1e10:.0f}')
)
ax.set_xlabel(r'$T^4 - T_0^4$ in $10^{10}\,\mathrm{K^4}$', fontsize=12)

fig.tight_layout()
plt.savefig("./04_APW/Images/TV5_StefanBoltzmann.jpg", dpi=400)
plt.show()