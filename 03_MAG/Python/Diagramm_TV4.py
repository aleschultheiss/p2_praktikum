import numpy as np
import matplotlib.pyplot as plt

#Folgende Arrays sind unsere Messwerte

# Feldstromsteigungen in mA/s
dIdt = np.array([
    16.625,
    40.000,
    66.500,
    93.300,
    111.1667
])

# Unsicherheiten der Feldstromsteigungen in mA/s
dIdt_err = np.array([
    1.7,
    1.5,
    8.0,
    2.1,
    4.0
])

# Induktionsspannungen in mV
U_ind = np.array([
    10.0,
    25.0,
    40.0,
    58.0,
    71.0
])

# Ableseunsicherheit der Induktionsspannung in mV
U_err = np.ones(len(U_ind)) * 1.0


# Lineare Regression

m_exp, b_exp = np.polyfit(dIdt, U_ind, 1)

# Vorhergesagte Werte zur Berechnung von R^2
U_fit = m_exp * dIdt + b_exp

ss_res = np.sum((U_ind - U_fit)**2)
ss_tot = np.sum((U_ind - np.mean(U_ind))**2)

R2 = 1 - ss_res / ss_tot




# K_theo = 0.6622 Vs/A
#
# Da auf der x-Achse mA/s und auf der y-Achse mV
# verwendet werden, besitzt die theoretische Gerade
# numerisch dieselbe Steigung
K_theo = 0.6622




x = np.linspace(0, 120, 500)

y_exp = m_exp * x + b_exp
y_theo = K_theo * x




plt.figure(figsize=(8, 5.5))

# Messwerte mit horizontalen und vertikalen Fehlerbalken
plt.errorbar(
    dIdt,
    U_ind,
    xerr=dIdt_err,
    yerr=U_err,
    fmt='o',
    capsize=4,
    label='Messwerte'
)

# Ausgleichsgerade experimentell
plt.plot(
    x,
    y_exp,
    label=(
        rf'Lineare Regression: '
        rf'$U = {m_exp:.3f}\,\frac{{\mathrm{{Vs}}}}{{\mathrm{{A}}}}'
        rf'\,\frac{{\mathrm{{d}}I}}{{\mathrm{{d}}t}}'
        rf'{b_exp:+.2f}\,\mathrm{{mV}}$'
        '\n'
        rf'$R^2={R2:.4f}$'
    )
)

# Die Theoriegerade
plt.plot(
    x,
    y_theo,
    '--',
    label=(
        rf'Theorie: '
        rf'$K_\mathrm{{theo}}={K_theo:.4f}\,\mathrm{{Vs/A}}$'
    )
)

plt.xlabel(
    r'Betrag der Feldstromsteigung '
    r'$|\mathrm{d}I/\mathrm{d}t|$ in $\mathrm{mA/s}$'
)

plt.ylabel(
    r'Betrag der Induktionsspannung '
    r'$|U_{\mathrm{ind}}|$ in $\mathrm{mV}$'
)

plt.xlim(0, 120)
plt.ylim(0, 80)

plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()



plt.show()


# Folgender Abschnitt gibt den plot aus

print(f"Experimentelle Steigung: K_exp = {m_exp:.4f} Vs/A")
print(f"Achsenabschnitt:          b     = {b_exp:.2f} mV")
print(f"Bestimmtheitsmaß:         R²    = {R2:.4f}")
print(f"Theoretische Steigung:    K_theo = {K_theo:.4f} Vs/A")

abweichung = abs(m_exp - K_theo) / K_theo * 100

print(f"Relative Abweichung:      {abweichung:.1f} %")