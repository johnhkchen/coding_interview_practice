# Pattern from experimentation:
# Top: Paths increased N-fold from previous lattice size, Bottom: Lattice size
# 6/2, 10/3, 14/4, 18/5, 22/6, 26/7, 30/8, 34/9
# 2x2,  3x3,  4x4,  5x5,  6x6,  7x7,  8x8,  9x9
# Closed form:
# L(i) = L(i-1) * (4i - 2) / i

def paths(n):
        if n == 2:
                return 6
        return int(paths(n-1) * (4*n - 2) / n);

print("There are {} paths for a 20x20 lattice.".format(paths(20)))