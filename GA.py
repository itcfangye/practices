##################################
#                                #
#   Last edited on Jan 11, 2017  # 
#                                #
#   By Shu Cheng                 #
##################################

import random
import math
import plot
        
def create_init_group(x = []) :       #产生初始种群
    a = []                              #x为初始个体
    while len(a) < len(x) :
        b = []
        while len(b) < len(x) :
            j = random.randint(0,len(x)-1)
            if x[j] not in b:
                b.append(x[j])
        if b not in a :
            a.append(b)
    return a

def cal_svalue(x = []) :         #计算个体适应值
    _sum = 0                    #x为个体
    for i in range(len(x)-1) :
        a = math.sqrt(((x[i+1][0]-x[i][0])**2)+((x[i+1][1]-x[i][1])**2))
        _sum = _sum + a
    b = 1/_sum
    return b

def cal_gvalue(x = []) :         #计算种群适应度
    value = []                  #x为种群
    _sum = 0
    for i in range(len(x)) :
        a = cal_svalue(x[i])
        _sum = _sum + a
    for j in range(len(x)):
        b = cal_svalue(x[j])/_sum
        value.append(b)
    return value

def select(x = [], y = []) :        #选择
    select = []     #x是种群，y是适应度
    i = 0
    for i in range(len(x)) :
        a = random.random()
        for j in range(0,len(x)) :          #轮盘赌
            if a >= sum(y[0:j]) and a < sum(y[0:j+1]):
                select.append(x[j])
    return select

def exchange(x = []) :          #交叉
    exc1 = []                   #x为种群
    exc2 = []
    for i in range(0, 9, 2) :
        if x[i] != x[i+1] :
            a = random.randint(0, 7)        #选择片段
            exc1 = x[i][a:a+3]
            b = random.randint(0, 7)
            exc2 = x[i+1][b:b+3]
            for j in exc2 :
                x[i].remove(j)
            for k in exc1 :
                x[i+1].remove(k)
            for l in range(2, -1, -1) :
                x[i].insert(a, exc2[l])
                x[i+1].insert(b, exc1[l])
    return x

def variation(x = []) :            #变异
    y = random.randint(1, 9)
    for i in range(y) :               #x为个体
        a = random.randint(0, len(x)-1)
        b = random.randint(0, len(x)-1)
        if a != b :
            x[a], x[b] = x[b], x[a]

def main() :
    father = []
    son = []
    value_f = []
    value_s = []
    maxx = []   #最佳路径
    fit = 0     #最佳路径适应值
    gen = 0     #最佳的代数
    k = 0
    best = []
    maxx = init
    fit = 100*cal_svalue(init)
    print('循环次数：%d' %ex_num)
    print('初始序列为:',init, '适应值为:%0.2f' %fit)
    father = create_init_group(init)
    while k < ex_num :
        value_f = cal_gvalue(father)
        son = select(father, value_f)       #自然选择
        son = exchange(son)              #交换
        for i in range(len(son)) :       #根据可能性变异
            a = random.random()
            if a < chance :
                variation(son[i])
        value_s = cal_gvalue(son)
        while max(value_s) > min(value_f) :
            c = value_s.index(max(value_s))
            d = value_f.index(min(value_f))
            son[c], father[d] = father[d], son[c]
            value_s[c], value_f[d] = value_f[d], value_s[c]
        e = value_f.index(max(value_f))
        best.append(e)
        temp = father[e]
        temp_v = 100*cal_svalue(temp)
        #print(temp, '\t', temp_v, '\t', k)
        if temp_v > fit :
            maxx = temp
            fit = temp_v
            gen = k
        k = k + 1
        
    print('最佳序列为:',maxx, '适应值为:%0.2f' %fit, '此时为第%d代' %gen)
    #plot.plot(best)

#主程序
print('#===================================#')
print('#                                   #')
print('#       遗传算法解决旅行商问题       #')
print('#                                   #')
print('#===================================#')

c1 = [0, 0]   #各城市坐标
c2 = [1, 1]
c3 = [2, 2]
c4 = [3, 3]
c5 = [4, 4]
c6 = [5, 5]
c7 = [6 ,6]
c8 = [7, 7]
c9 = [8, 8]
c10 = [9, 9]
#init = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]   #最短路径
init = [c1, c6, c2, c7, c3, c8, c4, c9, c5, c10]    #预设初始序列
city_num = 10   #城市个数
chance = 0.3    #变异的概率 (0 ~ 1)
ex_num = 1000000   #遗传代数
main()

