# !/usr/bin/env python3
# -*- coding:UTF-8 -*-
# author: ChenDu
# time: 2018/11/4 0004


###########################
# 说明：
#      撰写本文的原因是，笔者在研究博文“http://python.jobbole.com/83563/”中发现
#      原内容有少量笔误，并且对入门学友缺少一些信息。于是笔者做了增补，主要有：
#      1.查询并简述了涉及的大部分算法；
#      2.添加了连接或资源供进一步查询；
#      3.增加了一些lib库的基本操作及说明；
#      4.增加了必须必要的python的部分语法说明；
#      5.增加了对模型算法，数据挖掘等领域的思考和判断；
#      6.修订了原作者代码上的笔误，跑通全部程序，拷贝就可用！
#      7.其他
#      目标是：针对python是0基础！但喜欢数据挖掘的初级学友，方面其入门，减少挫折感！
#              通过“一份带注释的可用代码”来学习！
# 建议：先学习，或初步浏览原作者的博文（如上）。
# 链接：笔者资源收集贴“http://www.cnblogs.com/taichu/p/5216659.html”，供新老学友参考，笔者会不断整理更新！
###########################

###########################
# （0）心得
# 1.因为数据的找寻，分析和建模一条龙代价不菲。
#   应该‘榨干’一份数据和模型的每种可能性，彻底研究掌握。
#   往往能一通百通，一个模型反复折腾能用到各种方法和体会！
###########################


###########################
# （1）观察原始数据（样本）
# 知识点：数据导入；数据可视化
###########################

##################
# 在ubuntu15.10中通过如下6条命令来安装python环境
# sudo apt-get install python   #安装python最新版，一般已经自带最新2.7版本了
# sudo apt-get install python-numpy    #安装python的numpy模块
# sudo apt-get install python-matplotlib
# sudo apt-get install python-networkx
# sudo apt-get install python-sklearn
# python  #看python版本并进入交互式界面，就可以执行如下命令，全部拷贝黏贴进去试试看？
# 另外，可以下载Anaconda的Python IDE集成环境，搜一下非常好，很多SCIPY等核心库都集成了，免去安装之苦！
# 特别注意：笔者是WIN10宿主机上安装Ubuntu15.10最新虚拟机，在Ubuntu中默认安装了python，升级并安装以上lib后实践所有如下代码！
##################

from urllib import request

url = 'http://aima.cs.berkeley.edu/data/iris.csv'
response = request.urlopen(url)
# 以下为本地样本存储路径，请根据实际情况设定！
# localfn='/mnt/hgfs/sharedfolder/iris.csv' #for linux
# localfn='C:\\TEMP\\iris.csv' #for windows
localfn = 'iris.csv'  # for windows
localf = open(localfn, 'w')
localf.write(response.read().decode('utf-8'))
localf.close()

# data examples
# COL1,  COL2,   COL3,   COL4,   COL5
# 5.1   3.5    1.4    0.2    setosa
# … …  …  …  …
# 4.7   3.2    1.3    0.2    setosa
# 7 3.2    4.7    1.4    versicolor
# … …  …  …  …
# 6.9   3.1    4.9    1.5    versicolor
# 6.3   3.3    6  2.5    virginica
# … …  …  …  …
# 7.1   3  5.9    2.1    virginica

#############################
# U can get description of 'iris.csv'
# at 'http://aima.cs.berkeley.edu/data/iris.txt'
# Definiation of COLs:
# 1. sepal length in cm (花萼长)
# 2. sepal width in cm（花萼宽）
# 3. petal length in cm (花瓣长)
# 4. petal width in cm（花瓣宽）
# 5. class:
#      -- Iris Setosa
#      -- Iris Versicolour
#      -- Iris Virginica
# Missing Attribute Values: None
#################################


from numpy import genfromtxt, zeros

# read the first 4 columns
data = genfromtxt(localfn, delimiter=',', usecols=(0, 1, 2, 3))
# read the fifth column
target = genfromtxt(localfn, delimiter=',', usecols=(4), dtype=str)

print(data.shape)
# output: (150, 4)
print(target.shape)
# output: (150,)

# auto build a collection of unique elements
print(set(target))
# output: set(['setosa', 'versicolor', 'virginica'])
# print set(data) #wrong usage of set, numbers is unhashable

