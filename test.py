from utils import image_process
import cv2
from scripts.options import options

if __name__ == "__main__":
    
    image_process.read_corr_save_image()
    

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
