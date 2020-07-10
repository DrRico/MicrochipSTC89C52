import scipy.io as scio

path = 'data//July04_p5_6_1.mat'
matData = scio.loadmat(path)
matData = matData['means'][0]
hexLists = []
for i in matData:
    hexLists.append(str(hex(i))[2:])
print(hexLists)
n = 104  #大列表中几个数据组成一个小列表
hexLists = [hexLists[i:i + n] for i in range(0, len(hexLists), n)]
print(hexLists)
print(''.join(hexLists[0]))
print(''.join(hexLists[1]))

