from scripts.options import options
from math import sqrt
x_scale = options.x_scale
y_scale = options.y_scale

class pose_result:
    def __init__(self,x,y):
        self.x = x*x_scale
        self.y = y*y_scale

def output_handle_info(output_handle_info_path = options.output_result_info_path):
    result = dict()
    info_file = open(output_handle_info_path,'r')
    
    for line in info_file:
        info = line.split(" - ")
        body_num = int(info[0])
        body_name = info[1].rstrip('\n')
        result[body_name] = body_num

    info_file.close()

    return result

body_part_idx = output_handle_info()


def get_body_location(detection_result, body_name: str):
    body_idx = body_part_idx[body_name]
    x_result = detection_result.pose_landmarks[0][body_idx].x
    y_result = detection_result.pose_landmarks[0][body_idx].y
    return pose_result(x_result, y_result)
    
    
def get_leg_length(detection_result):
    r_ankle = get_body_location(detection_result, "right ankle")
    r_knee = get_body_location(detection_result, "right knee")
    r_hip = get_body_location(detection_result, "right hip")
    l1 = sqrt((r_ankle.x-r_knee.x)**2+(r_ankle.y-r_knee.y)**2)
    l2 = sqrt((r_knee.x-r_hip.x)**2+(r_knee.y-r_hip.y)**2)
    right_leg = l1+l2

    l_ankle = get_body_location(detection_result, "left ankle")
    l_knee = get_body_location(detection_result, "left knee")
    l_hip = get_body_location(detection_result, "left hip")
    l1 = sqrt((l_ankle.x-l_knee.x)**2+(l_ankle.y-l_knee.y)**2)
    l2 = sqrt((l_knee.x-l_hip.x)**2+(l_knee.y-l_hip.y)**2)
    left_leg = l1+l2

    return (right_leg + left_leg)/2


def get_arm_length(detection_result):
    r_shoulder = get_body_location(detection_result, "right shoulder")
    r_elbow = get_body_location(detection_result, "right elbow")
    r_wrist = get_body_location(detection_result, "right wrist")
    l1 = sqrt((r_shoulder.x-r_elbow.x)**2+(r_shoulder.y-r_elbow.y)**2)
    l2 = sqrt((r_elbow.x-r_wrist.x)**2+(r_elbow.y-r_wrist.y)**2)
    right_arm = l1+l2

    l_shoulder = get_body_location(detection_result, "left shoulder")
    l_elbow = get_body_location(detection_result, "left elbow")
    l_wrist = get_body_location(detection_result, "left wrist")
    l1 = sqrt((l_shoulder.x-l_elbow.x)**2+(l_shoulder.y-l_elbow.y)**2)
    l2 = sqrt((l_elbow.x-l_wrist.x)**2+(l_elbow.y-l_wrist.y)**2)
    left_arm = l1+l2

    return (right_arm + left_arm)/2


def get_sholder_width(detection_result):
    r_shoulder = get_body_location(detection_result, "right shoulder")
    l_shoulder = get_body_location(detection_result, "left shoulder")
    x_differ = r_shoulder.x-l_shoulder.x
    y_differ = r_shoulder.y-l_shoulder.y
    return sqrt(x_differ**2 + y_differ**2)


def get_hip_width(detection_result):
    r_hip = get_body_location(detection_result, "right hip")
    l_hip = get_body_location(detection_result, "left hip")
    x_differ = r_hip.x-l_hip.x
    y_differ = r_hip.y-l_hip.y
    return sqrt(x_differ**2+y_differ**2)


def get_upper_body_height(detection_result):
    r_shoulder = get_body_location(detection_result, "right shoulder")
    r_hip = get_body_location(detection_result, "right hip")
    r_height = sqrt((r_hip.x-r_shoulder.x)**2+(r_hip.y-r_shoulder.y)**2)

    l_shoulder = get_body_location(detection_result, "left shoulder")
    l_hip = get_body_location(detection_result, "left hip")
    l_height = sqrt((l_hip.x-l_shoulder.x)**2+(l_hip.y-l_shoulder.y)**2)

    return (r_height+l_height)/2


def get_measurement(detection_result):
    result = dict()
    result["arm length"] = get_arm_length(detection_result)
    result["leg length"] = get_leg_length(detection_result)
    result["sholder width"] = get_sholder_width(detection_result)
    result["hip width"] = get_hip_width(detection_result)
    result["upper body height"] = get_upper_body_height(detection_result)
    return result
    