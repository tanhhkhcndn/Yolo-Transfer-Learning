# Yolo-Transfer-Learning
Yolo Transfer Learning
https://link.springer.com/article/10.1007/s11554-022-01227-x
https://www.freecodecamp.org/news/how-to-detect-objects-in-images-using-yolov8/
https://learnopencv.com/train-yolov8-on-custom-dataset/
https://stackoverflow.com/questions/75324341/yolov8-get-predicted-bounding-box

https://thinkinfi.com/train-yolov8-on-custom-dataset-in-windows-gpu/
1. Fine-tuning YOLOv8
https://blog.paperspace.com/yolov8/
https://medium.com/@yongsun.yoon/fine-tuning-yolov8-using-custom-dataset-generated-by-open-world-object-detector-5724e267645d
2. Description
 https://blog.paperspace.com/yolov8/
 https://www.makeuseof.com/yolov8-how-train-custom-data/
 https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb#scrollTo=3C3EO_2zNChu
 https://learnopencv.com/ultralytics-yolov8/

3. Yolo 5
 https://docs.ultralytics.com/yolov5/tutorials/transfer_learning_with_frozen_layers/
 https://cv.gluon.ai/build/examples_detection/skip_fintune.html

4. Video
https://github.com/ultralytics/ultralytics/issues/375

5. Error fix
alexschimel 
I have experienced the same error. My added feedback:

    I tried both classify and detect tasks, and in both cases trying CPU and GPU (device=0). The error ONLY occurs in the classify task when using the GPU.
    Setting workers=0 did fix the issue. Did not notice the training to be slow, but then I am using very small datasets for debugging.
    Setting val=False did NOT fix the issue.
    Found this relevant thread on stackoverflow: https://stackoverflow.com/questions/75111196/yolov8-runtimeerror-an-attempt-has-been-made-to-start-a-new-process-before-th
    @glenn-jocher's answers are 100% obvious generic ChatGPT answers, are absolutely not helpful, and are making the process of looking online for a solution to a frustrating problem an even more frustrating experience. Can you please quit that?

My specs:

    Windows 10
    GPU: NVIDIA GeForce RTX 2070 with Max-Q Design (driver version 537.13)
    Cuda release 12.2, V12.2.140
    starting with a conda env, and installed pytorch first, then ultralytics in it with pip
    pytorch 2.1.0+cu121
    ultralytics 8.0.196
