import numpy as np

U_in  = 0.690
dU_in = 0.013

# (f_str, df_str, U_out, dU_out)
data = [
    ("100.00",  "0.10",  0.070, 0.005),
    ("500",     "10",    0.318, 0.005),
    ("1000.0",  "2.0",   0.378, 0.005),
    ("1200.0",  "2.0",   0.420, 0.005),
    ("1400.0",  "2.0",   0.462, 0.005),
    ("1600.0",  "2.0",   0.495, 0.005),
    ("1800.0",  "2.0",   0.525, 0.005),
    ("2000.0",  "2.0",   0.550, 0.013),
    ("2500.0",  "2.0",   0.590, 0.013),
    ("3000.0",  "2.0",   0.610, 0.013),
    ("4000.0",  "2.0",   0.640, 0.013),
    ("5000",    "2.0",   0.655, 0.013),
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
