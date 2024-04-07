from utils.detector import get_detector
from utils.image_process import get_mp_image, prepare_img_corr_param, read_corr_save_image
from utils.handle_result import get_measurement
from utils.drawing_tool import plot_points

from argparse import ArgumentParser

def measure():
    read_corr_save_image()

    detector = get_detector()
    mp_image = get_mp_image()
    
    detection_result = detector.detect(mp_image)
    measurement = get_measurement(detection_result)
    
    plot_points(detection_result = detection_result)
    
    print(measurement)


def get_args():
    args = ArgumentParser()
    args.add_argument("--action", type=str, help = "action to do", default="measure")
    return args.parse_args()


def update_env():
    prepare_img_corr_param()
    
    # update x,y scale? maybe need actual photo


if __name__ == "__main__":
    args = get_args()
    if args.action == "measure":
        measure()
    if args.action == "update_environment":
        update_env()
    