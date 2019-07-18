# 진행상황

### 20190619
![20190619](./image/20190619.PNG)

### 20190712
> 1. annotation 작업 마침\
>(1) hand.name
```
left
right
```


(2) hand.data
```
classes = 2
train = data/train.txt
valid = data/test.txt
names = data/hand.name
backup = backup
```


(3) annForm.py

1) 4 classes -> 2 classes
```python
def classNum(hand):
    if hand == "myleft" or hand == "yourleft":  #lefthand
      return '0' # hand.name의 첫번째 줄
    elif hand == "myright" or hand == "yourright":   #righthand
      return '1' # hand.name의 두번째 줄
```

2) 제목이 다를 때마다 파일 새로 생성
```python
if w != w_:
     # print("diffff")
     new.close()
     break
```
