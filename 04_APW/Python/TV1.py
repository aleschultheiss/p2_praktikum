import numpy as np
import matplotlib.pyplot as plt


# Messdaten


t_pb = np.array([
    -20, -15, -10, -5, 0, 5, 10, 15,
    30, 60, 90, 110, 150, 200, 300
], dtype=float)

T_pb = np.array([
    27.0, 27.0, 27.1, 27.0, 27.0, 29.0, 30.1, 30.0,
    30.0, 30.0, 29.9, 29.9, 30.0, 30.0, 29.9
], dtype=float)


t_al = np.array([
    -20, -15, -10, -5, 0, 5, 10, 15,
    30, 60, 90, 110, 150, 200, 300
], dtype=float)

T_al = np.array([
    27.5, 27.4, 27.5, 27.5, 27.5, 30.1, 31.4, 32.6,
    32.5, 32.5, 32.4, 32.4, 32.4, 32.3, 32.3
], dtype=float)


# Extrapolationsverfahren

def extrapolation_plot(t, T, material):
    # Vorlauf: nur Messwerte vor dem Eintauchen
    mask_vor = t <= -5

    # Nachlauf: Bereich, in dem die Temperatur wieder
    # annähernd linear verläuft
    mask_nach = t >= 30

    # Lineare Fits: T = m*t + b
    m_vor, b_vor = np.polyfit(t[mask_vor], T[mask_vor], 1)
    m_nach, b_nach = np.polyfit(t[mask_nach], T[mask_nach], 1)

    def T_vor(x):
        return m_vor * x + b_vor

    def T_nach(x):
        return m_nach * x + b_nach

    # Mischvorgang:
    # t = 0 ist das Eintauchen.
    # Nach ca. 15 s ist der starke Temperaturanstieg beendet.
    t_a = 0.0
    t_e = 15.0

    # Sehr feines Zeitraster für die Flächenberechnung
    t_dense = np.linspace(t_a, t_e, 10000)

    # Lineare Interpolation der Messkurve
    T_dense = np.interp(t_dense, t, T)

    # Suche nach t_g mit Fläche I = Fläche II

    t_g_candidates = np.linspace(t_a, t_e, 5000)

    differences = []

    for t_g in t_g_candidates:

        links = t_dense <= t_g
        rechts = t_dense >= t_g

        # Fläche I:
        # zwischen Messkurve und extrapoliertem Vorlauf
        A_I = np.trapezoid(
            T_dense[links] - T_vor(t_dense[links]),
            t_dense[links]
        )

        # Fläche II:
        # zwischen extrapoliertem Nachlauf und Messkurve
        A_II = np.trapezoid(
            T_nach(t_dense[rechts]) - T_dense[rechts],
            t_dense[rechts]
        )

        differences.append(abs(A_I - A_II))

    # t_g mit kleinstem Unterschied
    index = np.argmin(differences)
    t_g = t_g_candidates[index]

    # Temperaturen an der senkrechten Ausgleichsgeraden
    theta_k = T_vor(t_g)
    theta_m = T_nach(t_g)

    # Grafik

    fig, ax = plt.subplots(figsize=(9, 5.5))

    # Messwerte und Verbindungslinie
    ax.plot(t, T, "o", label="Messwerte")
    ax.plot(t, T, "-", alpha=0.5)

    # Extrapolierte Geraden
    t_fit = np.linspace(-25, 50, 500)

    ax.plot(
        t_fit,
        T_vor(t_fit),
        "--",
        label="extrapolierter Vorlauf"
    )

    ax.plot(
        t_fit,
        T_nach(t_fit),
        "--",
        label="extrapolierter Nachlauf"
    )

    # Senkrechte Ausgleichsgerade g
    ax.axvline(
        t_g,
        linestyle=":",
        label=rf"$g:\ t_g={t_g:.2f}\,\mathrm{{s}}$"
    )

    # Fläche I
    links = t_dense <= t_g
    ax.fill_between(
        t_dense[links],
        T_vor(t_dense[links]),
        T_dense[links],
        alpha=0.25,
        label="Fläche I"
    )

    # Fläche II
    rechts = t_dense >= t_g
    ax.fill_between(
        t_dense[rechts],
        T_dense[rechts],
        T_nach(t_dense[rechts]),
        alpha=0.25,
        label="Fläche II"
    )

    # theta_k und theta_m markieren
    ax.scatter([t_g], [theta_k], zorder=5)
    ax.scatter([t_g], [theta_m], zorder=5)

    ax.annotate(
        rf"$\Theta_k={theta_k:.2f}^\circ$C",
        (t_g, theta_k),
        xytext=(10, -18),
        textcoords="offset points"
    )

    ax.annotate(
        rf"$\Theta_m={theta_m:.2f}^\circ$C",
        (t_g, theta_m),
        xytext=(10, 8),
        textcoords="offset points"
    )

    ax.set_xlabel(r"$t\,/\,\mathrm{s}$")
    ax.set_ylabel(r"$\Theta\,/\,^\circ\mathrm{C}$")
    ax.set_title(
        f"Extrapolationsverfahren – {material}"
    )

    # Auf interessanten Bereich zoomen
    ax.set_xlim(-25, 50)

    ax.grid(alpha=0.3)
    ax.legend()

    plt.tight_layout()
    plt.show()

    # Ergebnisse ausgeben
    print(f"\n{material}")
    print("--------------------------------")
    print(f"Vorlauf:  T = {m_vor:.6f} t + {b_vor:.6f}")
    print(f"Nachlauf: T = {m_nach:.6f} t + {b_nach:.6f}")
    print(f"t_g       = {t_g:.3f} s")
    print(f"Theta_k   = {theta_k:.3f} °C")
    print(f"Theta_m   = {theta_m:.3f} °C")

    return t_g, theta_k, theta_m


# Auswertung für beide Materialien


result_pb = extrapolation_plot(
    t_pb,
    T_pb,
    "Blei"
)

result_al = extrapolation_plot(
    t_al,
    T_al,
    "Aluminium"
)