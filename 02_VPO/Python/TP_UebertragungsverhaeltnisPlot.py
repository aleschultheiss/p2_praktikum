import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit, root_scalar 

G_grenz = 1/np.sqrt(2)
frequenz     = [100, 500, 1000, 1200, 1400, 1600, 1800, 2000, 2500, 3000, 4000, 5000]
g_mid = [0.986, 0.919,  0.817,  0.775,  0.706,  0.665,  0.624,  0.583,  0.500, 0.437, 0.348, 0.280]
freq_err = [0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.005, 0.005, 0.005, 0.005, 0.005, 0.025]
g_err = [0.026, 0.025, 0.025, 0.025, 0.024, 0.024, 0.009, 0.008, 0.008, 0.007, 0.006, 0.023]
g_max = np.array(g_mid) + np.array(g_err)
g_min = np.array(g_mid) - np.array(g_err)
g_values = [(g_mid, "Mittlere Approximation", "purple"), (g_max, "Maximale Approximation", "magenta"), (g_min, "Minimale Approximation", "blue")]
def f(x, a, b):
    return b/np.sqrt(a * x**2 + 1)

fig, ax = plt.subplots(figsize=(7, 4.5))
freq_fit = np.linspace(0, 5000, 300)

for g, label, color in g_values:
    popt, pcov = curve_fit(f, frequenz, g, p0=[1.0, 1.0])
    a, b = popt[0], popt[1]
    ax.plot(freq_fit, f(freq_fit, a, b), color = color, linewidth = 1, label = label)
    res = root_scalar(lambda x: f(x, a, b) - G_grenz, bracket=[0, 5000])
    plt.vlines(res.root, 0, G_grenz, linewidth = .8, linestyles="--", color = color)
    plt.text(res.root, -0.02, f'{res.root:.1f} Hz',
         ha='center', va='top', rotation=90, color = color, fontsize = 6)

plt.hlines(G_grenz, 0, 5000, color = "grey", linewidth = .8, label=r"$|B| = 1/\sqrt{2}$")
plt.text(-350, G_grenz-.02, r"$1/\sqrt{2}$")

ax.errorbar(frequenz, g_mid, xerr=freq_err, yerr=g_err, fmt='o', ms = '1', mec = 'black',  
            ecolor='red', elinewidth=.1, capsize=1.5, label="Messpunkte mit Fehler")

ax.set_xlabel("Frequenz in Hz")
ax.set_ylabel("|G|")
ax.set_title(r"|G|($\omega$)")
ax.legend(fontsize = 8)
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_xlim(0, 5000)
ax.set_ylim(0, 1)
# plt.show()

plt.tight_layout()
plt.savefig("./02_VPO/Images/UebertragungsverhaeltnisTP.png", dpi=800)