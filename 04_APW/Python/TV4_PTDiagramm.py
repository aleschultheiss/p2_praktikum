import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

temp = np.array([39.9, 50, 80, 90, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250])
temp = temp + 273.15
tempErr = np.full(len(temp), 3)

pressures = np.array([1, 1, 1.9, 2.1, 2.8, 3.0, 3.2, 3.5, 4.0, 4.5, 5.1, 5.4, 6.2, 7.1, 8.0, 9.0, 10.1, 11.1, 12.2, 13.5, 15.0, 16.2, 18.0, 19.8, 21.6, 23.7, 26.0, 28.2, 31.1, 33.3, 36.0, 39.5, 43, 47, 51])
pressures = pressures + 0.965
pressError = np.full(13, 0.5)
pressError = np.append(pressError, np.full(len(pressures) - 13, 1))

def func(T, a, b, c):
    return a + np.exp(c + b / T)

params, covariance = curve_fit(func, temp, pressures)
a, b, c = params
perr = np.sqrt(np.diag(covariance))  # Unsicherheiten der Parameter

temp_fit = np.linspace(min(temp), max(temp), 500)
press_fit = func(temp_fit, a, b, c)

fig, ax = plt.subplots(figsize=(7, 4.5))

ax.errorbar(temp, pressures, pressError, tempErr,
            fmt='o', color='steelblue', ecolor='salmon',
            ms=3, capsize=3, label='Messdaten')

ax.plot(temp_fit, press_fit, 'r-', linewidth=1.5,
        label=(f'Fit: $a + e^{{c + b/T}}$\n'
               f'$a = ({a:.3f} \\pm {perr[0]:.3f})$bar'))

ax.set_ylabel('Druck in bar')
ax.set_xlabel('Temperatur in K')
ax.set_title('Dampfdruckkurve')
ax.legend(fontsize=9)
ax.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
# plt.show()
plt.savefig("./04_APW/Images/PTDiagramm.jpg", dpi = 400)