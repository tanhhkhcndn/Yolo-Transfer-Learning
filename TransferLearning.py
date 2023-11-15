from ultralytics import YOLO
import ultralytics
import torch
print(torch.cuda.is_available())
ultralytics.checks()

# training
# model = YOLO('yolov8n.pt')
# if __name__ == '__main__':
#     results = model.train(data='G:\\Code4Paper\\2023\\Yolo-Transfer-Learning\\Dataset\\hamster\\data.yaml', epochs=50, batch=8, device = 0)
#     results = model.val()


# testing
 
# Load our custom goat model
model = YOLO("runs/detect/train/weights/best.pt")
 
# Use the model to detect object - goat
model.predict(source="hamster.jpg", save=False, show=True)


# 
# results = model("testImage.jpg")  # return a list of Results objects
# results= model.predict('testImage.jpg', show=False, save=True, imgsz=320, conf=0.5)
# print(len(model.names))
# input("Press Enter to continue...")
# Process results list
# for result in results:
#     boxes = result.boxes  # Boxes object for bbox outputs
#     masks = result.masks  # Masks object for segmentation masks outputs
#     keypoints = result.keypoints  # Keypoints object for pose outputs
#     probs = result.probs  # Probs object for classification outputs
#     print(boxes)
#     print(masks)
#     print(probs)