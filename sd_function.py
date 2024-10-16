import numpy as np
import matplotlib.pyplot as plt

def central_diff(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

def forward_diff(f, x, h):
    return (f(x + 2 * h) - 2 * f(x + h) + f(x)) / (h ** 2)

def backward_diff(f, x, h):
    return (f(x) - 2 * f(x - h) + f(x - 2 * h)) / (h ** 2)


def smooth_filter(y, h):
    n = len(y)
    derivative = np.zeros(n)

    for i in range(1, n-1):
        derivative[i] = (y[i+1] - 2*y[i] + y[i-1]) / (h**2)

    return derivative

def df_exact(x):
    return -np.sin(x)

# Define the function to differentiate
def f(x):
    return np.sin(x)

# Smooth filter
x_vals = np.linspace(0, 2 * np.pi, 100)

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Specify the step size
h = x[1] - x[0]

# smooth filter formula
derivative = smooth_filter(y, h)

# central difference formula
central = central_diff(f, x_vals, h)

# forward difference formula
forward = forward_diff(f, x_vals, h)

# backward difference formula
backward = backward_diff(f, x_vals, h)

def test_for_finite_differences(f, df_exact):
    points = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    for h in points:
        print("h =", h)
        for x in [0.5, 1, 2, 3]:
            df_cd = central_diff(f, x, h)
            df_fd = forward_diff(f, x, h)
            df_bd = backward_diff(f, x, h)

            df_sf = smooth_filter(y, h)
            df_exact_val = df_exact(x)
            print("x =", x)
            print("Exact derivative:", df_exact_val)
            print("Central difference:", df_cd)
            print("Forward difference:", df_fd)
            print("Backward difference:", df_bd)
            print("Smooth Filter:", df_sf[0])
            print("Absolute error for central difference:", abs(df_cd - df_exact_val))
            print("Absolute error for forward difference:", abs(df_fd - df_exact_val))
            print("Absolute error for backward difference:", abs(df_bd - df_exact_val))
            print()




plt.plot(x_vals, derivative, label='Smooth Filter')
plt.plot(x_vals, central, label='Central Difference')
plt.plot(x_vals, forward, label='Forward Difference')
plt.plot(x_vals, backward, label='Backward Difference')
plt.plot(x_vals, -np.sin(x_vals), label='True Derivative')
plt.legend()
test_for_finite_differences(f, df_exact)

plt.show()
