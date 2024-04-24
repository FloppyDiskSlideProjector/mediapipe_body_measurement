import os
import cv2
class Options:
    def __init__(self):
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    model_name = "pose_landmarker_heavy.task"
    image_path = os.path.join("data","image","sample.jpg")
    
    # scale
    # realife life measurement required
    x_scale = 1 # temporary value
    y_scale = 1 # temporary value

    affine_correction_r1 = 5
    rectangle_row = 7
    rectangle_col = 9
    
    chess_board_img_path = os.path.join("data","resource","chess_bord.jpeg")


    corr_param_path = os.path.join("scripts","corr_param.npy")
    corrected_image_path = os.path.join("data","image","corrected_image.jpeg")

    output_result_info_path = os.path.join("data","resource","output_handle_info.txt")

options = Options()