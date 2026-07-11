# $\text{Optimization of Quantum Knot Algorithm}$

A research project focused on optimizing quantum algorithm parameters for computing **Khovanov Homology**, aiming to improve computational efficiency, circuit performance, and scalability. The project investigates how different quantum circuit configurations influence the accuracy and resource requirements of homology computations.

## 📖 $\text{Overview}$

Computing Khovanov Homology using **Quantum Phase Estimation (QPE)** requires careful selection of algorithmic parameters to achieve accurate estimations while minimizing quantum resource consumption. Improper parameter settings may lead to significant estimation errors or unnecessary computational costs.

This research investigates the optimization of Quantum Phase Estimation parameters using **Response Surface Methodology (RSM)**. The study models the relationship between quantum algorithm parameters and estimation error, enabling the identification of parameter combinations that minimize error when compared with reference values obtained from the **Knot Atlas**.

## 🎯 $\text{Research Objectives}$

- Implement **QPE** for computing Khovanov Homology.
- Investigate the influence of quantum algorithm parameters on estimation accuracy.
- Build a statistical response surface model using experimental data.
- Determine the optimal parameter combination that minimizes estimation error.
- Validate optimized parameters against reference Khovanov Homology values from the **Knot Atlas**.

## ⚙️ $\text{Research Methodology}$

The research consists of the following stages:

1. Implement QPE with eigenstates in the form of Gibbs state density matrices derived from the Khovanov Laplacian.
2. Generate experimental data using different parameter combinations based **Reduced Five Level Factorial Design (R-FLFD)**.
3. Compare estimated values with reference data from the Knot Atlas.
4. Calculate estimation errors.
5. Construct a Response Surface Methodology (RSM) model.
6. Perform optimization to identify the minimum-error parameter combination.
7. Validate the optimized parameters through additional experiments.

## 🔬 $\text{Experimental Factors}$

Three independent variables are investigated:

| Factor | Description |
|---------|-------------|
| Inverse Temperature | Controls the quantum state preparation. |
| Evolution Time | Determines the evolution duration in Quantum Phase Estimation. |
| Resolution Qubits | Number of qubits used in the QPE register, affecting estimation precision. |

## 📊 $\text{Response Variable}$

The response variable is **Estimation Error** which is calculated as the difference between the quantum-computed Khovanov Homology and the reference values provided by the **Knot Atlas**.

## 📈 $\text{Experiment Results}$

### Evaluation Metrics

The optimized quantum algorithm is evaluated using:

- Residual
- Coefficient of Determination
- Number of Qubits

### Data Source

Ground-truth Khovanov Homology values are obtained from **Knot Atlas** ( https://katlas.org/wiki/Main_Page ). These reference values are used to evaluate the accuracy of the Quantum Phase Estimation algorithm.

### Optimization Output

The optimization process aims to determine:

- Optimal inverse temperature (β)
- Optimal evolution time (t)
- Optimal number of QPE resolution qubits (n)
- Minimum estimation error
- Predicted response surface
- Interaction effects among variables

### Planned Visualizations

- Response Surface Plot (3D)
- Contour Plot
- Residual Analysis
- Predicted vs Actual Error
- Error Distribution

### Current Progress

- ✅ Literature review completed
- ✅ Quantum algorithm formulation
- ✅ Quantum Phase Estimation implementation
- ✅ Experimental data generation
- ✅ Response Surface Methodology modeling
- ✅ Parameter optimization
- ✅ Validation using Knot Atlas