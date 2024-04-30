from utils.detector import get_detector, pose_detect_check
from utils.image_process import get_mp_image, prepare_img_corr_param, read_corr_save_image, update_img_scale
from utils.handle_result import get_measurement
from utils.drawing_tool import plot_points
from scripts.options import options

from argparse import ArgumentParser

def measure():
    read_corr_save_image(input_img_path = options.image_path, output_img_path=options.corrected_image_path)

    mp_image = get_mp_image()
    detector = get_detector()

    detection_result = detector.detect(mp_image)
    pose_detect_check(detection_result)
    measurement = get_measurement(detection_result)
    
    plot_points(detection_result = detection_result)
    
    print(measurement)


def get_args():
    args = ArgumentParser()
    args.add_argument("--action", type=str, help = "action to do", default="measure")
    return args.parse_args()


def update_env():
    prepare_img_corr_param()
    
    update_img_scale()


if __name__ == "__main__":
    args = get_args()
    if args.action == "measure":
        measure()
    if args.action == "update_environment":
        update_env()
    