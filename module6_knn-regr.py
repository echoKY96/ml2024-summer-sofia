import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.data_points = None
        self.target_values = None

    def fit(self, data_points, target_values):
        self.data_points = np.array(data_points)
        self.target_values = np.array(target_values)

    def predict(self, x):
        if self.k > len(self.target_values):
            raise ValueError("k must be less than or equal to the number of data points (N).")

        distances = np.linalg.norm(self.data_points - np.array([x]), axis=1)
        k_nearest_indices = np.argsort(distances)[:self.k]
        k_nearest_targets = self.target_values[k_nearest_indices]
        return np.mean(k_nearest_targets)

def main():
    try:
        N = int(input("Enter the number of data points (N, positive integer): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")
        
        k = int(input("Enter the number of neighbors (k, positive integer): "))
        if k <= 0:
            raise ValueError("k must be a positive integer.")
        
        data_points = []
        target_values = []
        
        print(f"Please enter {N} points (x, y):")
        for i in range(N):
            x = float(input(f"Enter x value for point {i + 1}: "))
            y = float(input(f"Enter y value for point {i + 1}: "))
            data_points.append((x, y))
            target_values.append(y)

        model = KNNRegressor(k)
        model.fit(data_points, target_values)

        x_predict = float(input("Enter the x value for prediction: "))
        predicted_y = model.predict(x_predict)
        print(f"The predicted Y value for X = {x_predict} is: {predicted_y}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
