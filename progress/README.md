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


2. 4000번까지 학습




detection X

![11232_4000](./image/11232_4000.PNG)

---
### 20190718
#### learning rate 변경, 학습

1. cfg 변경

```
18: learning_rate=0.001
```


2. 7000번까지 학습

- left detection이 잘 안됨

![20190718](./image/20190718.PNG)

- memory error
```
#yolo-mj.cfg
width=416(<-608)
height=416(-<608)
```


3. 8000번까지 학습

- left detection 잘됨

![8000](./video/8000.mp4)
