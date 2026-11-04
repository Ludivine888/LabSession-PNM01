import math

def f(x):
    return math.cos(x) - x

def f_turunan(x):
    return -math.sin(x) - 1.0

def g(x):
    return math.cos(x)

def g_turunan(x):
    return -math.sin(x)

x0 = 0.5
toleransi = 0.0001
maks_iterasi = 100

print("=== SOAL 2: SISTEM PERSAMAAN NON-LINEAR ===")
print(f"Persamaan: f(x) = cos(x) - x = 0, Tebakan Awal x0 = {x0}, Toleransi = {toleransi}\n")

# 1. FIXED-POINT ITERATION
print(">>> METODE FIXED-POINT ITERATION:")
turunan_awal = abs(g_turunan(x0))
print(f"Cek syarat konvergen: |g'({x0})| = {turunan_awal:.6f}")
if turunan_awal < 1:
    print("Status: |g'(x)| < 1 (Aman, konvergen!)\n")
    x_lama = x0
    for r in range(1, maks_iterasi + 1):
        x_baru = g(x_lama)
        selisih = abs(x_baru - x_lama)
        print(f"Iterasi {r:2d}: x = {x_baru:.6f}, selisih = {selisih:.6f}")
        if selisih < toleransi:
            print(f"-> Konvergen di iterasi ke-{r}, Akar = {x_baru:.6f}\n")
            break
        x_lama = x_baru
else:
    print("Status: Divergen, hentikan iterasi.\n")

# 2. METODE NEWTON-RAPHSON
print(">>> METODE NEWTON-RAPHSON:")
print(f"Cek turunan: f'({x0}) = {f_turunan(x0):.6f} != 0 (Aman)\n")
x_lama = x0
for r in range(1, maks_iterasi + 1):
    turunan = f_turunan(x_lama)
    x_baru = x_lama - (f(x_lama) / turunan)
    selisih = abs(x_baru - x_lama)
    print(f"Iterasi {r:2d}: x = {x_baru:.6f}, selisih = {selisih:.6f}")
    if selisih < toleransi:
        print(f"-> Konvergen di iterasi ke-{r}, Akar = {x_baru:.6f}\n")
        break
    x_lama = x_baru