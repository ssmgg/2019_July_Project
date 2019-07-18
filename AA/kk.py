import glob

files = glob.glob('C:/Users/rhdwb/Desktop/darknet/build/darknet/x64/data/hand/*.txt')
print(files)
i=0
test = open("test.txt", 'w', encoding='utf8')
train = open("train.txt", 'w', encoding='utf8')

for file in files:
    i = i+1
    if i < 1000:
        test.write(file.split('.')[0]+'.jpg'+'\n')
    elif i > 1000:
        train.write(file.split('.')[0]+'.jpg'+'\n')
    elif i == 1000:
        test.close()
train.close()
