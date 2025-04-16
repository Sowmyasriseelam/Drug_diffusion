import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_agg import RendererAgg
import threading

_lock = threading.Lock()

# --- Sidebar Inputs ---
st.sidebar.title("Simulation Parameters")

L = st.sidebar.number_input("Polymer length (cm)", min_value=0.1, max_value=10.0, value=1.0)
D = st.sidebar.number_input("Diffusion coefficient (cm²/s)", min_value=1e-10, max_value=1e-4, format="%.1e", value=1e-6)
Nx = st.sidebar.slider("Number of spatial points", 50, 500, 200)
T = st.sidebar.number_input("Total simulation time (s)", min_value=10, max_value=10000, value=1000)
dt = st.sidebar.number_input("Time step (s)", min_value=0.01, max_value=10.0, value=0.1)
initial_conc = st.sidebar.number_input("Initial concentration at source", min_value=0.0, value=1.0)

# --- Simulation Grid Setup ---
dx = L / Nx
Nt = int(T / dt)
x = np.linspace(0, L, Nx)
C = np.zeros(Nx)
C[0] = initial_conc

C_over_time = []
time_points = []

# --- Diffusion Simulation (Explicit Finite Difference) ---
for t in range(Nt):
    C_new = C.copy()
    for i in range(1, Nx - 1):
        C_new[i] = C[i] + D * dt / dx**2 * (C[i+1] - 2*C[i] + C[i-1])
    C = C_new
    if t % int(100/dt) == 0:
        C_over_time.append(C.copy())
        time_points.append(t * dt)

# --- Plot Concentration Profiles ---
st.subheader("Drug Concentration Profiles")
with _lock:
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    colors = plt.cm.viridis(np.linspace(0, 1, len(C_over_time)))
    for i, (C_plot, time) in enumerate(zip(C_over_time, time_points)):
        label = f"{int(time)}s"
        ax1.plot(x, C_plot, label=label, color=colors[i])
    ax1.set_xlabel("Position (cm)")
    ax1.set_ylabel("Concentration")
    ax1.set_title("Concentration vs Position over Time")
    ax1.legend(fontsize='small', loc='center left', bbox_to_anchor=(1, 0.5))
    ax1.grid(True)
    st.pyplot(fig1)

# --- Plot Cumulative Drug Uptake ---
release_profile = [np.trapz(C_t, x) for C_t in C_over_time]

st.subheader("Cumulative Drug Uptake")
with _lock:
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    ax2.plot(time_points, release_profile, color='green')
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Total Drug in Polymer")
    ax2.set_title("Cumulative Drug Release")
    ax2.grid(True)
    st.pyplot(fig2)


