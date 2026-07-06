# =====================================
# Khovanov Laplacian Matrices for Link
# =====================================
import numpy as np
from scipy.linalg import block_diag

# L2a1 as Hopf Link
def l2a1():
    # Differential d^0 matrices
    d0 = np.array([
        [1, 0, 0, 0],
        [0, 1, 1, 0],
        [1, 0, 0, 0],
        [0, 1, 1, 0]
    ], dtype=float)

    # Differential d^1 matrices
    d1 = np.array([
        [0, 0, 0, 0],
        [1, 0, -1, 0],
        [1, 0, -1, 0],
        [0, 1, 0, -1]
    ], dtype=float)

    # Define the 0th Laplacian
    Delta0 = d0.conj().T @ d0

    # Define the 1st Laplacian
    Delta1 = d1.conj().T @ d1 + d0 @ d0.conj().T

    # Define the 2nd Laplacian
    Delta2 = d1 @ d1.conj().T

    # Direct sum for every Laplacian (Global Laplacian)
    Delta = block_diag(Delta0, Delta1, Delta2)

    return Delta