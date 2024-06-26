import mediapipe as mp
from scripts.options import options
import numpy as np
import cv2


import matplotlib.pyplot as plt


def get_mp_image(image_path = options.corrected_image_path):
    return mp.Image.create_from_file(image_path)
    

def chess_board_corners(image,r,mode = "pixel"):
	square_size=int(r+1)
	ret, corners = cv2.findChessboardCorners(image, (options.rectangle_row,options.rectangle_col),None)
	if ret == False:
		raise ValueError("Corner not found\nrecomendation1: modify image_filter(image)\nrecomendation2: use another image")
	corners2 = cv2.cornerSubPix(image,corners,(11,11),(-1,-1),options.criteria)

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
	

def corr_param_from_chessboard(image):
	
	gray=image_filter(image)

	refPt=chess_board_corners(gray,options.affine_correction_r1)
	pt1=np.asarray(refPt,dtype=np.float32)
	dist=(refPt[1][0]-refPt[0][0])
	refPt[1]=(refPt[0][0]+dist,refPt[0][1])
	refPt[2]=(refPt[0][0],refPt[0][1]+dist)
	refPt[3]=(refPt[0][0]+dist,refPt[0][1]+dist)
	pt2=np.asarray(refPt,dtype=np.float32)
	M=cv2.getPerspectiveTransform(pt1,pt2)
	return M


def prepare_img_corr_param():
	chess_bord_img = cv2.imread(options.chess_board_img_path)
	affine_correct_params = corr_param_from_chessboard(chess_bord_img)
	np.save(options.corr_param_path,affine_correct_params)

    
def image_correction(image): # cv image
	affine_correct_params = np.load(options.corr_param_path)
	image2 = np.copy(image)
	# if(len(image2)<3):
	# 	image2=cv2.cvtColor(image2,cv2.COLOR_GRAY2RGB)
	dst=cv2.warpPerspective(image2,affine_correct_params,(image.shape[1],image.shape[0]))
	return dst


def read_corr_save_image(input_img_path, output_img_path):
	image = cv2.imread(input_img_path)
	image = image_correction(image)
	image = cv2.imwrite(output_img_path,image)


def update_img_scale(chess_bord_img_path = options.chess_board_img_path):
    #prepare_image
	image = cv2.imread(chess_bord_img_path)
	corrected_image = image_correction(image)
	gray=image_filter(corrected_image)

	#find corner
	corners=chess_board_corners(gray,options.affine_correction_r1)

	#calculate xy scale
	img_height = image.shape[0]
	img_width = image.shape[1]
	corner_height = (corners[2][1]+corners[3][1])/2 - (corners[0][1]+corners[1][1])/2
	corner_width = (corners[1][0]+corners[3][0])/2 - (corners[0][0]+corners[2][0])/2
	
	new_x_scale = options.real_world_width*img_width/corner_width
	new_y_scale = options.real_world_height*img_width/corner_height
	
	new_x_scale = new_x_scale*options.real_life_x_scale
	new_y_scale = new_y_scale*options.real_life_y_scale

	file = open(options.xy_scale_path,'w')
	file.write("x " + str(new_x_scale)+'\n')
	file.write("y " + str(new_y_scale))
	file.close()

	#update options
	options.update_xy_scale()
	
	
