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

def ReadGenerateTxtName(rootdir):
    lines = []
    with open(rootdir, 'r',encoding='utf-8') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(double(line))
    return lines
def drawPic(data,lable):

    x = [i for i in range(len(data))]
    # plt.ylim(0.1, 1)  # 限定纵轴的范围

    #plt.plot(x,data)
    plt.scatter(x,data)
    plt.title('line chart')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(lable)
    plt.show()

def drawPic_chafen(data,lable):

    x = [i for i in range(len(data))]
    #plt.ylim(0.1, 1)  # 限定纵轴的范围

    plt.plot(x,data)

    plt.title('line chart')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(lable)
    plt.show()

AllAPdata = []
AllAPlabel = []
if __name__ == '__main__':

    #data_lists = ReadTxtName("date.txt")
    name_1 = r'July07_empty_temp_4'
    name_2 = r'July07_empty_temp_3'   #


    lists_1 = ReadTxtName(name_1 + ".txt")
    lists_2 = ReadTxtName(name_2 + ".txt")# '''

    '''lists_8_9 = [111,116,118,123,123,137,184,155,147,146,144,151]
    lists_4_5 = [111,120,122,119,123,128,175,152,145,144,143,151]
    empty_1 = [115,120,122,126,127,133,181,157,150,149,147,156]
    empty_2 = [115,120,122,127,127,133,180,156,149,149,147,156]
    center_list_1 = [110,115,117,121,122,128,175,152,145,144,142,150]
    center_list_2 = [110,115,117,121,122,128,175,152,145,144,142,150]#'''
    dif = list(map(lambda x: x[0]-x[1], zip(lists_1, lists_2)))


    #cha_lists = ReadTxtName("e_data.txt")
    drawPic(dif,'diff_')
    #drawPic(empty_lists,'空场')
    #drawPic_chafen(cha_lists,'差分')
