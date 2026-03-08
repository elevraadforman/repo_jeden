import matplotlib.pyplot as plt
import numpy as np

# Create figure 1: Linear function
x1 = np.linspace(-10, 10, 100)
y1 = 2 * x1 + 3

fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.plot(x1, y1, 'b-', linewidth=2)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.grid(True, alpha=0.3)
title1 = ax1.set_title('Linear Function: y = 2x + 3', fontsize=24, fontweight='bold', fontfamily='serif')
fig1.savefig('figure1_linear.png', dpi=300, bbox_inches='tight')
plt.close(fig1)

# Create figure 2: Quadratic function
x2 = np.linspace(-5, 5, 100)
y2 = x2**2 - 2*x2 + 1

fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.plot(x2, y2, 'r-', linewidth=2)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.grid(True, alpha=0.3)
title2 = ax2.set_title('Quadratic Function: y = x² - 2x + 1', fontsize=24, fontweight='bold', fontfamily='serif')
fig2.savefig('figure2_quadratic.png', dpi=300, bbox_inches='tight')
plt.close(fig2)

# Create figure 3: Sine function
x3 = np.linspace(0, 2*np.pi, 100)
y3 = np.sin(x3)

fig3, ax3 = plt.subplots(figsize=(8, 6))
ax3.plot(x3, y3, 'g-', linewidth=2)
ax3.set_xlabel('x', fontsize=12)
ax3.set_ylabel('y', fontsize=12)
ax3.grid(True, alpha=0.3)
title3 = ax3.set_title('Sine Function: y = sin(x)', fontsize=24, fontweight='bold', fontfamily='serif')
fig3.savefig('figure3_sine.png', dpi=300, bbox_inches='tight')
plt.close(fig3)
