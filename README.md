
# Glider Snake Optimization (GSO)

## Overview

Glider Snake Optimization (GSO) is a novel nature-inspired metaheuristic optimization algorithm motivated by the gliding and serpentine locomotion behavior of arboreal snakes. The algorithm models the search process as a cooperative chain of agents, where each agent updates its position based on both global leader guidance and local predecessor interaction. This mechanism enables an effective balance between exploration and exploitation, particularly in complex and high-dimensional optimization problems.

This repository provides the official Python implementation of the GSO algorithm used in the experimental evaluations reported in the corresponding research paper.

---

## Repository Contents

The repository includes the following files:

* **GSO.py**: Core Python implementation of the Glider Snake Optimization algorithm
* **README.md**: Documentation and usage instructions

---

## Requirements

The implementation requires:

* Python **3.8** or later
* **NumPy** library
* **random** (standard library)

Install NumPy using:

```bash
pip install numpy
```

---

## Installation

Clone or download this repository and ensure NumPy is installed.

---

## Usage

The GSO function optimizes continuous problems. Define your fitness function, then call GSO with parameters.

### Example: Sphere Function

```python
import numpy as np

def sphere(x):
    return np.sum(x**2)

result = GSO(
    fitness_func=sphere,
    sol_count=10,
    dimensions=30,
    iterations_count=100,
    lower_bound=-100,
    upper_bound=100,
    mutation_rate=0.5,
    verbose=True
)

print(f"Best fitness: {result.leader_fitness}")
print(f"Best solution: {result.leader_solution}")
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `fitness_func` | function | - | Objective function to minimize |
| `sol_count` | int | - | Population size (recommended: 10) |
| `dimensions` | int | - | Problem dimensionality |
| `iterations_count` | int | - | Max iterations (recommended: 100) |
| `lower_bound` | float/list | - | Lower search bound(s) |
| `upper_bound` | float/list | - | Upper search bound(s) |
| `mutation_rate` | float | 0.5 | Probability for chain mutation |
| `stopping_func` | function | None | Custom stopping criterion |
| `plt_func` | function | None | Plotting callback |
| `verbose` | bool | True | Print progress |

---

## Algorithm Details

GSO sorts the population by fitness each iteration (elitism preserved). Followers update via:

- **Mutation mode** (if `mutation_rate > m` and rank > 50%): Chain + leader influence
- **Chain mode**: Global leader + nearest neighbor pull

Adaptive parameter \( A = 1 - t / T_{\max} \) controls step size.

---





---

## Citation

Cite the GSO paper if used in research.
