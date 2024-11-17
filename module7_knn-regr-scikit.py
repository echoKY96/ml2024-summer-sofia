import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    try:
        N = int(input("Enter the number of data points (N, positive integer): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")
        
        k = int(input("Enter the number of neighbors (k, positive integer): "))
        if k <= 0:
            raise ValueError("k must be a positive integer.")
        
        if k > N:
            raise ValueError("k must be less than or equal to the number of data points (N).")
        
        data_points = np.zeros(N)
        target_values = np.zeros(N)
        
        print(f"Please enter {N} points (x, y):")
        for i in range(N):
            x = float(input(f"Enter x value for point {i + 1}: "))
            y = float(input(f"Enter y value for point {i + 1}: "))
            data_points[i] = x
            target_values[i] = y

        # Reshape data for the model
        data_points = data_points.reshape(-1, 1)
        
        # Use Scikit-learn's KNeighborsRegressor
        model = KNeighborsRegressor(n_neighbors=k, metric='manhattan')
        model.fit(data_points, target_values)

        x_predict = float(input("Enter the x value for prediction: "))
        predicted_y = model.predict(np.array([[x_predict]]))[0]
        print(f"The predicted Y value for X = {x_predict} is: {predicted_y}")

        variance = np.var(target_values)
        print(f"Variance of the target values: {variance}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
