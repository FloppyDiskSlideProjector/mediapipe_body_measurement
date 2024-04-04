import os
import cv2
class options:
    model_name = "pose_landmarker_heavy.task"
    image_path = os.path.join("data","image","sample.jpg")
    
    # scale
    # realife life measurement required
    x_scale = 1 # temporary value
    y_scale = 1 # temporary value

    affine_correction_r1 = 5
    rectangle_row = 7
    rectangle_col = 9
    
    chess_board_img_path = os.path.join("data","normalization","chess_bord.jpeg")

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)