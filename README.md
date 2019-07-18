7월 프로젝트
----

# Yolo+Android (2개월_s)
https://junyoung-jamong.github.io/machine/learning/2019/01/25/Android%EC%97%90%EC%84%9C-%EB%82%B4-YOLO%EB%AA%A8%EB%8D%B8-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0.html

## 핸드셋
hand data set 을 활용하는 예제, egohand dataset이 어떤 것이고, label 처리 코드도 존재
(egohands_dataset_clean, egohands_dataset_clean_4classes_
https://github.com/victordibia/handtracking


## hand data set 원본 다큐먼트
http://vision.soic.indiana.edu/projects/egohands/


---

1. cfg
```
3: batch=1
4: subdivisions=64
6: batch=1
7: subdivisions=64
*17: flip=0*
18: learning_rate=0.01
20: max_batches=4000(class * 2000)
127: filters=21
135: classes=2
171: filters=21
177: classes=2
```
- If you train the model to distinguish Left and Right objects as separate classes (left/right hand, left/right-turn on road signs, ...) then for disabling flip data augmentation - add flip=0


2. hand.name
```
left #class 0
right #class 1
```


3. hand.data
```
classes = 2
train = data/train.txt
valid = data/test.txt
names = data/hand.name
backup = backup
```


4. cmd code
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
>cd C:\Users\rhdwb\Desktop\darknet\build\darknet\x64
C:\Users\rhdwb\Desktop\darknet\build\darknet\x64\data\hand\CARDS_COURTYARD_B_T_frame_0036.jpg
```
