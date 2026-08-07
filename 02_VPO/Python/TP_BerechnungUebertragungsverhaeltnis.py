import numpy as np

U_in  = 1.090
dU_in = 0.013

# (f_str, df_str, U_out, dU_out)
# Hinweis: "1400.0y" im Original ist ein Tippfehler → 1400.0
data = [
    ("100.00",  "0.10",  1.075, 0.025),
    ("500",     "10",    1.002, 0.025),
    ("1000.0",  "2.0",   0.890, 0.025),
    ("1200.0",  "2.0",   0.845, 0.025),
    ("1400.0",  "2.0",   0.770, 0.025),
    ("1600.0",  "2.0",   0.725, 0.025),
    ("1800.0",  "2.0",   0.680, 0.005),
    ("2000.0",  "2.0",   0.635, 0.005),
    ("2500.0",  "2.0",   0.545, 0.005),
    ("3000.0",  "2.0",   0.476, 0.005),
    ("4000.0",  "2.0",   0.379, 0.005),
    ("5000",    "10",    0.305, 0.025),
]

print("% Übertragungsverhältnis |G| = Û_out / Û_in")
print(f"% U_in = {U_in} ± {dU_in} V")
print(f"% Fehlerformel: Δ|G|/|G| = sqrt((ΔÛ_out/Û_out)² + (ΔÛ_in/Û_in)²)\n")

for f_str, df_str, U_out, dU_out in data:
    G  = U_out / U_in
    dG = G * np.sqrt((dU_out / U_out)**2 + (dU_in / U_in)**2)

    # Auf 3 Nachkommastellen runden
    G_r  = round(G,  3)
    dG_r = round(dG, 3)

    row = (
        f"        ${f_str} \\pm {df_str}$"
        f" & ${U_out:.3f} \\pm {dU_out:.3f}$"
        f" & ${G_r:.3f} \\pm {dG_r:.3f}$ \\\\"
    )
    print(row)
