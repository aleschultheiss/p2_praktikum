import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import quad
from math import ceil

# --- Messwerte ---
pAtm = 723.6
p0   = 438

pMessExp  = np.array([438, 417, 400, 380, 366, 350, 334, 322, 309, 296])
pExp      = pMessExp - p0 + pAtm
xExp      = np.array([72, 74, 76, 78, 80, 82, 84, 86, 88, 90])

pMessKomp = np.array([142, 149, 160, 170, 181, 192, 204, 216, 230, 244])
pKomp     = pMessKomp - p0 + pAtm
xKomp     = np.array([90, 88, 86, 84, 82, 80, 78, 76, 74, 72])

dp = 0.5

# --- Fit: p = C / x ---
def hyperbel(x, C):
    return C / x

paramsExp,  covExp  = curve_fit(hyperbel, xExp,  pExp)
paramsKomp, covKomp = curve_fit(hyperbel, xKomp, pKomp)
CExp,  = paramsExp
CKomp, = paramsKomp
dCExp  = np.sqrt(covExp[0, 0])
dCKomp = np.sqrt(covKomp[0, 0])

# --- Integration: ∫ C/x dx = C · ln(x2/x1) ---
x1, x2 = 72, 90
WExp,  _ = quad(lambda x: CExp  / x, x1, x2)
WKomp, _ = quad(lambda x: CKomp / x, x1, x2)
dWExp    = dCExp  * np.log(x2 / x1)
dWKomp   = dCKomp * np.log(x2 / x1)

print(f"Expansion:   W = ({WExp:.1f} ± {dWExp:.1f}) mmHg·mm")
print(f"Kompression: W = ({WKomp:.1f} ± {dWKomp:.1f}) mmHg·mm")

# --- Plot ---
xFit   = np.linspace(70, 92, 300)
xFill  = np.linspace(x1, x2, 300)

fig, ax = plt.subplots(figsize=(7, 4.5))

# Flächen
ax.fill_between(xFill, hyperbel(xFill, CExp),
                alpha=0.15, color='steelblue'
)
ax.fill_between(xFill, hyperbel(xFill, CExp),
                hatch='////', edgecolor='steelblue', facecolor='none', linewidth=0,
                label=rf'$W_E/A_{{Kammer}}$'
)
ax.fill_between(xFill, hyperbel(xFill, CKomp),
                alpha=0.15, color='firebrick',
                label=rf'$W_K/A_{{Kammer}}$'
)



# Fits
ax.plot(xFit, hyperbel(xFit, CExp),
        color='steelblue', linewidth=1.5, linestyle='--',
        label=rf'Fit Exp.: $C_E = ({CExp:.0f} \pm {dCExp:.0f})$')
ax.plot(xFit, hyperbel(xFit, CKomp),
        color='firebrick', linewidth=1.5, linestyle='--',
        label=rf'Fit Komp.: $C_K = ({CKomp:.0f} \pm {dCKomp:.0f})$')

# Messdaten
ax.errorbar(xExp, pExp, yerr=dp,
            fmt='o', color='steelblue', ecolor='steelblue',
            ms=3, capsize=3, linewidth=0, elinewidth=0.8, capthick=0.8,
            label='Expansion (Messdaten)')
ax.errorbar(xKomp, pKomp, yerr=dp,
            fmt='o', color='firebrick', ecolor='firebrick',
            ms=3, capsize=3, linewidth=0, elinewidth=0.8, capthick=0.8,
            label='Kompression (Messdaten)')

# Integrationsgrenzen markieren
for xv in [x1, x2]:
    ax.axvline(xv, color='gray', linewidth=0.8, linestyle=':', alpha=0.7)
ax.vlines(min(xExp), max(pKomp), max(pExp), colors='orange', label="Isochore Prozesse")
ax.vlines(max(xExp), min(pKomp), min(pExp), colors = 'orange')

ax.set_xlabel(r'Kolbenposition $x$ in mm', fontsize=12)
ax.set_ylabel(r'Druck $p$ in mmHg', fontsize=12)
ax.set_title(r'$p$-$x$-Diagramm (Stirling Prozess)', fontsize=13)
ax.text(73, 580, 
        rf"$W_{{Exp}}/A_{{kammer}} = ({round(WExp)} \pm  {ceil(dWExp)}) \mathrm{{mmHg}} \cdot \mathrm{{mm}}$", 
        fontsize = 8,
        color = 'steelblue',
        bbox=dict(
            facecolor = "white", 
            alpha = 0.5,
            edgecolor = "white"
        )
)

ax.text(73, 300, 
        rf"$W_{{Komp}}/A_{{kammer}} = ({round(WKomp)} \pm  {ceil(dWKomp)}) \mathrm{{mmHg}} \cdot \mathrm{{mm}}$", 
        fontsize = 8,
        color = 'firebrick',
        bbox=dict(
            facecolor = "white", 
            alpha = 0.5,
            edgecolor = "white"
        )
)

ax.tick_params(direction='in', top=True, right=True)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.4)
ax.set_ylim(0, 950)
ax.legend(fontsize=6.5, loc='upper right')

fig.tight_layout()
plt.savefig("./05_TEP/Images/TV13_PV-DiagrammSterling.jpg", dpi = 400)
plt.show()