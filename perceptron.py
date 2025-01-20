import random

def show_learning(w):
    print("w0 = {:5.2f}, w1 = {:5.2f}, w2 = {:5.2f}".format(w[0], w[1], w[2]))

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

random.seed(7) # Keep things repeatable
LEARNING_RATE = 0.1
index_list = [0, 1, 2, 3]

# Training data for a NAND gate perceptron
x_train = [(1.0, -1.0, -1.0), (1.0, -1.0, 1.0), (1.0, 1.0, -1.0), (1.0, 1.0, 1.0)]
y_train = [1.0, 1.0, 1.0, -1.0]

# "Random" starter weights
w = [0.2, -0.6, 0.25]

# Training loop
learning_complete = False
while not learning_complete:
    learning_complete = True
    random.shuffle(index_list)
    for i in index_list:
        x = x_train[i]
        y = y_train[i]
        y_actual = compute_output(w, x)

        if y != y_actual:
            for j in range(0, len(w)):
                w[j] += (y * LEARNING_RATE * x[j])  # Note: y is either 1.0 or -1.0, so will adjust this to add/subtrac as required without an extra if statement
            learning_complete = False
            show_learning(w)