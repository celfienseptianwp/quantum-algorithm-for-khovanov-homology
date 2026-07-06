import numpy as np
from scipy.linalg import expm
from qiskit.circuit.library import UnitaryGate, QFT
from qiskit.quantum_info import DensityMatrix
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile

# =================
# Padding Function
# =================
def padding(matrix, alpha):
    # Initial dimension of matrices
    n = matrix.shape[0]

    # Finding the nearest power of two
    N = 2**(int(np.ceil(np.log2(n))))

    # If matrices already 2^n x 2^n
    pad = N - n
    if pad == 0:
        return matrix

    # Zero matrices with N x N dimension 
    matrix_padding = np.zeros((N, N))

    # The main block is filled with the primary matrix
    matrix_padding[:n, :n] = matrix

    # Padding is applied to the remaining blocks
    matrix_padding[n:, n:] = alpha * np.eye(pad)

    return matrix_padding

# =====================
# Gibbs State Function
# =====================
def gibbs_state(matrix, mu):
    exp_matrix = expm(-mu * matrix)
    return exp_matrix / np.trace(exp_matrix)

# =====================
# Trace of Gibbs State
# =====================
def trace(matrix, mu):
    exp_matrix = expm(-mu * matrix)
    return np.trace(exp_matrix)

# ==========================
# Unitary Operator Function
# ==========================
def unitary_operator(matrix, time):
    return expm(-1j * matrix * time)

# ===============================
# Quantum Phase Estimation (QPE)
# ===============================
def QuantumPhaseEstimation(quantum_circuit, unitary_matrix, n_control):
    # Determine the total qubit
    U_gate = UnitaryGate(unitary_matrix.data)
    n_target = U_gate.num_qubits
    total_qubit = n_control + n_target

    # Hadamard for control qubit
    for i in range(n_control):
        quantum_circuit.h(i)

    # Apply the Controlled-U^(2^(k)) iteration
    target_qubits = list(range(n_control, total_qubit))
    for k in range(n_control):
        controlled_U = U_gate.power(2**k).control(1)
        quantum_circuit.append(controlled_U, [k] + target_qubits)

    # Apply the IQFT
    quantum_circuit.barrier()
    IQFT = QFT(
        num_qubits=n_control,
        inverse=True
    )
    quantum_circuit.append(IQFT, range(n_control))

# ===================
# Quantum Simulation
# ===================
def QuantumSimulation(Delta, parameters):
    # Parameter variation
    X = parameters

    # Constructing the Gibbs state
    mu = X[0]
    keadaan_gibbs = gibbs_state(Delta, mu)
    keadaan_gibbs = padding(keadaan_gibbs, 0)

    # Constructing the unitary operator
    t = X[1]
    operator_uniter = unitary_operator(padding(Delta, 1), t)

    # Initialization
    qubit_resolusi = X[2]
    qubit_sistem = int(np.log2(keadaan_gibbs.shape[0]))
    total_qubits = qubit_resolusi + qubit_sistem

    # Density matrix for resolution qubit
    rho_resolusi = np.zeros((2**qubit_resolusi, 2**qubit_resolusi), dtype=complex)
    rho_resolusi[0, 0] = 1

    # Density matrix for total qubit
    rho_total = np.kron(keadaan_gibbs, rho_resolusi)
    rho = DensityMatrix(rho_total)

    # Quantum circuit based density matrix
    qc = QuantumCircuit(total_qubits)
    qc.set_density_matrix(rho)

    # Apply the Quantum Phase Estimation
    QuantumPhaseEstimation(qc, operator_uniter, qubit_resolusi)
    qc.save_density_matrix()

    # Simulation
    sim = AerSimulator(method="density_matrix")
    qct = transpile(qc, sim)
    result = sim.run(qct).result()
    final_rho = result.data(0)['density_matrix']

    return total_qubits, final_rho