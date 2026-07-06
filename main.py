from qiskit.quantum_info import DensityMatrix, partial_trace
import numpy as np
from data.link import l2a1
from src.helper import QuantumSimulation, trace

# ===================
# 1. Load the Matrix
# ===================
Delta = l2a1()

print(Delta)
print(f"The shape of matrices: {Delta.shape}")

# ====================================
# 2. Define the Parameters [mu, t, k]
# ====================================
mu = 5
t = 5
qubit_resolusi = 5

parameters = [
    mu, t, qubit_resolusi
]

# ======================
# 3. Quantum Simulation
# ======================
total_qubits, final_rho = QuantumSimulation(Delta, parameters)

# ===========================
# 4. Betti Number Estimation
# ===========================
# Partial trace
rho_total = DensityMatrix(final_rho)
rho_phase = partial_trace(rho_total, list(np.arange(qubit_resolusi, total_qubits)))

# Betti number computation
chain_dimension = trace(Delta, parameters[0])
probabilities = np.real(np.diag(rho_phase.data))
probability_zero = probabilities[0]
kernel_dimension = chain_dimension * probability_zero

print(f"""
=============== Betti Number Estimation ===============
Combination parameters      : {parameters}
Trace of Gibbs state        : {chain_dimension}
Probability of zero state   : {probability_zero}
Global Betti                : {kernel_dimension}
Error                       : {kernel_dimension - 4}
""")