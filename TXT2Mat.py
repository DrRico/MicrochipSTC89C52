# -*-coding = utf-8-*-
import os
import pickle
import matplotlib.pyplot as plt
import scipy.io as scio
from pylab import *  # 支持中文

mpl.rcParams['font.sans-serif'] = ['SimHei']

def ReadTxtName(rootdir):
    lines = []
    with open(rootdir, 'r',encoding='utf-8') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            if line.startswith('j'):
                lines.append(int(line.split('CH1=')[1].split(' (')[0]))
    return lines

def drawPic(data,lable):
    x = [i for i in range(len(data))]
    plt.ylim(14200, 15800)  # 限定纵轴的范围

    plt.plot(x,data)


    plt.title('line chart')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(lable)

    plt.show()


def saveMat(name,data):
    # keys = [str(i) for i in range(1,len(data)+1)]
    # dic = dict(zip(keys,data))
    filename = name+'.mat'
    scio.savemat(filename, mdict={'means': data})
    # f = scio.loadmat(filename)
    # print(f)


if __name__ == '__main__':
    name_str = 'July04_p16_1_1'
    empty_lists = ReadTxtName(name_str+".txt")
    saveMat(name_str,empty_lists)


    #drawPic(empty_lists,'空场')
    #drawPic(data_lists,'数据')