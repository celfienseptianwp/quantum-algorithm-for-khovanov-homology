# $\text{Optimizing Quantum Algorithm Parameters for Comuting Khovanov Homology}$

## 📖 Overview

Computing Khovanov Homology using Quantum Phase Estimation (QPE) requires careful selection of algorithmic parameters to achieve accurate estimations while minimizing quantum resource consumption. Improper parameter settings may lead to significant estimation errors or unnecessary computational costs.

This research investigates the optimization of Quantum Phase Estimation parameters using **Response Surface Methodology (RSM)**. The study models the relationship between quantum algorithm parameters and estimation error, enabling the identification of parameter combinations that minimize error when compared with reference values obtained from the **Knot Atlas**.

---

## 🎯 Research Objectives

- Implement Quantum Phase Estimation (QPE) for computing Khovanov Homology.
- Investigate the influence of quantum algorithm parameters on estimation accuracy.
- Build a statistical response surface model using experimental data.
- Determine the optimal parameter combination that minimizes estimation error.
- Validate optimized parameters against reference Khovanov Homology values from the Knot Atlas.

---

## ⚙️ Research Methodology

The research consists of the following stages:

1. Implement the Quantum Phase Estimation algorithm.
2. Generate experimental data using different parameter combinations.
3. Compare estimated values with reference data from the Knot Atlas.
4. Calculate estimation errors.
5. Construct a Response Surface Methodology (RSM) model.
6. Perform optimization to identify the minimum-error parameter combination.
7. Validate the optimized parameters through additional experiments.

---

## 🔬 Experimental Factors

Three independent variables are investigated:

| Factor | Description |
|---------|-------------|
| Inverse Temperature (β) | Controls the quantum state preparation. |
| Evolution Time (t) | Determines the evolution duration in Quantum Phase Estimation. |
| Resolution Qubits (n) | Number of qubits used in the QPE register, affecting estimation precision. |

---

## 📊 Response Variable

The response variable is

**Estimation Error**

which is calculated as the difference between the quantum-computed Khovanov Homology and the reference values provided by the **Knot Atlas**.

---

## 📈 Experiment Results

### Experimental Design

The experiments are conducted using **Response Surface Methodology (RSM)** with three numerical factors:

| Variable | Symbol |
|----------|--------|
| Inverse Temperature | β |
| Evolution Time | t |
| Resolution Qubits | n |

The response is

- Estimation Error

---

### Evaluation Metrics

The optimized quantum algorithm is evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Relative Error (%)
- Quantum Circuit Depth
- Number of Quantum Gates
- Number of Qubits

---

### Data Source

Ground-truth Khovanov Homology values are obtained from:

- **Knot Atlas**

These reference values are used to evaluate the accuracy of the Quantum Phase Estimation algorithm.

---

### Optimization Output

The optimization process aims to determine:

- Optimal inverse temperature (β)
- Optimal evolution time (t)
- Optimal number of QPE resolution qubits (n)
- Minimum estimation error
- Predicted response surface
- Interaction effects among variables

---

### Planned Visualizations

- Response Surface Plot (3D)
- Contour Plot
- Main Effect Plot
- Interaction Plot
- Pareto Chart of Effects (if applicable)
- Residual Analysis
- Predicted vs Actual Error
- Error Distribution

---

### Current Progress

- ✅ Literature review completed
- ✅ Quantum algorithm formulation
- 🔄 Quantum Phase Estimation implementation
- 🔄 Experimental data generation
- ⏳ Response Surface Methodology modeling
- ⏳ Parameter optimization
- ⏳ Validation using Knot Atlas