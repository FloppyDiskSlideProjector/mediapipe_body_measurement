import matplotlib.pyplot as plt
import numpy as np

def plot_points(detection_result, x_length = 100, y_length = 100):
    image = np.zeros((x_length, y_length, 3))
    for count, landmark in enumerate(detection_result.pose_landmarks[0]):
        x,y = landmark.x, landmark.y
        x = int(x*x_length)
        y = int(y*y_length)
        image[y,x] = [1, 1, 1]
        
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.imshow(image)
    plt.show()