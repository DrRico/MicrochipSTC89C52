# -*-coding = utf-8-*-
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

    plt.plot(x,data)
    # plt.scatter(x,data)
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

    count = 5
    start = 13 * (count-1)
    end = 13 * count
    name = r'July07_empty_temp_3'
    empty_lists = ReadTxtName(name + ".txt")
    drawPic(empty_lists,name)

    # cha_lists = ReadTxtName("e_data.txt")
    # drawPic_chafen(cha_lists,'差分')

# [111,116,118,123,123,137,184,155,147,146,144,151]
# 第一组空场[115,120,122,126,127,133,181,157,150,149,147,156]