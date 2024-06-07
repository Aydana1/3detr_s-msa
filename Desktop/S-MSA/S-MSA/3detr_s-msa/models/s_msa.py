import math
import numpy as np

def weighted_inverse_distance(nearest_points, query_points, power):
    # Calculate the distances between the query point and each of the three points
    dist1 = np.linalg.norm(query_points[:] - nearest_points[0, :], axis=1, keepdims=True)
    dist2 = np.linalg.norm(query_points[:]  - nearest_points[1, :], axis=1, keepdims=True)
    dist3 = np.linalg.norm(query_points[:]  - nearest_points[2, :], axis=1, keepdims=True)

    epsilon=1e-8
    #print(np.min(dist1))
    #print(np.where(dist1 == 0)[0])
    indices = np.where(dist1 == 0)[0]
    if np.min(dist1) < epsilon:
        # Handle division by zero by returning the value at the closest point
        # print("index: ", np.argmin(dist1))
        min_v = nearest_points[0, indices, 0] # min val 
        dist1[indices, 0] = min_v
        #print("dist1 ", dist1.shape)
    
    indices = np.where(dist2 == 0)[0]
    if np.min(dist2) < epsilon:
        min_v = nearest_points[0, indices, 0]
        dist2 = min_v
        #print("dist2 ", dist2.shape)
    
    indices = np.where(dist3 == 0)[0]
    if np.min(dist3) < epsilon:
        min_v = nearest_points[0, indices, 0]
        dist3 = min_v
        #print("dist3 ", dist3.shape)

    #print(dist1.shape)
    w1 = 1 / (dist1**power)
    w2 = 1 / (dist2**power)
    w3 = 1 / (dist3**power)
    # Calculate the weights for each point using the inverse of the distance raised to the power
    # Normalize the weights so that they sum to one
    w_sum = w1 + w2 + w3
    w1_norm = w1 / w_sum
    w2_norm = w2 / w_sum
    w3_norm = w3 / w_sum

    # Calculate the interpolated value as the weighted sum of the values at each point
    value = w1_norm * nearest_points[0, :] + w2_norm * nearest_points[1, :] + w3_norm * nearest_points[2, :]
    #print("value: ", value.shape)

    return value