######################
# plot库用法简述：
# 'bo'=blue+circle; 'r+'=red+plus;'g'=red+*
# search keyword 'matlab plot' on web for details
# http://www.360doc.com/content/15/0113/23/16740871_440559122.shtml
# http://zhidao.baidu.com/link?url=6JA9-A-UT3kmslX1Ba5uTY1718Xh-OgebUJVuOs3bdzfnt4jz4XXQdAmvb7R5JYMHyRbBU0MYr-OtXPyKxnxXsPPkm9u5qAciwxIVACR8k7
######################

# figure for 2D data
from pylab import plot, show

plot(data[target == 'setosa', 0], data[target == 'setosa', 2], 'bo')
plot(data[target == 'versicolor', 0], data[target == 'versicolor', 2], 'r+')
plot(data[target == 'virginica', 0], data[target == 'virginica', 2], 'g*')
show()

# 注意:如果在Ubuntu的python交互式环境下运行，则figure会打断程序的RUN.
# 如果你用Anaconda的spyder（Python2.7）则方便的多，生成的figure会自动输出到console
# 且不会打断程序运行！

# figure for all 4D（4个维度） data, 同色一类，圈是花萼，加号花瓣
setosa_sepal_x = ssx = data[target == 'setosa', 0]
setosa_sepal_y = ssy = data[target == 'setosa', 1]
setosa_petal_x = spx = data[target == 'setosa', 2]
setosa_petal_y = spy = data[target == 'setosa', 3]

versicolor_sepal_x = vsx = data[target == 'versicolor', 0]
versicolor_sepal_y = vsy = data[target == 'versicolor', 1]
versicolor_petal_x = vpx = data[target == 'versicolor', 2]
versicolor_petal_y = vpy = data[target == 'versicolor', 3]

virginica_sepal_x = vgsx = data[target == 'virginica', 0]
virginica_sepal_y = vgsy = data[target == 'virginica', 1]
virginica_petal_x = vgpx = data[target == 'virginica', 2]
virginica_petal_y = vgpy = data[target == 'virginica', 3]

plot(ssx, ssy, 'bo', spx, spy, 'b+')
plot(vsx, vsy, 'ro', vpx, vpy, 'r+')
plot(vgsx, vgsy, 'go', vgpx, vgpy, 'g+')
show()

# figure for 1D（花萼的长度），三类长度及平均值的直方图
# pylab详细用法参考如下
# http://hyry.dip.jp/tech/book/page/scipy/matplotlib_fast_plot.html
from pylab import figure, subplot, hist, xlim, show

xmin = min(data[:, 0])
xmax = max(data[:, 0])
figure()  # 可省略，默认会生成一个figure
subplot(411)  # distribution of the setosa class (1st, on the top)
hist(data[target == 'setosa', 0], color='b', alpha=.7)
xlim(xmin, xmax)
# subplot（行,列,plot号）；(4,1,2)合并为412,都小于10可合成
subplot(412)  # distribution of the versicolor class (2nd)
hist(data[target == 'versicolor', 0], color='r', alpha=.7)
xlim(xmin, xmax)
subplot(413)  # distribution of the virginica class (3rd)
hist(data[target == 'virginica', 0], color='g', alpha=.7)
xlim(xmin, xmax)
subplot(414)  # global histogram (4th, on the bottom)
hist(data[:, 0], color='y', alpha=.7)
xlim(xmin, xmax)
show()

###########################
# （2）样本分类
# 朴素贝叶斯分类器是常用的一种，分为（高斯模型/非多项式模式/非伯努利模式）
###########################

# 仿造target阵列(1维)弄出全0的t阵列
t = zeros(len(target))
# type(t) #show type of t (numpy.ndarray)
# print t #show contains of t
# 将target阵列中特定元素的位置设置为1(真简洁)
t[target == 'setosa'] = 1
t[target == 'versicolor'] = 2
t[target == 'virginica'] = 3
# print t

# 用全部data集来做训练
from sklearn.naive_bayes import GaussianNB

classifier = cf = GaussianNB()
cf.fit(data, t)  # training on the iris dataset
# print(cf.predict(data[0]))  # 训练完分类1条数据
# output:[ 1.]
# print(t[0])
# output:1.0

# 从原始数据data中划分为训练集和验证集，t也做同样划分
from sklearn import cross_validation

train, test, t_train, t_test = cross_validation.train_test_split(data, t, test_size=0.4, random_state=0)

print(train.shape)
# output:(90, 4)
print(test.shape)
# output:(60, 4)
print(t_train.shape)
# output:(90,)
print(t_test.shape)
# output:(60,)

