import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import seaborn as sns
import copy

##数据全显示
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)


##绘图时可以显示中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

##去除省略号
np.set_printoptions(threshold=np.inf)


# #读数据
filepath=r"D:\python\result(washed).csv"
df=pd.read_csv(filepath,encoding="gbk",header=0,engine="python")


## 1.	请以课程1成绩为x轴，体能成绩为y轴，画出散点图。
## 量化体育成绩，bad在60~69随机，general在70~79随机，good在80~89随机，excellent在90~99随机

C1_list=df.C1 #C1成绩列表
PE_list=[]    #体育成绩列表
for i in range(len(df)):
    if df.Constitution[i] == "bad":
        j=random.randint(60,69)
        PE_list.append(j)
    elif df.Constitution[i] == "general":
        j = random.randint(70, 79)
        PE_list.append(j)
    elif df.Constitution[i] == "good":
        j = random.randint(80, 89)
        PE_list.append(j)
    elif df.Constitution[i] == "excellent":
        j = random.randint(90, 99)
        PE_list.append(j)
plt.scatter(C1_list,PE_list,c='red',marker='*')
plt.title("课程C1和体育成绩Constitution散点图")
plt.xlabel("C1")
plt.ylabel("Constitution")
plt.savefig('exp2-1-scatterplot.png',bbox_inches='tight')
plt.show()

## 2.	以5分为间隔，画出课程1的成绩直方图。
bins=[65,70,75,80,85,90]  #设置间隔
plt.hist(df.C1,edgecolor='black',bins=bins)
plt.title('课程C1成绩直方图')
plt.grid(True, linestyle='--', alpha=0.5,axis='y')
plt.savefig('exp2-2-Histogram.png',dpi=300,bbox_inches='tight')
plt.show()

## 3.	对每门成绩进行z-score归一化，得到归一化的数据矩阵。
## 量化体育成绩，bad在60~69随机，general在70~79随机，good在80~89随机，excellent在90~99随机

list=[]   #存放所有成绩的列表，是二维列表
list.append(df.C1.tolist())
list.append(df.C2.tolist())
list.append(df.C3.tolist())
list.append(df.C4.tolist())
list.append(df.C5.tolist())
list.append(df.C6.tolist())
list.append(df.C7.tolist())
list.append(df.C8.tolist())
list.append(df.C9.tolist())
PE_sum=0
PE_list=[]
for i in range(len(df)):
    if df.Constitution[i] == "bad":
        j=random.randint(60,69)
        PE_sum+=j
        PE_list.append(j)
    elif df.Constitution[i] == "general":
        j = random.randint(70, 79)
        PE_sum += j
        PE_list.append(j)
    elif df.Constitution[i] == "good":
        j = random.randint(80, 89)
        PE_sum += j
        PE_list.append(j)
    elif df.Constitution[i] == "excellent":
        j = random.randint(90, 99)
        PE_sum += j
        PE_list.append(j)
PE_average=PE_sum/len(df) #体育成绩平均值
list.append(PE_list)
PE_SUM=0  #体育成绩-体育成绩平均值然后平方，最后所有项求和

for i in list[9]:
    PE_SUM+=(list[9][i]-PE_average)**2
PE_var=np.sqrt(PE_SUM/len(df))    #PE_var表示体育成绩标准差

j=0
#每一列进行z-score归一化，j表示列数
while j<10:
    if j<9:
        average=df["C"+str(j+1)].mean()
        var=df["C"+str(j+1)].std()
        for i in range(len(df)):
            list[j][i]=(list[j][i]-average)/var
    else:
        average=PE_average
        var=PE_var
        for i in range(len(df)):
            list[j][i] = (list[j][i] - average) / var
    j+=1

data=np.mat(list) #用data形成list矩阵
data_mat=data.T   #data_mat用来存data矩阵的转置，这样data_mat就是归一化后的数据矩阵
# print(data_mat[0])
df1=pd.DataFrame(data=data_mat)
df1.to_csv('exp2-3-zscore_data.txt',sep='\t',header=False,index=False)

## 4.	计算协相关矩阵，并画出混淆矩阵。
## 量化体育成绩，bad在60~69随机，general在70~79随机，good在80~89随机，excellent在90~99随机，将C6~C9的成绩乘10

