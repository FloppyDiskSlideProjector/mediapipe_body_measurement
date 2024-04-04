import mediapipe as mp
from scripts.options import options
import numpy as np
import cv2


def get_image(image_path = options.image_path):
    return mp.Image.create_from_file(image_path)
    

def chess_board_corners(image,gray,r):
	square_size=int(r+1)
	ret, corners = cv2.findChessboardCorners(gray, (options.rectangle_row,options.rectangle_col),None)
	corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),options.criteria)
	# Uncomment for old opencv version
	corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), options.criteria)
	coordinates=[]
	coordinates.append((corners2[0,0,0],corners2[0,0,1]))
	coordinates.append((corners2[square_size-1,0,0],corners2[square_size-1,0,1]))
	coordinates.append((corners2[options.rectangle_row*(square_size-1),0,0],corners2[options.rectangle_row*(square_size-1),0,1]))
	coordinates.append((corners2[options.rectangle_row*(square_size-1)+square_size-1,0,0],corners2[options.rectangle_row*(square_size-1)+square_size-1,0,1]))
	return coordinates


def image_filter(image):
	filtered_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	
	filtered_image = cv2.GaussianBlur(filtered_image, (5,5), 0)

	return filtered_image
	


def analyze_chessboard(image):
	
	gray=image_filter(image)

	refPt=chess_board_corners(image,gray,options.affine_correction_r1)
	pt1=np.asarray(refPt,dtype=np.float32)
	dist=(refPt[1][0]-refPt[0][0])
	refPt[1]=(refPt[0][0]+dist,refPt[0][1])
	refPt[2]=(refPt[0][0],refPt[0][1]+dist)
	refPt[3]=(refPt[0][0]+dist,refPt[0][1]+dist)
	pt2=np.asarray(refPt,dtype=np.float32)
	M=cv2.getPerspectiveTransform(pt1,pt2)
	return M

    
def image_correction(image): # cv image
	chess_bord_img = cv2.imread(options.chess_board_img_path)
	affine_correct_params = analyze_chessboard(chess_bord_img)

	image2 = np.copy(image)

	if(len(image2)<3):
		image2=cv2.cvtColor(image2,cv2.COLOR_GRAY2RGB)
	
	dst=cv2.warpPerspective(image2,affine_correct_params,(image.shape[1],image.shape[0]))
	return dst