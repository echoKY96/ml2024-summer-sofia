import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

N = int(input("Enter the number of training samples (N): "))
print("Provide the training set pairs (x, y) one by one.")
train_x = np.zeros(N, dtype=float)
train_y = np.zeros(N, dtype=int)
for i in range(N):
    train_x[i] = float(input(f"Enter x for pair {i + 1}: "))
    train_y[i] = int(input(f"Enter y for pair {i + 1}: "))

train_x = train_x.reshape(-1, 1)

M = int(input("\nEnter the number of test samples (M): "))
print("Provide the test set pairs (x, y) one by one.")
test_x = np.zeros(M, dtype=float)
test_y = np.zeros(M, dtype=int)
for i in range(M):
    test_x[i] = float(input(f"Enter x for pair {i + 1}: "))
    test_y[i] = int(input(f"Enter y for pair {i + 1}: "))

test_x = test_x.reshape(-1, 1)

best_k = None
best_accuracy = 0

max_k = min(10, M)
print(f"\nEvaluating kNN for k in range 1 to {max_k}...")
for k in range(1, max_k + 1):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_x, train_y)
    predictions = knn.predict(test_x)
    accuracy = accuracy_score(test_y, predictions)
    print(f"k = {k}, Accuracy = {accuracy:.2f}")
    
    if accuracy > best_accuracy:
        best_k = k
        best_accuracy = accuracy

print(f"\nBest k: {best_k}")
print(f"Test Accuracy with k = {best_k}: {best_accuracy:.2f}")