list1=[]  #二维矩阵存放数据源的每一列成绩
list1.append(df.C1.tolist())
list1.append(df.C2.tolist())
list1.append(df.C3.tolist())
list1.append(df.C4.tolist())
list1.append(df.C5.tolist())
list1.append(list(map(lambda x:x*10,df.C6.tolist())))
list1.append(list(map(lambda x:x*10,df.C7.tolist())))
list1.append(list(map(lambda x:x*10,df.C8.tolist())))
list1.append(list(map(lambda x:x*10,df.C9.tolist())))
PE_list=[]
for i in range(len(df)):
    if df.Constitution[i] == "bad":
        j=random.randint(60,69)
        PE_list.append(j)
    elif df.Constitution[i] == "general":
        j = random.randint(70, 79)
        PE_list.append(j)
    elif df.Constitution[i] == "good":
        j = random.randint(80, 89)
        PE_list.append(j)
    elif df.Constitution[i] == "excellent":
        j = random.randint(90, 99)
        PE_list.append(j)
list1.append(PE_list)
data1=np.mat(list1)   #data1用来存放list1矩阵
data1_mat=data1.T #data1转置就可以得到行表示学生，列表示成绩的矩阵
list_avg=[]   #存放每个学生的成绩平均值
for i in range(len(data1_mat)):
    sum=0 #一个学生的成绩和
    for j in range(10):
        sum+=data1_mat[i,j]
    list_avg.append(sum/10.0)
# print(len(list_avg))

list_var=[]   #每个学生成绩的标准差
for i in range(len(data1_mat)):
    sum=0 #一个学生的成绩-平均值然后平方，最后所有项求和
    for j in range(10):
        sum+=((data1_mat[i,j]-list_avg[i])**2)
    list_var.append(np.sqrt(sum/9.0))
# print(list_var)
cor_mat=np.mat(np.zeros((len(data1_mat),len(data1_mat)))) #先生成一个以学生数量为阶的全0方阵，之后替换里面元素变为相关矩阵
# print(len(cor_mat[0]))

def corvar(i,j):
#计算两个学生即两行的协方差
#运用公式cov（x，y）=E[（x-E（x)*(y-E(y))]
    stu1=[]   #存放第i行的成绩-其对应平均值的列表
    stu2=[]   #存放第j行的成绩-其对应平均值的列表
    for k in range(10):
        stu1.append(data1_mat[i,k]-list_avg[i])
        stu2.append(data1_mat[j,k]-list_avg[j])
    sum=0 #stu1和stu2元素按照下标对应相乘后加起来
    for k in range(10):
        sum+=stu1[k]*stu2[k]
    # print(stu1)
    # print(stu2)
    return sum/9.0    #返回协方差
# t=corvar(0,1)
# cor_mat[0,1]=t/(list_var[0]*list_var[1])
for i in range(len(data1_mat)):
    for j in range(len(data1_mat)):
        t=corvar(i,j)
        # print(t)
        cor_mat[i,j]=t/(list_var[i]*list_var[j])  #cor_mat[i,j]表示第i行第j行的相关系数
# print(cor_mat)
# df2=pd.DataFrame(data=cor_mat)
# df2.to_csv('exp2-5-Correlation Matrix.csv',sep=',',header=False,index=False)
plt.figure(figsize=(20,20),dpi=80)
sns.heatmap(cor_mat,vmin=-1,vmax=1,linewidths=0.08,xticklabels=False,cmap='coolwarm') #可视化相关矩阵，用热点图
plt.savefig('exp2-4-heatmap.png',dpi=100,bbox_inches='tight')
plt.show()

#
#
# ## 5.	根据协相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔。
a=copy.deepcopy(cor_mat)
# b=np.argsort(a[0],axis=1)
# print(b[0,len(a)-2])
# print(a[0,b[0,len(a)-2]])
# print(b)
# print(a[0])
maxlist=[]
id=[]
for i in range(len(a)):
    p=[]
    l=[]
    b=np.argsort(a[i],axis=1)
    p.append(a[i,b[0,len(a)-2]])
    p.append(a[i, b[0, len(a) - 3]])
    p.append(a[i, b[0, len(a) - 4]])
    maxlist.append(p)
    l.append(df.ID[b[0,len(a)-2]])
    l.append(df.ID[b[0, len(a) - 3]])
    l.append(df.ID[b[0, len(a) - 4]])
    id.append(l)
# print(maxlist)
id_mat=np.mat(id)
# print(id_mat)
dfid=pd.DataFrame(data=id_mat)
print(dfid)
dfid.to_csv('exp2-5-id_distance.txt',sep='\t',index=False,header=False)
