import json
import csv
json_file="/home/gcy/下载/python结巴分词+云图绘制/可视化工具/vaccini-italia-covid/covid19-opendata-vaccini/dati/somministrazioni-vaccini-latest.json"
#json无非是列表和字典数据结构的结合 所以无需害怕，用循环进行写入即可:
# 外层是字典，则用dict.keys()和dict.values()来分离，然后用list（）方法放到列表中就好处置了 
def csv_json():
    # 1.分别 读，创建文件
    json_fp = open(json_file, "r")
    csv_fp = open("csv_file.csv", "w")

    # 2.提出表头和表的内容
    data_list = json.load(json_fp)
    data_list1=data_list.values()#json最外层的values共两个，并装进列表中
    data_list2=list(data_list1)#两个values装进列表
    data_list3=data_list2[0]#取第一个value，得到二级字典
    data_list4=data_list3.values()#第二层字典的values，这次有三个元素
    data_list5=list(data_list4)#来自字典的元素们需要装进列表；而本来在列表中的字典元素可以自由提取
    data_list6=data_list5[0]#取第一个元素，是一个列表！这是最后一次分解，以后会简化步骤了！
    data_list7=data_list6[2]
    title=[]
    for i in data_list6:
        title.append(list(i.values())[0])#这里比较复杂，先提取values，再装入list，再取list中的第一个，将其加入title列表
    values1=data_list2[1]
    content=[]
    for i in values1:
        content.append(list(i.values()))
    #print(content)#打印数据

    # 3.csv 写入器
    writer = csv.writer(csv_fp)
    # 4.写入表头
    writer.writerow(title)
    # 5.写入内容
    writer.writerows(content)
    # 6.关闭两个文件"""
    json_fp.close()
    csv_fp.close()



#if __name__ == "__main__"用处：避免被其他python程序调用执行，也自动在这个文件中执行上面的函数 只有同一个文件才能执行
if __name__ == "__main__":
    csv_json()
   
