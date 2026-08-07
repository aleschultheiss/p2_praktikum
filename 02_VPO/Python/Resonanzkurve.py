import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f     = np.array([3.000, 4.000, 4.420, 4.450, 4.520, 5.000, 6.000])  # kHz
df    = np.array([0.02,  0.02,  0.02,  0.02,  0.02,  0.02,  0.02 ])

I     = np.array([0.494, 1.629, 3.059, 3.059, 2.941, 1.529, 0.662])   # mA
dI    = np.array([0.076, 0.082, 0.072, 0.072, 0.071, 0.079, 0.117])

def resonance(f, I_max, f0, Q):
    return I_max / np.sqrt(1 + Q**2 * (f/f0 - f0/f)**2)

p0 = [3.0, 4.43, 5.0]

popt,  pcov  = curve_fit(resonance, f, I,      p0=p0, sigma=dI, absolute_sigma=True)
# Fit durch I + dI
popt_up, _   = curve_fit(resonance, f, I + dI, p0=p0, sigma=dI, absolute_sigma=True)
# Fit durch I - dI
popt_dn, _   = curve_fit(resonance, f, I - dI, p0=p0, sigma=dI, absolute_sigma=True)

perr = np.sqrt(np.diag(pcov))
I_max_fit, f0_fit, Q_fit = popt
dI_max, df0, dQ          = perr

f_fine = np.linspace(0, 7.0, 1000)

fig, ax = plt.subplots(figsize=(8, 5))
ax.errorbar(f, I, xerr=df, yerr=dI,
            fmt='.', color='black', capsize=4,
            label='Messwerte', zorder=3)

ax.plot(f_fine, resonance(f_fine, *popt_up), color='magenta', lw=1,
        ls='--', alpha=0.6, label='Fit durch $I + \\Delta I$', zorder = 5)
ax.plot(f_fine, resonance(f_fine, *popt_dn), color='blue', lw=1,
        ls='--',  alpha=0.6, label='Fit durch $I - \\Delta I$', zorder = 5)

ax.plot(f_fine, resonance(f_fine, *popt), color='purple', lw=1,
        label=(f'Fit durch I'), zorder = 5)

# Messwerte
ax.axvline(f0_fit, color='grey', lw=1, ls='--', alpha=0.4)
plt.text(f0_fit, -0.25, f"{f0_fit:.3f}", ha='center', va='top', color = "black", fontsize = 10)

ax.set_xlabel('Frequenz $f$ (kHz)', fontsize=12)
ax.set_ylabel('Stromamplitude $I$ (mA)', fontsize=12)
ax.set_title('Resonanzkurve – Stromamplitude vs. Frequenz', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# plt.tight_layout()
plt.savefig('./02_VPO/Images/Resonanzkurve.jpg', dpi=800)