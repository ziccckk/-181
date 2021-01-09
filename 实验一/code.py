import pandas as pd
import random
import csv


df1=pd.read_csv('txt表1.csv')
df1['C10']=df1['C10'].fillna(0)
Gender=df1['Gender'].tolist()
# print(df1)
Gender_new=[]
for i in Gender:
    if i=='female':
        Gender_new.append('girl')
    if i=='male':
        Gender_new.append('boy')
    if i=='boy':
        Gender_new.append('boy')
    if i=='girl':
        Gender_new.append('girl')

df1['Gender']=Gender_new
df1['Height']=df1['Height'].apply(lambda x:float(x*100))
df1['ID']=df1['ID'].apply(lambda x:str(x))

df2=pd.read_excel('数据库表1.xlsx')
df2['C10']=df2['C10'].fillna(0)
def f(x):
    if x<10:
        return '20200'+str(x)
    elif x>=100:
        return '202'+str(x)
    else:
        return '2020'+str(x)

df2['ID']=df2['ID'].apply(f)
df3=pd.merge(df1,df2,how='outer').drop_duplicates(subset=['ID']).sort_values('ID')
# df3=pd.concat([df1,df2],axis=0)
# df3.to_csv('临时文件2.csv')
# # df3=df3.sort_values('ID')
# df3_dropna=df3.dropna(axis=0)
# df3_unique=df3.drop_duplicates(subset=['ID'],keep=False)
# # df3=df3.dropna(axis=0)
# df3=pd.concat([df3_dropna,df3_unique],axis=0).drop_duplicates(subset=['ID']).sort_values('ID')
df3['Height']=df3['Height'].apply(lambda x:int(x/100) if x>1000 else x)
df3['Constitution']=df3['Constitution'].fillna('bad')
df3['C1'].fillna(df3['C1'].mean(),inplace=True)
df3['C2'].fillna(df3['C2'].mean(),inplace=True)
df3['C3'].fillna(df3['C3'].mean(),inplace=True)
df3['C4'].fillna(df3['C4'].mean(),inplace=True)
df3['C5'].fillna(df3['C5'].mean(),inplace=True)
df3['C6'].fillna(df3['C6'].mean(),inplace=True)
df3['C7'].fillna(df3['C7'].mean(),inplace=True)
df3['C8'].fillna(df3['C8'].mean(),inplace=True)
df3['C9'].fillna(df3['C9'].mean(),inplace=True)
df3['C10'].fillna(df3['C10'].mean(),inplace=True)
df3['Height'].fillna(df3['Height'].mean(),inplace=True)



#

#问题1、2
df3.to_csv('合并数据.csv')
# print(df3_unique)
# print(df3_dropna)
print(df3)
df=pd.read_csv('合并数据.csv',encoding='gbk')
# print(df)
df1=df[(df['City'])=='Beijing']
df2=df[(df['City']=='Guangzhou')&(df['C1']>=80)&(df['C10']>=9)&(df['Gender']=='boy')].shape[0]

# print(df1)
C1_mean=df1['C1'].mean()
C2_mean=df1['C2'].mean()
C3_mean=df1['C3'].mean()
C4_mean=df1['C4'].mean()
C5_mean=df1['C5'].mean()
C6_mean=df1['C6'].mean()
C7_mean=df1['C7'].mean()
C8_mean=df1['C8'].mean()
C9_mean=df1['C9'].mean()
C10_mean=df1['C10'].mean()

问题3、4
df=pd.read_csv('合并数据.csv',encoding='gbk')
# print(df)
df1=df[(df['City'])=='Beijing']
df2=df[(df['City']=='Guangzhou')&(df['C1']>=80)&(df['C10']>=9)&(df['Gender']=='boy')].shape[0]

# print(df1)
C1_mean=df1['C1'].mean()
C2_mean=df1['C2'].mean()
C3_mean=df1['C3'].mean()
C4_mean=df1['C4'].mean()
C5_mean=df1['C5'].mean()
C6_mean=df1['C6'].mean()
C7_mean=df1['C7'].mean()
C8_mean=df1['C8'].mean()
C9_mean=df1['C9'].mean()
C10_mean=df1['C10'].mean()
print('北京学生C1课程平均成绩 % .2f'% C1_mean)
print('北京学生C2课程平均成绩 %.2f'% C2_mean)
print('北京学生C3课程平均成绩 % .2f'% C3_mean)
print('北京学生C4课程平均成绩 % .2f'% C4_mean)
print('北京学生C5课程平均成绩 % .2f'% C5_mean)
print('北京学生C6课程平均成绩 % .2f'% C6_mean)
print('北京学生C7课程平均成绩 % .2f'% C7_mean)
print('北京学生C8课程平均成绩 % .2f'% C8_mean)
print('北京学生C9课程平均成绩 % .2f'% C9_mean)
print('北京学生C10课程平均成绩 % .2f'% C10_mean)
print('广州男学生C1成绩80分以上并且C10成绩9分以上数量为%.2f'%df2)
