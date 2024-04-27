import numpy as np
import matplotlib.pyplot as plt

def numeric():
    # Length of Rod, Time Interval
    L = 1
    T = float(input("Enter the time interval (T): "))
    k = 1
    N = 10
    M = 50
    dx = L / N
    dt = T / M
    alpha = k * dt / dx**2

    # Position
    x = np.linspace(0, L, N+1)

    # Initial Condition
    u0 = np.sin(np.pi * x)

    # Partial Difference Equation (Numerical Scheme)
    u1 = np.copy(u0)
    for j in range(M):
        for i in range(1, N):
            u1[i] = u0[i] + alpha * (u0[i+1] - 2 * u0[i] + u0[i-1])
        u1[0] = 0
        u1[N] = 0
        u0 = np.copy(u1)

    # Plot solution
    plt.plot(x, u1)
    plt.xlabel('Position')
    plt.ylabel('Temperature')
    plt.title('Solution of the Heat Equation')
    plt.grid(True)
    plt.show()

# Call the function
numeric()
