**1) INTRODUCTION**

Controlled drug delivery systems are a significant advancement in pharmaceutical and biomedical engineering. Among these, polymer-based systems offer a promising means to regulate drug release, allowing for sustained therapeutic effects and reduced side effects. Understanding and predicting the behavior of drug diffusion within these polymers is crucial for designing efficient systems. This project aims to simulate one-dimensional drug diffusion in a polymeric biomaterial using a finite difference approach, enabling visualization of drug release profiles and cumulative uptake.

**2) LITERATURE SURVEY**

Research on drug delivery has evolved from simple diffusion models to more sophisticated bioresponsive systems. Higuchi's early models on drug release from matrices laid the groundwork for subsequent mathematical approaches. Crank's diffusion theory further provided robust analytical and numerical tools to simulate various scenarios. Recent developments incorporate computational simulations using MATLAB, Python, and AI-based techniques to predict and optimize drug delivery. Literature also highlights the significance of polymer properties, such as crosslinking density, porosity, and molecular interactions, which can influence diffusion behavior.

**3) METHODOLOGY / WORKFLOW**

- Define simulation parameters: polymer length, diffusion coefficient, spatial and temporal resolution, and initial concentration.
- Discretize the 1D domain using a finite difference method.
- Apply the explicit method for solving the diffusion equation.
- Visualize concentration profiles at different time points.
- Calculate and plot cumulative drug uptake over time.
- Integrate the simulation into a user-interactive Streamlit web application.

**4) WORK**

**4.1 Experimenting**
We began by setting up a baseline scenario for drug diffusion with commonly reported values of the diffusion coefficient and polymer length. Initial concentration was placed at one end of the polymer, and zero concentration was assumed throughout the rest of the material. Different values for diffusion coefficients and time durations were tested to observe their impact on diffusion dynamics.

**4.2 Modelling**
The drug diffusion was modeled using the 1D Fick's Second Law of Diffusion. The spatial domain was divided into discrete intervals, and the time evolution was calculated using the explicit finite difference scheme. This method updates the concentration at each point based on its neighbors, simulating how the drug spreads over time.

**4.3 Simulation**
The simulation was implemented in Python. The user inputs parameters via a Streamlit interface. The model runs iteratively, updating the concentration profile at regular time steps. Matplotlib was used for plotting the concentration at different times and for showing the cumulative drug release. While AI/ML wasn't used directly, the setup is designed to be easily extendable for future predictive modeling.

**5) RESULTS AND DISCUSSION**

The simulation successfully demonstrated drug diffusion dynamics over time. As expected, higher diffusion coefficients resulted in faster spread, and longer simulation durations captured the complete release profile. The plotted concentration profiles clearly showed how drug concentration dissipates from the source over time. The cumulative uptake graph increased monotonically, indicating consistent absorption by the polymer. The results align with theoretical expectations and previously published models.

An interesting observation was that at lower diffusion coefficients, the concentration gradient remained steep near the source, while higher values flattened the curve more evenly across the polymer. These outcomes underscore the sensitivity of the system to parameter variations, which is crucial in drug delivery design.

**6) CONCLUSION**

This project successfully developed a numerical simulation of drug diffusion in polymeric biomaterials and provided a user-friendly interface for parameter tuning and visualization. The tool can serve both educational and preliminary design purposes. Future work can involve incorporating AI/ML techniques for prediction based on material properties and integrating real experimental data to validate and calibrate the model.



cd your_project
source venv/bin/activate         # or venv\Scripts\activate on Windows
streamlit run app.py