# 用60%数据训练后，再用40%数据验证，得到93.3%
cf.fit(train, t_train)  # train
print(cf.score(test, t_test))  # test
# output:0.93333333333333335
cf.score(train, t_train)  # 用训练集训练后同样用它测试居然不是100%分类！
# output:0.97777777777777775

# 用全部数据训练后，同样用它测试，结果低于刚才97%
cf.fit(data, t)
# output:GaussianNB()
cf.score(data, t)
# output:0.95999999999999996


# 用100%数据训练后，再用40%数据验证，得到94.99%
cf.fit(data, t)
# output:GaussianNB()
cf.score(test, t_test)
# output:0.94999999999999996

#############################################################
# TODO：研究计划（笔者会另立博文研究此问题）
# 因为朴素贝叶斯分类法基于每个feature都是概率独立不相关。但其实相关，可尝试：
# 1.显然花萼长宽，花瓣的长宽，是很强的相关性，形成2个新feature；为sepal-size，petal-size
# 2.花萼与花瓣的长度合并，宽度合并，可能也有相关性，形成2个新feature！为whole-length，whole-wide
# 3.原来花萼长与宽，花瓣长与宽，就是4个初始feature;
# 4.以上初步判断的8个feature的组合关系？举例：一种花，就是花瓣很小，花萼较大呢？生物学有必然比例ratio吗？
#  再比如，一种花整体都很修长？或矮短？
#  我们也怀疑sepal-size和petal-size有一定的概率联系（正相关或负相关或某种关系）
#  即使分类器做到了100%，对未来样本的分类也不一定100%正确，因为样本的收集也存在标定误差（人为录入误差）
# TRY：尝试变更模型，数据转换后，再次做分类测试，交叉验证，期望提升准确率！
#############################################################


# 用混淆矩阵估计分类器表现
from sklearn.metrics import confusion_matrix

print(confusion_matrix(cf.predict(test), t_test))
# output:[[16  0  0]
# output: [ 0 23  4]
# output: [ 0  0 17]]

# 混淆矩阵简单说明
#        预测情况
#        -----------
#        类1 类2 类3
# 实 |类1 43  5   2
# 际 |类2 2   45  3
# 情 |类3 0   1   49
# 况 |
#
# 说明：正确的猜测都在表格的对角线
# 解读：实际情况是3个类每个都50个样本；
#      类3有1个错误的猜测为类2；
#      类2有2个错误的猜测为类1,3个错误的识别为类3
#      类1有5个错误的猜测为类2,2个错误的识别为类3

# 分类器性能的完整报告
# Precision：正确预测的比例
# Recall（或者叫真阳性率）：正确识别的比例
# F1-Score：precision和recall的调和平均数

from sklearn.metrics import classification_report

print(classification_report(classifier.predict(test), t_test, target_names=['setosa', 'versicolor', 'virginica']))
# output:            precision    recall  f1-score   support
# output:    setosa       1.00      1.00      1.00        16
# output:versicolor       1.00      0.85      0.92        27
# output: virginica       0.81      1.00      0.89        17
# output:avg / total      0.95      0.93      0.93        60

##############################################################
# 补充调和平均数知识点
# 调和平均数：Hn=n/(1/a1+1/a2+...+1/an)
# 几何平均数：Gn=(a1a2...an)^(1/n)
# 算术平均数：An=(a1+a2+...+an)/n
# 平方平均数：Qn=√ [(a1^2+a2^2+...+an^2)/n]
# 这四种平均数满足 Hn ≤ Gn ≤ An ≤ Qn
#
# 调和平均数典型举例：
# 问：有4名学生分别在一个小时内解题3、4、6、8道，求平均解题速度多少（1小时能解几道）？
# 答：就是求调和平均数，即1/[(1/3+1/4+1/6+1/8)/4]=4/(1/3+1/4+1/6+1/8)=4.57
###########################################################


# 以上仅仅只是给出用于支撑测试分类的数据量。
# 分割数据、减少用于训练的样本数以及评估结果等操作
# 都依赖于配对的训练集和测试集的随机选择


# 如果要切实评估一个分类器并与其它的分类器作比较的话，
# 我们需要使用一个更加精确的评估模型，例如Cross Validation。
# 该模型背后的思想很简单：多次将数据分为不同的训练集和测试集，
# 最终分类器评估选取多次预测的平均值。
# sklearn为我们提供了运行模型的方法：

from sklearn.cross_validation import cross_val_score

