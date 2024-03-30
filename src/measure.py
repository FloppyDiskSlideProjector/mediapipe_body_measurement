import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


import os


import matplotlib.pyplot as plt
import numpy as np

model_name = "pose_landmarker_heavy.task"

if __name__ == "__main__":
    # get detector
    model_path = os.path.join("model", model_name)
    base_options = python.BaseOptions(model_asset_path = model_path)
    options = vision.PoseLandmarkerOptions(base_options = base_options,
        running_mode=mp.tasks.vision.RunningMode.IMAGE)
    detector = vision.PoseLandmarker.create_from_options(options)
    
    # get image
    image = mp.Image.create_from_file(os.path.join("image","jdragon.jpg"))
    
    # image correction(maybe optional)
    # maybe use open cv Camera Calibration?
    # https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html
    
    # detect
    detection_result = detector.detect(image)
    
    # scale
    # realife life measurement required
    x_scale = 1 # temporary value
    y_scale = 1 # temporary value
    
    # result
    for count, landmark in enumerate(detection_result.pose_landmarks[0]):
        print(count, " ", landmark.x, " ",landmark.y)
        
        
    print('\n')
    right_sholder = detection_result.pose_landmarks[0][12]
    left_sholder = detection_result.pose_landmarks[0][11]
    
    left_hip = detection_result.pose_landmarks[0][23]
    right_hip = detection_result.pose_landmarks[0][24]
    
    left_heel = detection_result.pose_landmarks[0][29]
    right_heel = detection_result.pose_landmarks[0][30]
    left_foot = detection_result.pose_landmarks[0][31]
    right_foot = detection_result.pose_landmarks[0][32]
    
    base_height = (left_heel.y + right_heel.y + left_foot.y + right_foot.y)/4
    
    sholder_width = (left_sholder.x - right_sholder.x)*x_scale
    sholder_height = ((left_sholder.y + right_sholder.y)/2 - base_height)*y_scale
    hip_width = (left_hip.x-right_hip.x)*x_scale
    leg_length = ((left_hip.y-right_hip.y)/2-base_height)*y_scale
    print("sholder_width: ", sholder_width)
    print("sholder_height: ", sholder_height)
    print("hip_width: ", hip_width)
    print("leg_length: ", leg_length)
    
    
    image = np.zeros((100, 100, 3))
    for landmark in detection_result.pose_landmarks[0]:
        x,y = landmark.x, landmark.y
        x = int(x*100)
        y = int(y*100)
        image[y,x] = [1, 1, 1]
        
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.imshow(image)
    plt.show()
        