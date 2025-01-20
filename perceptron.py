# The bias must always be set to 1.
# x & w must have the same length
def compute_output(w, x):
    z = 0.0
    for i in range(len(w)):
        z += x[i] * w[i] # Compute the weighed input
    if z < 0:
        return -1
    else:
        return 1
    
# Define weights (These actually define a NAND gate!)
w = [0.9, -0.6, -0.5]
