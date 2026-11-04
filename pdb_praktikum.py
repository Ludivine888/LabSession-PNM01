import math

# Definisi PDB: dy/dx = f(x, y)
def f(x, y):
    return (x**2 + 2*y) / (x + 1)

# Solusi Analitik Eksak
def y_eksak(x):
    return (x + 1)**2 * math.log(x + 1) + 2*(x + 1) - 0.5 + 0.5*(x + 1)**2

# Parameter Soal
x0 = 0.0
y0 = 2.0
h = 0.2
target_x = 0.4
steps = int(round((target_x - x0) / h))

print("=== SOAL 1: PERSAMAAN DIFERENSIAL BIASA ===")
print(f"h = {h}, N = {steps} iterasi, Target x = {target_x}\n")

# A. METODE EULER
x_e, y_e = x0, y0
for i in range(steps):
    y_e = y_e + h * f(x_e, y_e)
    x_e = x_e + h
print(f"[Euler]  y({target_x:.1f}) = {y_e:.6f}")

# B. METODE HEUN (RK-2)
x_h, y_h = x0, y0
for i in range(steps):
    k1 = f(x_h, y_h)
    k2 = f(x_h + h, y_h + h * k1)
    y_h = y_h + (h / 2.0) * (k1 + k2)
    x_h = x_h + h
print(f"[Heun]   y({target_x:.1f}) = {y_h:.6f}")

# C. METODE RUNGE-KUTTA ORDE-4 (RK4)
x_rk, y_rk = x0, y0
for i in range(steps):
    k1 = f(x_rk, y_rk)
    k2 = f(x_rk + h/2.0, y_rk + (h/2.0) * k1)
    k3 = f(x_rk + h/2.0, y_rk + (h/2.0) * k2)
    k4 = f(x_rk + h, y_rk + h * k3)
    y_rk = y_rk + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
    x_rk = x_rk + h
print(f"[RK-4]   y({target_x:.1f}) = {y_rk:.6f}")

# D. SOLUSI EKSAK & ANALISIS GALAT
exact = y_eksak(target_x)
print(f"[Eksak]  y({target_x:.1f}) = {exact:.6f}\n")

print("--- TABEL ANALISIS GALAT ---")
methods = [("Euler", y_e), ("Heun (RK-2)", y_h), ("Runge-Kutta 4", y_rk)]
print(f"{'Metode':<15} | {'Hasil':<10} | {'Galat Mutlak':<12} | {'Galat Relatif (%)':<15}")
print("-" * 62)
for name, val in methods:
    abs_err = abs(exact - val)
    rel_err = (abs_err / exact) * 100.0
    print(f"{name:<15} | {val:<10.6f} | {abs_err:<12.6f} | {rel_err:<15.6f}%")