import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([3,5,7,9,11])
n = len(x)

w = 0.0
b = 0.0
learning_rate = 0.01
epochs = 10000000

for epoch in range(epochs):
    y_pre = w*x + b
    loss = np.mean((y-y_pre)**2)
    dw = (-2/n) * np.sum(x * (y-y_pre))
    db = (-2/n) * np.sum((y-y_pre))
    w -= learning_rate * dw
    b -= learning_rate * db
    print(f'epoch: {epoch}, loss: {loss}, w: {w}, b: {b}')