# cross validation with 6 iterations
scores = cross_val_score(classifier, data, t, cv=6)
print(scores)
# output:[ 0.92592593  1.          0.91666667  0.91666667  0.95833333  1.        ]
# 并非迭代越多次越好。当前CV=6，迭代6次

# 输出是每次模型迭代产生的精确度的数组。我们可以很容易计算出平均精确度：
from numpy import mean

print(mean(scores))
# output:0.96

# 循环不断增加迭代cv次数，并输出mean值
# 迭代CV必须>=2,否则报错'ValueError: k-fold cross validation requires at least one train / test split by setting n_folds=2 or more, got n_folds=1.'
# 迭代CV必须小于最小的一个样本数目（对t=50;t_train=27;t_test=16），详见后面ndarray归类打印！
# 1.穷举data的所有迭代cv可能的交叉验证平均值并打印
for i in range(2, 51):
    scores = cross_val_score(classifier, data, t, cv=i)
    print(mean(scores))  # 每句for语句在交互式界面必须跟一行空行（没任何字符包括空格）才能表示输入结束！

# 2.穷举test的所有迭代cv可能的交叉验证平均值并打印
for i in range(2, 17): print(mean(cross_val_score(classifier, test, t_test, cv=i)))

# 3.穷举train的所有迭代cv可能的交叉验证平均值并打印
for i in range(2, 28): print(mean(cross_val_score(classifier, train, t_train, cv=i)))

#
#
# 对一维numpy.ndarray数字值归类并打印
ndarray = {}
for item in t: ndarray[item] = ndarray.get(item, 0) + 1
# 下面必须有一行空行（没任何空格！），让交互式python确认for语句完成输入

print(ndarray)
# output:{1.0: 50, 2.0: 50, 3.0: 50}

# 对一维numpy.ndarray数字值归类并打印
ndarray = {}
for item in t_train: ndarray[item] = ndarray.get(item, 0) + 1
# 下面必须有一行空行，让交互式python确认for语句完成输入

print(ndarray)
# output:{1.0: 34, 2.0: 27, 3.0: 29}

# 对一维numpy.ndarray数字值归类并打印
ndarray = {}
for item in t_test: ndarray[item] = ndarray.get(item, 0) + 1
# 下面必须有一行空行，让交互式python确认for语句完成输入

print(ndarray)
# output:{1.0: 16, 2.0: 23, 3.0: 21}

#
#
# ***********************************
# 附加内容：写一个循环，从1和n-1到n-1和1来划分训练集和验证集；
# TODO：    并对每种划分应用model（此处是朴素贝叶斯分类器-高斯模型）训练后交叉验证；
#          交叉验证时也穷举所有可能的cv迭代次数；
#          收集数据并显示，看此model对已知数据集合的分类最优点在哪里？
#          figure的X是train/data（训练集合占比%）(0,1)；Y轴交叉验证mean值的迭代穷举后均值！(0,1)
#          因为训练集和验证集划分每次是随机的，每RUN一次会有一张不同的二维图
# TODO：    进一步扩展，对一个矩阵样本，能否自动的按照一定规律，穷举各种算法模型的结果？
#          并能设定阈值报警。这样我们就有个一个遍历所有算法的基础toolbox，对原始矩阵样式的样本
#          做自动auto的扫描，提供基本的信息和情况，然后再人为去研究。
# ***********************************

###########################
# （3）聚类
###########################
# k-means算法简介：算法接受输入量k ，并将n个数据对象分为k个聚类；获得的聚类满足:同一聚类中的对象相似度较高;不同聚类中对象相似度低；
#                聚类相似度是利用各聚类中对象的均值所获得一个“中心对象”（引力中心）来进行计算。
# k-means 算法基本步骤：
# （1） 从 n个数据对象任意选择k个对象作为初始聚类中心（最终期望聚为k类）；
# （2） 根据每个聚类对象的均值（中心对象），计算每个对象与这些中心对象的距离；按最小距离重新对相应对象进行划分；
# （3） 重新计算每个（有变化）聚类的均值（中心对象）；
# （4） 计算标准测度函数，当满足一定条件，如函数收敛时，则算法终止；如果条件不满足则回到步骤（2）。
############################


from sklearn.cluster import KMeans

kms = KMeans(n_clusters=3)  # initialization 先验知道3种植物，所以设定引力中心为聚合成3类。
# kmeans = KMeans(k=3, init='random') # both parameters are wrong
kms.fit(data)  # actual execution
c = kms.predict(data)

from sklearn.metrics import completeness_score, homogeneity_score

