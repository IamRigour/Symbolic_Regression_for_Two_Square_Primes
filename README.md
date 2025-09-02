# Symbolic regression for an approximation to the counting function of primes expressible as the sum of two squares  

We shall be using symbolic regression to imporve an approximation to $\pi_{2\text{sq}}(x)$.

We now derive an explicit approximation for $\pi_{2\text{sq}}(x)$ using Abel summation,
the Prime Number Theorem, and the Landau–Ramanujan asymptotic.

---

Let $1_{2\text{sq}}(n)$ denote the characteristic function of primes expressible as the sum of
two squares:
$$
1_{2\text{sq}}(n) =
\begin{cases}
1 & \text{if $n = a^2 + b^2$ for some integers $a,b$ and $n$ is prime},\\
0 & \text{otherwise}.
\end{cases}
$$
Then the counting function can be expressed precisely as
$$
\pi_{2\text{sq}}(x) = \sum_{n \leq x} 1_{2\text{sq}}(n).
$$

We also define the weighted sum
$$
S_{2\text{sq}}(x) = \sum_{n \leq x} n \, 1_{2\text{sq}}(n),
$$
which represents the sum of all two-square primes up to $x$.

To apply Abel’s summation formula, we split $\pi_{2\text{sq}}(x)$ at some $y < x$:

$$
\pi_{2\text{sq}}(x) = \sum_{n \leq x} 1_{2\text{sq}}(n)
= \sum_{n \leq y} 1_{2\text{sq}}(n) + \sum_{y < n \leq x} 1_{2\text{sq}}(n)
= C(y) + \sum_{y < n \leq x} \frac{n 1_{2\text{sq}}(n)}{n},
$$
where $C(y)$ denotes the number of two-square primes $\leq y$.

Now we recognize the second sum as suitable for Abel summation, with
$a_n = n1_{2\text{sq}}(n)$ and $f(n) = 1/n$.

By Abel’s summation formula,
$$
\pi_{2\text{sq}}(x) = C(y) + \frac{S_{2\text{sq}}(x)}{x} - \frac{S_{2\text{sq}}(y)}{y} +
\int_y^x \frac{S_{2\text{sq}}(t)}{t^2}\,dt.
$$

The Landau–Ramanujan theorem gives the number of integers $\leq t$ expressible
as a sum of two squares:
$$
N(t) \sim \frac{K t}{\sqrt{\log t}}, \quad K \approx 0.76422\ldots
$$
Meanwhile, the Prime Number Theorem suggests that the “probability” of an
integer near $t$ being prime is about $1/\log t$. Combining these heuristics, the
expected number of two-square primes near $t$ is approximately
$$
\frac{K t}{\sqrt{\log t}} \cdot \frac{1}{\log t}.
$$

Since no such prime exceeds $t$, the contribution to their weighted sum is of order
$$
S_{2\text{sq}}(t) \approx \frac{K t^2}{(\log t)^{3/2}}.
$$

Substituting this into Abel’s formula yields
$$
\pi_{2\text{sq}}(x) \approx C(y) + \frac{Kx}{(\log x)^{3/2}}
- \frac{Ky}{(\log y)^{3/2}} + K \int_y^x \frac{dt}{(\log t)^{3/2}}.
$$
---

The goal is to use symbolic regression to improve this approximation.
