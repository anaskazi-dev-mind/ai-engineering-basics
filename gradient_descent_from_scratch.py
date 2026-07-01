import numpy as np
import matplotlib.pyplot as plt 

def run_gradient_descent(learning_rate, epochs=50):
    x = 4.0
    y = 3.0
    loss_history = []

    for i in range(epochs):
        current_loss = (x**2) + (y**2)
        loss_history.append(current_loss)


        grad_x = 2 * x
        grad_y = 2 * y


        x = x - (learning_rate * grad_x)
        y = y - (learning_rate * grad_y)

    return loss_history

loss_slow = run_gradient_descent(0.001)
loss_perfect = run_gradient_descent(0.1)
loss_fast = run_gradient_descent(1.05)


plt.figure(figsize=(10, 6)) # Graph ki size tay karna

# plt.plot() x-axis par automatically epochs (0 to 50) lega aur y-axis par humari loss_history
plt.plot(loss_slow, label='LR = 0.001 (Slow/Underfit)', color='blue')
plt.plot(loss_perfect, label='LR = 0.1 (Perfect/Converged)', color='green')
plt.plot(loss_fast, label='LR = 1.05 (Exploding/Diverged)', color='red')

# Graph ko sundar aur samajhne laayak banana
plt.title('Loss Landscape: How Learning Rate affects AI')
plt.xlabel('Epochs (Number of Steps)')
plt.ylabel('Loss (Error)')
plt.ylim(0, 30) # Hum y-axis ki limit set kar rahe hain taaki graph saaf dikhe
plt.legend() # Yeh batata hai ki kaunsi line kis LR ki hai
plt.grid(True) # Background mein dabbe (grid) banana
plt.show() # Graph ko screen par dikhana