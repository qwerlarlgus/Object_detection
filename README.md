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


### Yolov5

# Re-clone repo
%cd ..
%rm -rf yolov5 && git clone https://github.com/ultralytics/yolov5
%cd yolov5

# Test all
%%shell
for x in s m l x; do
  python test.py --weights yolov5$x.pt --data coco.yaml --img 640
done

# Unit tests
%%shell
export PYTHONPATH="$PWD"  # to run *.py. files in subdirectories

rm -rf runs  # remove runs/
for m in yolov5s; do  # models
  python train.py --weights $m.pt --epochs 3 --img 320 --device 0  # train pretrained
  python train.py --weights '' --cfg $m.yaml --epochs 3 --img 320 --device 0  # train scratch
  for d in 0 cpu; do  # devices
    python detect.py --weights $m.pt --device $d  # detect official
    python detect.py --weights runs/train/exp/weights/best.pt --device $d  # detect custom
    python test.py --weights $m.pt --device $d # test official
    python test.py --weights runs/train/exp/weights/best.pt --device $d # test custom
  done
  python hubconf.py  # hub
  python models/yolo.py --cfg $m.yaml  # inspect
  python models/export.py --weights $m.pt --img 640 --batch 1  # export
done

# VOC
for b, m in zip([64, 48, 32, 16], ['yolov5s', 'yolov5m', 'yolov5l', 'yolov5x']):  # zip(batch_size, model)
  !python train.py --batch {b} --weights {m}.pt --data voc.yaml --epochs 50 --cache --img 512 --nosave --hyp hyp.finetune.yaml --project VOC --name {m}
