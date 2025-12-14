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

Install NumPy using:

```bash
pip install numpy
```

---

## Usage

The GSO algorithm can be applied to continuous optimization problems by defining an objective function and specifying the problem dimensions and bounds. The provided implementation follows the same configuration used in the experimental section of the paper.

A typical workflow includes:

1. Defining the objective function
2. Setting problem dimensionality and bounds
3. Initializing the GSO optimizer
4. Running the optimization process to obtain the best solution

---

## Algorithm Parameters

The main parameters of GSO are:

* **Population size (number of search agents)**: 10
* **Maximum number of iterations**: 100
* **Adaptive control parameter (A)**: linearly decreases from 1 to 0
* **Lower and upper bounds**: problem-dependent

Unless otherwise stated, all reported results in the paper were obtained using **10 agents** and **100 iterations** to ensure fair comparison with competing algorithms.

---

## Experimental Setup

All experiments were conducted on a fixed computational platform to ensure fairness and reproducibility. The system configuration is as follows:

* **CPU**: AMD Ryzen 7 5800X
* **RAM**: 16 GB DDR4 (3200 MHz)
* **GPU**: NVIDIA RTX 4060 (12 GB)
* **Operating System**: Windows 11 Pro (64-bit)

---

## Benchmark Problems

The GSO algorithm was evaluated on:

* 23 classical benchmark functions
* CEC 2019 benchmark suite
* High-dimensional optimization problems (100, 500, and 1000 dimensions)
* Constrained real-world engineering design problems

---

## Reproducibility

The source code in this repository corresponds exactly to the version used in the reported experiments. All benchmark tests were executed multiple times, and the following statistics were recorded:

* Best value
* Worst value
* Mean value
* Standard deviation

Initial solutions were generated using uniform random distributions within the defined search bounds.

---

## Citation

If you use this code in your research, please cite the corresponding paper describing the Glider Snake Optimization (GSO) algorithm.
