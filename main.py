from src.detector import get_detector
from utils.image_process import get_image
from utils.handle_result import get_measurement
from utils.drawing_tool import plot_points


if __name__ == "__main__":
    detector = get_detector()
    
    image = get_image()
    
    # image correction(maybe optional)
    
    detection_result = detector.detect(image)
        
    measurement = get_measurement(detection_result)
    
    plot_points(detection_result = detection_result)
    
    print(measurement)