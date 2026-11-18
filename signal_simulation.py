
import numpy as np
import matplotlib.pyplot as plt
import os

# Create folder for saving graphs
os.makedirs("output_graphs", exist_ok=True)

# Signal parameters
A = 1
f = 5
fs = 40
T = 1

# Continuous time
t = np.linspace(0, T, 1000)

# Discrete time
n = np.arange(0, int(fs * T) + 1)
td = n / fs

# Generate sine signals
continuous_sine = A * np.sin(2 * np.pi * f * t)
discrete_sine = A * np.sin(2 * np.pi * f * td)

# Generate cosine signals
continuous_cosine = A * np.cos(2 * np.pi * f * t)
discrete_cosine = A * np.cos(2 * np.pi * f * td)

# Plot all four signals
plt.figure(figsize=(12, 9))

plt.subplot(2, 2, 1)
plt.plot(t, continuous_sine)
plt.title("Continuous-Time Sine Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.stem(n, discrete_sine)
plt.title("Discrete-Time Sine Signal")
plt.xlabel("Sample Number (n)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(t, continuous_cosine)
plt.title("Continuous-Time Cosine Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.stem(n, discrete_cosine)
plt.title("Discrete-Time Cosine Signal")
plt.xlabel("Sample Number (n)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()

# Save graph
plt.savefig("output_graphs/signal_comparison.png", dpi=300)

# Display graph
plt.show()

print("Signal simulation completed successfully!")
print("Graph saved in output_graphs folder.")
