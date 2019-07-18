#f = open("C:/Users/rhdwb/Desktop/handtracking/images/train/train_labels.txt", 'r')
# f = open("prac.txt", 'r')
f = open("train_labels.txt", 'r')

lines = f.readlines()
line_length = len(lines)
header = lines[0]
i = 1

while True:
    row = lines[i].split('\t')
    name = row[0].split('.')
    new = open(name[0]+'.txt','w', encoding='utf8') #한 줄을 읽고 파일명 설정
    new.write(header)#filename   width   height  class   xmin  ymin    xmax    ymax
    while True:
        new.write(lines[i])
        print(lines[i])
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
