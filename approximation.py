import numpy as np
from scipy.integrate import quad
from math import sqrt, log
import csv

# Define the counting function

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



# Implement the approximation

K = 0.76422365358922
y = 100

def c_val(y):
    return pi_2sq(y)

def term_one(x):
    return K*x/(log(x))**1.5

def term_two(y):
    return K*y/(log(y))**1.5

def two_term_asymptotic_expansion(t):
     return t / (np.log(t)**1.5) + 3*t/(2*(np.log(t))**2.5)


def asymptotic_integral(x,y):
    return two_term_asymptotic_expansion(x) - two_term_asymptotic_expansion(y)

def approximation(x, y=100):
    return c_val(y) + term_one(x) - term_two(y) + K*asymptotic_integral(x, y)


    


def generate_csv(filename, x_values):
  
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["x", "actual", "approx"])
        for x in x_values:
            actual = pi_2sq(x)
            approx = approximation(x) 
            writer.writerow([x, actual, approx])
            

x_values =  list(range(10**3, 10**8+1, 10**3))
generate_csv("updated_two-square-primes_and_approx.csv", x_values)
