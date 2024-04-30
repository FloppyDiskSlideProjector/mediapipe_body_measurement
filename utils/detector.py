import mediapipe as mp
from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python import vision
import os

from scripts.options import options
from utils.image_process import image_correction

def get_detector(model_name = options.model_name):
    model_path = os.path.join("model", model_name)
    base_options = BaseOptions(model_asset_path = model_path)
    options = vision.PoseLandmarkerOptions(base_options = base_options,
        running_mode=mp.tasks.vision.RunningMode.IMAGE)
    detector = vision.PoseLandmarker.create_from_options(options)
    return detector


def pose_detect_check(detection_result):
    if len(detection_result.pose_landmarks) == 0:
        raise(ValueError("pose have not detected"))
    
