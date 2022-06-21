import numpy as np
from z3 import *
from complex import Complex, ComplexExpr, I

# Complex setting
# Definition of dynamical system and complex conjugate
f = lambda a,b: np.array([0 - I * (a + b)/Sqrt(2), 0 - I * (a - b)/Sqrt(2)])
fbar = lambda a,b: np.array([I * (a.conj() + b.conj())/Sqrt(2), I * (a.conj() - b.conj())/Sqrt(2)])

# Definition of barrier and its differential
B = lambda a, b: 1.2 - 2 * a * a.conj() - a.conj() * b - a * b.conj()
dBdz = lambda a, b: np.array([0 - a.conj() - b.conj(), b.conj() - a.conj()])
dBdzconj = lambda a, b: np.array([0 - a - b, b - a])
dBdt = lambda a, b: np.dot(dBdz(a, b), f(a, b)) + np.dot(dBdzconj(a, b), fbar(a, b))

# Initialise a Solver and state
s = Solver()
z0 = Complex('z_0')
z1 = Complex('z_1')
state = [z0, z1]

# Add proof constraints
s.add(Or(
    # Barrier is only real on all possible states
    And(state[0].len_sqr() + state[1].len_sqr() == 1, 
        Not(B(state[0], state[1]).i == 0)),
    # Barrier condition for initial region
    And(state[0].len_sqr() >= 0.9, 
        state[0].len_sqr() + state[1].len_sqr() == 1,
        Not(And(B(state[0], state[1]).r <= 0, B(state[0], state[1]).i == 0))),
    # Barrier condition for unsafe region
    And(state[0].len_sqr() < 0.1, 
        state[0].len_sqr() + state[1].len_sqr() == 1,
        Not(And(B(state[0], state[1]).r > 0, B(state[0], state[1]).i == 0))),
    # Barrier condition for convex condition
    And(state[0].len_sqr() + state[1].len_sqr() == 1, 
      Not(And(dBdt(state[0], state[1]).r <= 0, dBdt(state[0], state[1]).i == 0)))
))

# Perform checks
sat = s.check()
print(sat)
if sat == z3.sat:
    m = s.model()
    print(m)
if sat == z3.unsat: print("Barrier meets all conditions")
