def classNum(hand):
    if hand == "myleft" or hand == "yourleft":  #lefthand
        return '0'
    elif hand == "myright" or hand == "yourright":   #righthand
        return '1'


#f = open("C:/Users/rhdwb/Desktop/darknet/build/darknet/x64/data/hand/train_labels.txt", 'r')
f = open("prac.txt")
#f= open("test_labels.txt")
#f = open("train_labels.txt")

lines = f.readlines()
line_length = len(lines)
i = 1

while True:
    row = lines[i].split('\t')
    name = row[0].split('.')
    new = open(name[0]+'.txt','w', encoding='utf8') #한 줄을 읽고 파일명 설정
    while True: #한줄씩 annotation 내용 재설정
        row = lines[i].split('\t')
        hand = str(classNum(row[3]))
        print(hand)
        print(type(hand))
        xmin = float(row[4])
        ymin = float(row[5])
        xmax = float(row[6])
        ymax = float(row[7])

        x = str(round(((xmax + xmin) / 2.0 - 1)/float(row[1]),4))
        y = str(round(((ymax + ymin) / 2.0 - 1)/float(row[2]),4))
        width = str(round((xmax - xmin)/float(row[1]),4))
        height = str(round((ymax - ymin)/float(row[2]),4))

        newrow = hand + ' ' + x + ' ' + y + ' ' + width + ' ' + height + '\n'
        print(newrow)
        new.write(newrow)

        row_ = row[0].split('_')
        temp = lines[i + 1].split('\t')
        row__ = temp[0].split('_')
        w = row_[5]
        w_ = row__[5]
        print(w, w_)
        i = i+1
        if w != w_:
            print("diffff")
            new.close()
            break
