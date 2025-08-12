# Symbolic Regression for Two Square Primes

This project studies primes expressible as the sum of two squares:

$$
p = a^2 + b^2,\quad a,b \in \mathbb{Z}
$$

By Fermat’s theorem, these are exactly the primes $p = 2$ or $p \equiv 1 \ (\bmod\ 4)$.

*Goal:* Use *symbolic regression* to find a closed-form approximation  
$\pi_{2\text{sq}}(x) \approx f(x)$ for the count of such primes up to $x$,  
aiming for *better accuracy* than the classical Prime Number Theorem estimate:

$$
\pi_{2\text{sq}}(x) \sim \frac{x}{2 \ln x}.
$$

*Method:*
1. Generate primes $p \leq N$ with $p = a^2 + b^2$.
2. Compute $\pi_{2\text{sq}}(x)$.
3. Use Deap to fit $f(x)$.
4. Compare performance with PNT-based estimates.


