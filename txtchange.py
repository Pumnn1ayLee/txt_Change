import itertools
import pandas as pd
import os
need_path = 'E:/SAR/labels/val/'
nano_path = 'E:/SAR/labels1/val/'
new = []
dir = os.listdir(need_path)
for i in dir:
    file_name = os.path.basename(i)
    file_name1 = file_name.split('.')[0]
    print(file_name1)
    f = open(need_path + file_name1 + '.txt', 'r')
    something = f.readlines()
    print(something)
    for index,line in enumerate(something):
        strT = something[index]
        first = strT.strip('\n')
        out = first.split()
        new.append(out)
        print(out)
        for i in out:
            new1 = []
            new1.append(out[9])
            new1.append(out[8])
            xmax = float(max(out[0],out[2],out[4],out[6]))
            xmin = float(min(out[0],out[2],out[4],out[6]))
            ymax = float(max(out[1],out[3],out[5],out[7]))
            ymin = float(min(out[1],out[3],out[5],out[7]))
            print(xmin,xmax)
            l1 = abs(float(xmax - xmin))
            h1 = abs(float(ymax - ymin))
            xc1 = abs(float(xmax - xmin))
            xc2 = abs(float(xc1/2))
            xc3 = abs(float(xc2-1))
            yc1 = abs(float(ymax - ymin))
            yc2 = abs(float(yc1/2))
            yc3 = abs(float(yc2-1))
            xcenter = abs(float(xc3/512))
            ycenter = abs(float(yc3/512))
            L = abs(float(l1 / 512))
            H = abs(float(h1 / 512))
            new1.append(xcenter)
            new1.append(ycenter)
            new1.append(L)
            new1.append(H)
            newFile = open(nano_path + file_name1 + '.txt', 'a')
        for i in new1:
            newFile.write(str(i) + ' ')
        newFile.write('\n')
        newFile.close()
        new1.clear()