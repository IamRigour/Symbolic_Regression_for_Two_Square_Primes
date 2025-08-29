import numpy as np
from scipy.integrate import quad
from math import sqrt, log
import csv
import pyprimesieve
from time import perf_counter
import numba

# Define the counting function
@numba.njit
def pi_2sq(n):
    prime = np.ones(n+1, dtype=np.bool_)
    prime[:2] = False  # 0 and 1 not prime
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    count = 0
    for p in range(2, n+1):
        if prime[p] and (p == 2 or p % 4 == 1):
            count += 1
    return count

# Implement the new approximation
K = 0.76422365358922
y = 100

def c_val(y):
    return pi_2sq(y)

def term_one(x):
    return K*x/(log(x))**1.5

def term_two(y):
    return K*y/(log(y))**1.5

def integrand(x):
    return 1 / (np.log(x)**1.5)

def integrate_chunked(a, b, chunks=1000):
    points = np.linspace(a, b, chunks+1)
    total = 0
    for i in range(chunks):
        val, _ = quad(integrand, points[i], points[i+1])
        total += val
    return total

def new_approximation(x):
    return c_val(y) + term_one(x) - term_two(y) + K*integrate_chunked(y, x)

def generate_csv(filename, x_values):
    total = len(x_values)
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["x", "actual", "approx"])
        for idx, x in enumerate(x_values, start=1):
            actual = pi_2sq(x)
            approx = new_approximation(x)
            writer.writerow([x, actual, approx])

            # Single-line progress update
            percent = (idx / total) * 100
            print(f"\rProgress: {percent:.2f}% ({idx}/{total})", end="")

    print("\nProcessing complete!")

start = perf_counter()
x_values = list(range(10**3, 10**8+1, 10**3))
generate_csv("two-square-primes_and_approx.csv", x_values)
end = perf_counter()

print(f"Time taken: {end - start:.2f} seconds")
