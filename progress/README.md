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




- detection: 실패

  원인: 학습량 부족(thresh=0 설정 -> detection 됨 -> 결론: 학습에서 문제 발생)


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

![20190718](./image/20190718_7000.PNG)


![7000번 학습시킨 결과 영상](./video/7000.mp4)


- memory error
```
#yolo-mj.cfg
width=416(<-608)
height=416(-<608)
```


3. 8000번까지 학습

- left detection 잘됨

![20190718_8000](./image/20190718_8000.PNG)


![8000번 학습시킨 결과 영상](./video/8000.mp4)


---
## 20190719
### 10000번까지 학습 완료, 안드로이드 얹는 작업 실패, Yolo v2 로 학습 재시작


1. 10000번까지 학습 완료

![1000번 학습 결과](./image/07610_10000.PNG)


2. 안드로이드 얹는 작업 - 실패


3. Yolo v2로 학습 시작
