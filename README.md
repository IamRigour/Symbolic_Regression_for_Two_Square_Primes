# Symbolic Regression for Two Square Primes

This project studies primes expressible as the sum of two squares:

$$
p = a^2 + b^2,\quad a,b \in \mathbb{Z}
$$

Goal:* By Fermat’s theorem, these are exactly the primes $p = 2$ or $p \equiv 1 \ (\bmod\ 4)$.
Having come up with a 'not-so-good' approximation for $\pi_{2\text{sq}}(x)$, we seek to use symbolic regression to make this approximation better than it is, although it may not be better than $\frac{x}{2\log x}$.
$$
\pi_{2\text{sq}}(x) \sim \frac{x}{2 \ln x}.
$$

*Method:*
1. Generate primes $p \leq N$ with $p = a^2 + b^2$.
2. Compute $\pi_{2\text{sq}}(x)$.
3. Use Deap to fit $f(x)$.
4. Compare performance with PNT-based estimates.


