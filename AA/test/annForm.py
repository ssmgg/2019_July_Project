def classNum(hand):
    if hand == 'myleft' or 'yourleft':  #lefthand
        return str(0)
    elif hand == 'myright' or 'youright':   #righthand
        return str(1)


import glob
import os

files = glob.glob("test/*.txt")
print(files, 7)
for file in files:
    file = file.split('\\')[1]
    f = open('test/'+file, encoding='utf8')
    print(f,0)
    lines = f.readlines()
    print(lines)
    line_length = len(lines)
    print(line_length)

    i = 1
    while True:
        print(lines)
        row = lines[i].split('\t')
        hand = classNum(row[3])
        xmin = float(row[4])
        ymin = float(row[5])
        xmax = float(row[6])
        ymax = float(row[7])

        x = str((xmax + xmin)/2)
        y = str((ymax + ymin)/2)
        width = str(xmax - xmin)
        height = str(ymax - ymin)

        newrow = hand + ' ' + x +' ' + y + ' ' + width + ' ' + height + '\n'
        f.write(newrow)
        print(newrow)

        row_ = row[0].split('_')
        temp = lines[i+1].split('\t')
        row__ = temp[0].split('_')
        w = row_[5]
        w_ = row__[5]
        i = i+1
        if w != w:
            print("diffff")
            f.close()
            break


