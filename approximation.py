import numpy as np
from scipy.integrate import quad
from math import sqrt, log
import csv
import  pyprimesieve
from time import perf_counter
# Define the counting function

from math import sqrt

def pi_2sq(x):
    step_size = int(sqrt(x))
    pi_vals = {}

    # Initial block - using primesieve
    x_0 = step_size
    primes = pyprimesieve.primes(1, x_0 + 1)
    pi_vals[x_0] = sum(1 for p in primes if p == 2 or p % 4 == 1)

    i = x_0
    while i <= x - step_size:
        new_x = i + step_size
        # Get primes in the current range
        primes = pyprimesieve.primes(i + 1, new_x + 1)
        pi_vals[new_x] = pi_vals[i] + sum(1 for p in primes if p == 2 or p % 4 == 1)
        i = new_x

    if i < x:
        primes = pyprimesieve.primes(i + 1, x + 1)
        pi_vals[x] = pi_vals[i] + sum(1 for p in primes if p == 2 or p % 4 == 1)
    
    return pi_vals[x]



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

def integrate_chunked(a, b, chunks=10_000):
    points = np.linspace(a, b, chunks+1)
    total = 0
    for i in range(chunks):
        val, _ = quad(integrand, points[i], points[i+1])
        total += val
    return total

def new_approximation(x):
    return c_val(y) + term_one(x) - term_two(y) + K*integrate_chunked(y, x)


def generate_csv(filename, x_values):
    print("First")
    with open(filename, mode="w", newline="") as file:
        print("Second")
        writer = csv.writer(file)
        writer.writerow(["x", "actual", "approx"])
        # print(f"x_vals: {x_values}")
        for x in x_values:
            print(f"Third: ", x)
            actual = pi_2sq(x)
            approx = 0 #new_approximation(x)
            writer.writerow([x, actual, approx])
            print(f"Actual: {actual}, Approximate: {approx}")


x_values =  list(range(10**3, 10**8, 10**3))

generate_csv("2sq_and_approx.csv", x_values)