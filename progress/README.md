# 진행상황
---
### 20190619
![20190619](./image/20190619.PNG)
![20190619_ssmgg](./video/20190619_ssmgg.mp4)

----
### 20190712
#### annotation 작업 마침

hand.name, hand.data, mj-yolov3-tiny.cfg

annForm.py

---
### 20190716
#### cfg 변경, 4000번 학습(detection X)
1. cfg 변경

  yolo3-mj.cfg
```
3: batch=1
4: subdivisions=64
6: batch=1
7: subdivisions=64
**17: flip=0**
# If you train the model to distinguish Left and Right objects as separate classes (left/right hand, left/right-turn on road signs, ...) then for disabling flip data augmentation - add flip=0
18: learning_rate=0.01
20: max_batches=4000(class * 2000)
127: filters=21
135: classes=2
171: filters=21
177: classes=2
```


2. 4000번까지 학습


```cmd
# train first
>darknet.exe detector train data/hand.data cfg/mj-yolov3-tiny.cfg darknet53.conv.74
  or
>darknet.exe detector train data/hand.data cfg/mj-yolov3-tiny.cfg darknet53.conv.74 -map

# train
>darknet.exe detector train data/hand.data cfg/yolov3-mj.cfg backup/yolov3-mj_7000.weights
  or
>darknet.exe detector train data/hand.data cfg/yolov3-mj.cfg backup/yolov3-mj_7000.weights -map

# test
# image
>darknet.exe detector test data/hand.data cfg/yolov3-mj.cfg backup/yolov3-mj_7000.weights C:\Users\rhdwb\Desktop\darknet\build\darknet\x64\data\hand\CARDS_COURTYARD_B_T_frame_0036.jpg
# webcam
>darknet.exe detector demo data/hand.data cfg/mj-yolov3-tiny.cfg backup/mj-yolov3-tiny_last.weights

# darknet dir
> cd C:\Users\rhdwb\Desktop\darknet\build\darknet\x64
C:\Users\rhdwb\Desktop\darknet\build\darknet\x64\data\hand\CARDS_COURTYARD_B_T_frame_0036.jpg
```


detection X

![1.1232_4000](./image/1.1232_4000.PNG)

---
### 20190718
#### learning rate 변경, 7000번 학습

1. cfg 변경

```
18: learning_rate=0.001
```


- memory error
```
#yolo-mj.cfg
width=416(<-608)
height=416(-<608)
```
