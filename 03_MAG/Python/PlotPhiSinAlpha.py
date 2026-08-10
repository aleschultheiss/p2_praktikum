import numpy as np
import matplotlib.pyplot as plt
from math import ceil

alpha = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
sinAlpha = np.sin(np.radians(alpha))
phi = -np.array([0.0, -8.0, -19.0, -24.5, -32.0, -38.0, -42.5, -46.0, -48.0, -49.5])
dphi = 2.3

line, cov = np.polyfit(sinAlpha, phi, 1, cov=True)
slope, intercept = line
d_slope, d_intercept = np.sqrt(np.diag(cov))

y_line = np.polyval(line, sinAlpha)
slope, intercept = line
label_fit = (rf"Linearer Fit $\varphi = a \cdot \sin(\alpha) + b$" "\n" rf"mit $a = {slope:.1f} \pm {ceil(d_slope*10)/10:.1f}, b = {intercept:.1f} \pm {ceil(d_intercept*10)/10:.1f}$")

fig, ax = plt.subplots(figsize=(7, 4.5))

ax.errorbar(
    sinAlpha, phi,
    yerr=dphi,
    fmt='o',
    ms=4,
    color='steelblue',
    mec='white',
    mew=0.8,
    ecolor='steelblue',
    elinewidth=1,
    capsize=4,
    capthick=1,
    label="Messwerte",
    zorder=3,
)

ax.plot(
    sinAlpha, y_line,
    color='tomato',
    linewidth=1.5,
    linestyle='--',
    label=label_fit,
    zorder=2,
)

# Achsen bei 0,0
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Achsenpfeile
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=4)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, ms=4)

ax.set_xlim(-0.05, 1.1)
ax.set_ylim(-5, 60)

# Achsenbeschriftungen etwas versetzt, damit sie nicht auf den Achsen kleben
ax.set_xlabel(r"$\sin(\alpha)$", labelpad=15)
ax.set_ylabel(r"$\varphi$ in $^{\circ}$", labelpad=15, rotation=0, ha='right')

ax.set_title(r"$\varphi$ in Abhängigkeit von $\sin(\alpha)$", pad=12, fontsize=12)

ax.grid(True, linestyle=':', alpha=0.4, color='gray')

ax.legend(
    loc='upper left',
    framealpha=0.9,
    edgecolor='lightgray',
    fontsize=9,
)

plt.tight_layout()
plt.savefig("./03_MAG/Images/PhiSinAlpha.png", dpi=800)
plt.show()