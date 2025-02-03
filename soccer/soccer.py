import cv2
import torch
from yolov5.models.common import Detect
# from yolov5.utils.datasets import LoadImages
from yolov5.utils.general import non_max_suppression, scale_coords
from yolov5.utils.torch_utils import select_device

# Load the pre-trained YOLO model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='path_to_yolov5_weights.pt')

# Load the image
image = cv2.imread('path_to_your_image.jpg')

# Perform object detection
results = model(image)

# Display the results
results.print()  # Print results to the console
results.show()   # Display results in a new window
results.save()   # Save results to an image file
