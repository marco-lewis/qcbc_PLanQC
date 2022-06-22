# Checks for Barrier Certificates on Quantum Systems

A repository containing the related files to run the checks of the example given in the Extended Abstract ("Verification of Quantum Systems using Barrier Certificates").

## Setup and Running the Code
You may want to create a virtual environment beforehand. While inside the local repository, run the following:

`mkdir env && cd env`

`python3 -m venv env`

`source env/bin/activate`

1. Install the Z3 SMT solver (available at https://github.com/Z3Prover/z3).

2. Run ``` pip install requirements.txt```

3. Run ```python SMT_checks.py```

## Files

- complex.py - modified example from https://github.com/Z3Prover/z3/blob/master/examples/python/complex/complex.py
- requirements.txt - contains rquired packages to install
- SMT_checks.py - checks on the barrier provided in "Verification of Quantum Systems using Barrier Certificates"