print(completeness_score(t, c))
# output:0.764986151449
print(homogeneity_score(t, c))
# output:0.751485402199

# 特别注意！t中只要是3类值就行，不一定非要1,2,3
# 当大部分数据点属于一个给定的类并且属于同一个群集，那么完整性得分就趋向于1。
# 当所有群集都几乎只包含某个单一类的数据点时同质性得分就趋向于1.
figure()
subplot(211)  # top figure with the real classes
plot(data[t == 1, 0], data[t == 1, 2], 'bo')
plot(data[t == 2, 0], data[t == 2, 2], 'ro')
plot(data[t == 3, 0], data[t == 3, 2], 'go')
subplot(212)  # bottom figure with classes assigned automatically
plot(data[c == 1, 0], data[c == 1, 2], 'bo', alpha=.5)
plot(data[c == 2, 0], data[c == 2, 2], 'go', alpha=.5)
plot(data[c == 0, 0], data[c == 0, 2], 'mo', alpha=.5)
show()

# 观察此图我们可以看到，底部左侧的群集可以被k-means完全识别，
# 然而顶部的两个群集有部分识别错误。按照kmean的中心对象是引力中心的聚类方法
# 出现识别错误是必然的；样本的偶然性可能导致识别错误

# 如下是将4个feature维度组合为2个点放入一个平面，也可以看到聚类为3种后，
# 边界变得清晰了。
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(211)  # top figure with the real classes
plt.plot(data[t == 1, 0], data[t == 1, 1], 'bo', data[t == 1, 2], data[t == 1, 3], 'b+')
plt.plot(data[t == 2, 0], data[t == 2, 1], 'ro', data[t == 2, 2], data[t == 2, 3], 'r+')
plt.plot(data[t == 3, 0], data[t == 3, 1], 'go', data[t == 3, 2], data[t == 3, 3], 'g+')
plt.subplot(212)  # bottom figure with classes assigned automatically
plt.plot(data[c == 0, 0], data[c == 0, 1], 'bo', data[c == 0, 2], data[c == 0, 3], 'b+', alpha=.7)
plt.plot(data[c == 1, 0], data[c == 1, 1], 'ro', data[c == 1, 2], data[c == 1, 3], 'r+', alpha=.7)
plt.plot(data[c == 2, 0], data[c == 2, 1], 'go', data[c == 2, 2], data[c == 2, 3], 'g+', alpha=.7)
p = plt
fig = plt.gcf()
fig.show()  # p.show()也可，但二者只能执行一次。

###########################
# （4）回归
###########################

# 回归是一个用于预测变量之间函数关系调查的方法。
# 假设有两个变量：一个被认为是因，一个被认为是果。
# 回归模型描述两者关系；从一个变量推断另一个变量；
# 当这种关系是一条线时，称为线性回归。


##############
# sklear.linear_model模块中的LinearRegression模型。
# 它通过计算每个数据点到拟合线的垂直差的平方和，
# 找到平方和最小的最佳拟合线。类似sklearn模型；
#
##############

# 下面举例随机产生了40个点样本，但大致函数趋势是
# 在第一象限线性增长，用线性回归来找出拟合线并评估
# Step1-随机产生第一象限40个点
from numpy.random import rand

x = rand(40, 1)  # explanatory variable
y = x * x * x + rand(40, 1) / 5  # depentend variable

# Step2-线性回归
from sklearn.linear_model import LinearRegression

linreg = LinearRegression()
linreg.fit(x, y)

# Step3-随机产生x变量，用线性回归模型推断y变量（推断出来是一条线）
from numpy import linspace, matrix

# 产生0到1之间40个样本值
randx = linspace(0, 1, 40)
# 用随机产生的40个x轴样本，用线性回归预测其y轴样本，并输出比较
# 推断y时先将x当做矩阵转置为y再推断
plot(x, y, 'o', randx, linreg.predict(matrix(randx).T), '--r')
show()

# Step4-通过测量MSE指标看拟合线与真实数据的距离平方。0最好
from sklearn.metrics import mean_squared_error

print(mean_squared_error(linreg.predict(x), y))

#########################
# 针对本例实际花萼的长宽数据做线性回归
#########################
# 获取x和y（需要reshape来转换数组(50,)到一维矩阵(50,1)，才能做linreg.fit!
ssx_blue = data[target == 'setosa', 0].reshape((50, 1))  # 获取setosa的sepal花萼length
ssy_blue = data[target == 'setosa', 1].reshape((50, 1))  # 获取setosa的sepal花萼width

