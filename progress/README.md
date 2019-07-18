# 진행상황

### 20190619
![20190619](./image/20190619.PNG)

### 20190712
#### annotation 작업 마침

hand.name, hand.data, mj-yolov3-tiny.cfg

annForm.py


### 20190716
#### cfg 변경, 4000번 학습(detection X)
1. cfg 변경

yolo3-mj.cfg

3: batch=1

4: subdivisions=64

6: batch=1

7: subdivisions=64

**17: flip=0**

18: learning_rate=0.01

20: max_batches=4000(class * 2000)

127: filters=21

135: classes=2

171: filters=21

177: classes=2



2. 4000번까지 학습

detection X


### 20190718
#### learning rate 변경, 7000번 학습

1. cfg 변경
18: learning_rate=0.001

- memory error
```
#yolo-mj.cfg
width=416(<-608)
height=416(-<608)
```
