import numpy as np
from sklearn.metrics import precision_score, recall_score

N = int(input("Enter the number of points (N): "))

X = np.zeros(N)
Y = np.zeros(N)

print("Enter the points (x, y) one by one:")
for i in range(N):
    while True:
        x_value = int(input(f"Enter x value for point {i+1} (0 or 1): "))
        if x_value == 0 or x_value == 1:
            X[i] = x_value
            break
        else:
            raise ValueError("Invalid input! x value must be 0 or 1.")
    
    while True:
        y_value = int(input(f"Enter y value for point {i+1} (0 or 1): "))
        if y_value == 0 or y_value == 1:
            Y[i] = y_value
            break
        else:
            raise ValueError("Invalid input! y value must be 0 or 1.")

precision = precision_score(X, Y, average='binary')
recall = recall_score(X, Y, average='binary')

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
