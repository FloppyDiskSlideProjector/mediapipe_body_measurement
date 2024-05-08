import os
import cv2
class Options:
    def __init__(self):
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        self.update_xy_scale()

    
    def update_xy_scale(self):
        file = open(self.xy_scale_path)
        x,y = file.read().split('\n')
        x = float(x.split(' ')[1])
        y = float(y.split(' ')[1])
        self.x_scale = x
        self.y_scale = y


    model_name = "pose_landmarker_heavy.task"
    image_path = os.path.join("data","image","sample.jpg")
    
    # scale
    # realife life measurement required

    affine_correction_r1 = 6
    rectangle_row = 7
    rectangle_col = 9
    
    chess_board_img_path = os.path.join("data","resource","chess_bord.jpeg")


    corr_param_path = os.path.join("scripts","corr_param.npy")
    corrected_image_path = os.path.join("data","image","corrected_image.jpeg")

    output_result_info_path = os.path.join("data","resource","output_handle_info.txt")
    
    real_world_width = 16
    real_world_height = 16

    xy_scale_path = os.path.join("data","resource","xy_scale.txt")

    # when the distance between camera and person is 2.4m
    # this value could be vary
    # depends on the environment
    real_life_x_scale = 1.24062972
    real_life_y_scale = 1.24062972


options = Options()
