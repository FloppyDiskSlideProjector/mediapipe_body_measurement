from utils.detector import get_detector
from utils.image_process import get_mp_image, prepare_img_corr_param, read_corr_save_image
from utils.handle_result import get_measurement
from utils.drawing_tool import plot_points
import cv2
from scripts.options import options

if __name__ == "__main__":
    
    prepare_img_corr_param()
    

    """
    image = cv2.imread(options.chess_board_img_path)

    
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    ret, corners = cv2.findChessboardCorners(gray, (options.rectangle_row,options.rectangle_col),None)
    print(corners)
    print()
    print(type(corners))
    corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), options.criteria)
    #cv2.imwrite("temp.jpg", gray)
    #blurred_image = cv2.GaussianBlur(gray, (5,5), 0)
    #cv2.imwrite("temp2.jpg", blurred_image)
    """
