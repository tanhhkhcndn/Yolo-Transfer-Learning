from ultralytics import YOLO

model = YOLO('yolov8n.pt')
# 
# results = model("testImage.jpg")  # return a list of Results objects
results= model.predict('testImage.jpg', show=True, save=True, imgsz=320, conf=0.5)
input("Press Enter to continue...")
# Process results list
# for result in results:
#     boxes = result.boxes  # Boxes object for bbox outputs
#     masks = result.masks  # Masks object for segmentation masks outputs
#     keypoints = result.keypoints  # Keypoints object for pose outputs
#     probs = result.probs  # Probs object for classification outputs
#     print(boxes)
#     print(masks)
#     print(probs)