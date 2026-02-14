[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18641268.svg)](https://doi.org/10.5281/zenodo.18641268)

n-adic Collatz Universe Laboratory  
Author: Hiroshi Harada  
Year: 2026  
License: CC BY 4.0 (Creative Commons Attribution 4.0 International)

------------------------------------------------------------

Description  
This archive provides a comprehensive and clean Python implementation of the
n-adic Collatz Universe, a theoretical framework that generalizes the classic
Collatz conjecture (3x + 1) to any integer base n.

The system operates on a dual-phase dynamical model:

- Adaptive Recursive Division (ARD): Acts as gravitational collapse,
  prioritizing division by the largest available divisors of n.

- Modular Jump Phase: For numbers coprime to n, the system applies an
  acceleration jump:
    ((n + 1) * x + c_r) / n
  where r = x mod n, and c_r is a modular constant chosen so that
  r + c_r is divisible by n.

By adjusting the base n and the jump constants c_r, users can design and
explore numerical universes with varying behaviors: rapid convergence,
stable cycles (traps), or unbounded divergence.

Example: Collatz-4 Universe (n = 4)

In the 4-adic universe, gravitational forces from divisors 4 and 2 dominate
the collapse phase, while modular jumps provide asymmetric accelerations.
With modular constants set as c₁ = -1 and c₃ = +1, the system exhibits a rich
interplay of descent and surge.

Starting from 20737, the orbit undergoes a dramatic sequence of transformations,
reaching a maximum value of 150,876 before converging to 1 in 41 steps.
This trajectory exemplifies high-altitude oscillations followed by gravitational
stabilization—a signature of 4-adic turbulence.

------------------------------------------------------------

Key Features

- Universal Base Selection: Explore any base n, such as 4, 6, 7, 12, 18, or 30.
- Smart Constant Mapping: The system identifies all remainders r coprime to n
  and prompts for valid c_r values.
- Automated Universe Scanner: Includes a batch scan mode (1 to 100) to
  statistically map convergence rates and detect attractors.
- Cycle Detection: Uses memory-based tracking to detect fixed points and
  multi-node loops efficiently.
- Integer-Safe Dynamics: All operations are guaranteed to remain within the
  integer domain.

------------------------------------------------------------

Files in this Archive

- n_adic_lab.py : The core simulation and exploration engine
- README.txt    : This documentation and theoretical overview
- LICENSE       : Full text of the CC BY 4.0 license

------------------------------------------------------------

Purpose

This laboratory is designed for:

- Generalizing Number Theory: Moving beyond the n = 2 constraint of the classic
  Collatz problem.
- Universe Design: Engineering specific cycles or “Sanctuary Points” by tuning c_r.
- Statistical Mechanics of Orbits: Comparing orbit behaviors in high-gravity
  (composite) vs. high-energy (prime) bases.
- Educational Exploration: Visualizing the interplay between modular arithmetic
  and iterative dynamics.

------------------------------------------------------------

Methodology

The implementation follows a gravity-first approach.
For example, in an n = 4 universe, the system checks for divisibility by 4 and 2
before applying any jump. This simulates how composite bases naturally collapse
values toward the ground state (1), while prime bases tend to produce more
energetic, chaotic orbits.

------------------------------------------------------------

Citation

If you use this framework or publish results based on simulations from this lab,
please cite the Zenodo DOI associated with this archive.

------------------------------------------------------------

Contact

Hiroshi Harada
