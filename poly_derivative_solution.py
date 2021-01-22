# Task 1
# Polynomial coefficients
a0 = 1
a1 = -2
a2 = 4.6
a3 = 0.2

# Point at which we evaluate the derivative
x0 = 3.1

# Calculate the derivative
p_prime = a1 + 2*a2*x0 + 3*a3*x0**2

# This will be True if the code is correct
print(p_prime == 32.286)



# Task 3
def eval_derivative(a, x0):
    '''
    Evaluate the derivative at x0 of a polynomial defined by
    coefficients a, given as a list.
    '''
    # Get the number of coefficients
    N = len(a)

    # Initialise the sum
    p_prime = 0

    # Loop over the coefficients to add each term separately (starting at degree 1)
    for i in range(1, N):
        # Add the term of degree i-1
        p_prime += i * a[i] * x0**(i-1)

    # Return the derivative
    return p_prime


# Tests
print(eval_derivative([1, -2, 4.6, 0.2], 3.1) == 32.286)
print(eval_derivative([0], 72.1419) == 0)           # p(x) = 0
print(eval_derivative([999.9], 72.1419) == 0)       # p(x) = 999.9 (or any other arbitrary constant)
print(eval_derivative([1, 2], 123.456) == 2)        # p(x) = 2x + 1
print(eval_derivative([0]*10 + [1], 2) == 5120)     # p(x) = x^10
print(eval_derivative([0, 1, -1, 0, 0, 0, 1], 1.5) == 43.5625)   # p(x) = x^6 - x^2 + x
# etc...


# Task 3 challenge: mth order derivative
def eval_mth_derivative(a, m, x0):
    '''
    Evaluate the mth derivative at x0 of a polynomial defined by
    coefficients a, given as a list.
    '''
    # Get the number of coefficients
    N = len(a)

    # Initialise the sum
    p_prime = 0

    # Loop over the coefficients to add each term separately (starting at degree m)
    for i in range(m, N):
        # Calculate the term without coefficient first
        term = x0**(i-m)
        
        # Multiply by a_i coefficient
        term *= a[i]
        
        # Loop to multiply the term by i(i-1)(i-2)....(i-(m-1))
        for k in range(m):
            term *= i - k
        
        # Finally, add the term of degree i-m to p_prime
        p_prime += term

    # Return the derivative
    return p_prime

# Tests
print(eval_mth_derivative([0, 1, -1, 0, 0, 0, 1], 1, 1.5) == 43.5625)
print(eval_mth_derivative([1, -2, 4.6, 0.2], 1, 3.1) == 32.286)

# Think about why these work...
import math
print(eval_mth_derivative([123, 456, 789, 101112, 131415, 1], 5, 1) == math.factorial(5))
print(eval_mth_derivative([0]*10 + [1], 9, 2) == 2 * math.factorial(10))
print(eval_mth_derivative([1, -2, 4.6, 0.2], 0, 1) == sum([1, -2, 4.6, 0.2]))