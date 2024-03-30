from scripts.options import options
x_scale = options.x_scale
y_scale = options.y_scale

def get_foot_height(detection_result):
    left_heel = detection_result.pose_landmarks[0][29]
    right_heel = detection_result.pose_landmarks[0][30]
    left_foot = detection_result.pose_landmarks[0][31]
    right_foot = detection_result.pose_landmarks[0][32]
    return (left_heel.y + right_heel.y + left_foot.y + right_foot.y)/4*y_scale


def get_sholder_width(detection_result):
    right_sholder = detection_result.pose_landmarks[0][12]
    left_sholder = detection_result.pose_landmarks[0][11]
    return (left_sholder.x - right_sholder.x)*x_scale
    
    
def get_sholder_height(detection_result):
    right_sholder = detection_result.pose_landmarks[0][12]
    left_sholder = detection_result.pose_landmarks[0][11]
    foot_height = get_foot_height(detection_result)
    return foot_height-(left_sholder.y + right_sholder.y)/2*y_scale
    
    
def get_hip_width(detection_result):
    left_hip = detection_result.pose_landmarks[0][23]
    right_hip = detection_result.pose_landmarks[0][24]
    return (left_hip.x-right_hip.x)*x_scale
    
    
def get_leg_length(detection_result):
    foot_height = get_foot_height(detection_result)
    left_hip = detection_result.pose_landmarks[0][23]
    right_hip = detection_result.pose_landmarks[0][24]
    return foot_height-(left_hip.y+right_hip.y)/2*y_scale


def get_measurement(detection_result):
    result = dict()
    result["sholder_width"] = get_sholder_width(detection_result)
    result["sholder_height"] = get_sholder_height(detection_result)
    result["hip_width"] = get_hip_width(detection_result)
    result["leg_length"] = get_leg_length(detection_result)
    return result
    