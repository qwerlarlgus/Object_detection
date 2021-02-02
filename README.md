# Object_detection

### Kaggle:  https://www.kaggle.com/ultralytics/yolov5-ultralytics - COCO 128 small

### cvat: https://cvat.org/

### roboflow: https://app.roboflow.com/dataset/coco-128-small-yzqm6

How to Train YOLOv4-tiny
If you want to train an object detector that is lightning fast and can be deployed on edge devices, then you can train it on YOLOv4-tiny. We have written a nice guide here on how to train and deploy YOLOv4-tiny on your custom data to detect your custom objects.

Note: YOLOv4-tiny is implemented in the Darknet framework, not PyTorch.

How to Train YOLOv4-CSP/P5/P6/P7
If you want to use a medium sized model, you'll want to use YOLOv4-CSP, and this can be a good place to start iterating on the Scaled-YOLOv4 models.

If you want to scale up from there for ultimate accuracy, the YOLOv4-P5/P6/P7 models will be of use.

Here is the Scaled-YOLOv4 repo, though you will notice that WongKinYiu has provided it there predominantly for research replication purposes and there are not many instructions for training on your own dataset. To train on your own data, our guide on training YOLOv5 in PyTorch on custom data will be useful, as it is a very similar training procedure.
