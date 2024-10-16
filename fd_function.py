import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def df_exact(x):
    return np.cos(x)

def central_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_diff(f, x, h):
    return (f(x) - f(x - h)) / h

def smooth_filter(signal, window_size):
    kernel = np.ones(window_size) / window_size
    smoothed_signal = np.convolve(signal, kernel, mode='same')
    return smoothed_signal


#smooth filter
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
window_size = 5
smoothed_signal = smooth_filter(y, window_size)
derivative = np.gradient(smoothed_signal, x)


# Define the range of x values to evaluate the derivative
x_vals = np.linspace(0, 2 * np.pi, 100)


# Define the step size for the finite difference formulas
h = 0.1



# the central difference formula
central = central_diff(f, x_vals, h)

#forward difference formula
forward = forward_diff(f, x_vals, h)

#backward difference formula
backward = backward_diff(f, x_vals, h)

def test(f, df_exact):
    points = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    for h in points:
        print("h =", h)
        for x in [1, 2, 3]:
            df_cd = central_diff(f, x, h)
            df_fd = forward_diff(f, x, h)
            df_bd = backward_diff(f, x, h)
            df_exact_val = df_exact(x)
            print("x =", x)
            print("Exact derivative:", df_exact_val)
            print("Central difference:", df_cd)
            print("Forward difference:", df_fd)
            print("Backward difference:", df_bd)
            print("Absolute error for central difference:", abs(df_cd - df_exact_val))
            print("Absolute error for forward difference:", abs(df_fd - df_exact_val))
            print("Absolute error for backward difference:", abs(df_bd - df_exact_val))
            print()

# Plot the results using matplotlib
plt.plot(x_vals, derivative, label='smooth filter')
plt.plot(x_vals, forward, label='Forward Difference')
plt.plot(x_vals, backward, label='Backward Difference')
plt.plot(x_vals, np.cos(x_vals), label='True Derivative')
plt.legend()


test(f, df_exact)

plt.show()
