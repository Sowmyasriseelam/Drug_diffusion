import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Dictionary of materials and their diffusion coefficients (in cm^2/s)
material_dict = {
    "Polymers": {
        "PVA (hydrogel)": 1e-6,
        "PEG (crosslinked)": 5e-8,
        "PLGA (biodegradable)": 1e-9,
        "PDMS (hydrophobic)": 1e-8,
        "Chitosan (natural)": 5e-8,
        "PCL (implant)": 1e-10
    },
    "Ceramics": {
        "Hydroxyapatite (HA)": 1e-12,
        "Bioactive Glass": 1e-10,
        "Alumina (Al2O3)": 1e-13,
        "Zirconia": 1e-14
    },
    "Metals": {
        "Titanium (Ti)": 1e-16,
        "Stainless Steel (316L)": 1e-14,
        "Gold (Au)": 1e-15
    }
}

st.title("Drug Diffusion Simulator in Biomaterials")

# Material type and material selection
material_type = st.selectbox("Select Material Type", list(material_dict.keys()))
material = st.selectbox("Select Material", list(material_dict[material_type].keys()))

# Auto-filled diffusion coefficient, allow override
D_default = material_dict[material_type][material]
D = st.number_input("Diffusion Coefficient D (cm²/s)", value=D_default, format="%e")

# Other parameters
L = st.number_input("Polymer Length (cm)", value=1.0)
T = st.number_input("Total Time (s)", value=1000)
dt = st.number_input("Time Step (s)", value=10)
Nx = st.number_input("Number of Spatial Points", value=100, step=1)

# Simulation
if st.button("Run Simulation"):
    dx = L / (Nx - 1)
    Nt = int(T / dt)
    x = np.linspace(0, L, Nx)
    C = np.zeros(Nx)
    C[0] = 1.0  # Boundary condition
    profiles = []
    times = [0, T//5, T//2, T]

    for t in range(Nt):
        C_new = C.copy()
        for i in range(1, Nx - 1):
            C_new[i] = C[i] + (D * dt / dx**2) * (C[i+1] - 2*C[i] + C[i-1])
        C = C_new
        if (t + 1) * dt in times:
            profiles.append(C.copy())

    # Plot concentration profiles
    fig, ax = plt.subplots()
    for i, C_snap in enumerate(profiles):
        ax.plot(x, C_snap, label=f"t = {times[i]} s")
    ax.set_xlabel("Position (cm)")
    ax.set_ylabel("Drug Concentration")
    ax.set_title("Drug Diffusion Profile")
    ax.legend()
    st.pyplot(fig)

    # Plot cumulative release
    C = np.zeros(Nx)
    C[0] = 1.0
    release = []
    time_points = []
    for t in range(Nt):
        C_new = C.copy()
        for i in range(1, Nx - 1):
            C_new[i] = C[i] + (D * dt / dx**2) * (C[i+1] - 2*C[i] + C[i-1])
        C = C_new
        release.append(np.trapz(C, x))
        time_points.append(t * dt)

    fig2, ax2 = plt.subplots()
    ax2.plot(time_points, release)
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Cumulative Drug Released")
    ax2.set_title("Cumulative Drug Release")
    st.pyplot(fig2)

    st.success("Simulation complete!")