# 用x和y获得线性回归模型
linreg = LinearRegression()
linreg.fit(ssx_blue, ssy_blue)

# 随机产生x变量，用线性回归模型推断y变量（推断出来是一条线）
# 根据经验蓝色品种setosa的花萼sepal的长宽尺寸一般为X:[4.0-6.0]y:[2.5-4.5]
randx = linspace(4.0, 6.0, 50)
plot(ssx_blue, ssy_blue, 'o', randx, linreg.predict(matrix(randx).T), '--r')
show()

# 通过测量MSE指标看拟合线与真实数据的距离平方。0最好
print(mean_squared_error(linreg.predict(ssx_blue), ssy_blue))

###########################
# （5）相关性分析
###########################

# 通过研究feature之间的相关性来理解变量之间是否相关，相关强弱。
# 相关性分析帮助定位被依赖的重要变量。最好的相关方法可能是皮尔逊积矩相关系数。
# 它是由两个变量的协方差除以它们的标准差的乘积计算而来。
# 我们将鸢尾花数据集的4个变量两两组合计算出其相关性系数。
# 特别说明：feature是可以组合与变换的，所以不一定是未处理的初始feature两两做相关性判断，
#          而可能是人为判断有相关性的，尝试组合或变换feature再不断测试相关性。

# 当值一起增长时相关性为正。当一个值减少而另一个值增加时相关性为负。
# 1代表完美的正相关，0代表不相关，-1代表完美的负相关。

# 本例红色被关联为最高的正相关，可以看出最强相关是：
# “花瓣宽度”petal width和“花瓣长度”petal length这两个变量。

from numpy import corrcoef

corr = corrcoef(data.T)  # .T gives the transpose
print(corr)
# output:[[ 1.         -0.10936925  0.87175416  0.81795363]
# output: [-0.10936925  1.         -0.4205161  -0.35654409]
# output: [ 0.87175416 -0.4205161   1.          0.9627571 ]
# output: [ 0.81795363 -0.35654409  0.9627571   1.        ]]

from pylab import pcolor, colorbar, xticks, yticks
from numpy import arange

pcolor(corr)  # 添加相关性矩阵，4个属性所以是4x4
colorbar()  # 添加彩色注释条
# 添加X,Y轴注释，默认一个属性是1，坐标是1,2,3,4，对应四个属性name如下。
xticks(arange(1, 5), ['sepal length', 'sepal width', 'petal length', 'petal width'], rotation=-20)
yticks(arange(1, 5), ['sepal length', 'sepal width', 'petal length', 'petal width'], rotation=-45)
show()

###########################
# （6）成分分析（降维）
# 涉及算法之一PCA
###########################


from sklearn.decomposition import PCA

# 降维到更少feature（主成分）不仅仅是为了可视化
# 虽然3D也可以看，但不直观，最直观的是2D平面图，而4D或更高维人眼无法观察
# 所以将data中原始4个feature降维到2维来观察。
# 特别注意：它等于自动的将feature做了算法组合，以期望分离不同种类。
pca = PCA(n_components=2)

pcad = pca.fit_transform(data)

plot(pcad[target == 'setosa', 0], pcad[target == 'setosa', 1], 'bo')
plot(pcad[target == 'versicolor', 0], pcad[target == 'versicolor', 1], 'ro')
plot(pcad[target == 'virginica', 0], pcad[target == 'virginica', 1], 'go')
show()

# 查看主成分PC
print(pca.explained_variance_ratio_)
# output: [ 0.92461621  0.05301557]
pc1, pc2 = pca.explained_variance_ratio_  # 保存2个PC

print(1 - sum(pca.explained_variance_ratio_))
# output:0.0223682249752
print(1.0 - pc1 - pc2)  # 等价于上述输出

# 逆变换还原数据
data_inv = pca.inverse_transform(pcad)
# 比较还原后数据和原始数据的相似度
print(abs(sum(sum(data - data_inv))))
# output:6.66133814775e-15

# 循环尝试：PC数量从1维到4维（原始数据也是4维）
# 看PCA覆盖信息量；4个肯定100%，3个也很高了；
for i in range(1, 5):
    pca = PCA(n_components=i)
    pca.fit(data)
    print(sum(pca.explained_variance_ratio_) * 100, '%')

# output:92.4616207174 %
# output:97.7631775025 %
# output:99.481691455 %
# output:100.0 %


print("END")
# END
