import mediapipe as mp
from scripts.options import options


def get_image(image_path = options.image_path):
    return mp.Image.create_from_file(image_path)
    
    
def image_correction():
    # image correction(maybe optional)
    # maybe use open cv Camera Calibration?
    # https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html
    None