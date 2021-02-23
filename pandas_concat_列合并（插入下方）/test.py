#主要用到的是concat合并功能！



from os import linesep
import pandas as pd
from pandas.io.parsers import read_csv
data=pd.read_csv("删减.csv")
df=pd.DataFrame(data)
with open("删减.csv","r",encoding="utf-8") as f:
    dt=read_csv(f)

#print(df)
#print(data2["id"])
list=[]

#print(result)
#result.to_csv("final.csv", index=False, sep=' ') 
#print(df.head)
for i in dt:
    list.append(i)
list1=list[0:180]
print(list1)
"""for i in list1:
    a=data[i]
    result = pd.concat([a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a])"""
fuck=pd.DataFrame()
print(fuck)
for i in list1:
    a=data[i]
    fuck[i]=pd.concat([a,a,a,a,a,a,a,a,a,a,a])
B6_1_=[]
B6_2_=[]
B6_3_=[]
B6_4_=[]
B6_5_=[]
B6_6_=[]
B6_7_=[]
B6_8_=[]
B6_9_=[]
B6_10_=[]
B6_11_=[]
for i in list:
    if "B6_1_" in i:
        B6_1_.append("data["+i+"]")
    elif "B6_2_" in i:
        B6_2_.append("data["+i+"]")
    elif "B6_3_" in i:
        B6_3_.append("data["+i+"]")
    elif "B6_4_" in i:
        B6_4_.append("data["+i+"]")
    elif "B6_5_" in i:
        B6_5_.append("data["+i+"]")
    elif "B6_6_" in i:
        B6_6_.append("data["+i+"]")
    elif "B6_7_" in i:
        B6_7_.append("data["+i+"]")
    elif "B6_8_" in i:
        B6_8_.append("data["+i+"]")
    elif "B6_9_" in i:
        B6_9_.append("data["+i+"]")
    elif "B6_10_" in i:
        B6_10_.append("data["+i+"]")
    elif "B6_11_" in i:
        B6_11_.append("data["+i+"]")
    
#print(B6_11_)
list_all=[B6_1_,B6_2_,B6_3_,B6_4_,B6_5_,B6_6_,B6_7_,B6_8_,B6_9_,B6_10_,B6_11_]
#fuck.index=[i+1 for i in range(3726)]


print(list)
fuck["B6_1_"]=pd.concat([
    data['B6_1_1'],data['B6_2_1'],data['B6_3_1'],data['B6_4_1'],data['B6_5_1'],data['B6_6_1'],data['B6_7_1'],data['B6_8_1'],data['B6_9_1'],data['B6_10_1'],data['B6_11_1']
    ])
fuck["B6_2_"]=pd.concat([
data['B6_1_2'],data['B6_2_2'],data['B6_3_2'],data['B6_4_2'],data['B6_5_2'],data['B6_6_2'],data['B6_7_2'],data['B6_8_2'],data['B6_9_2'],data['B6_10_2'],data['B6_11_2']

    ])
fuck["B6_3_"]=pd.concat([data['B6_1_3'],data['B6_2_3'],data['B6_3_3'],data['B6_4_3'],data['B6_5_3'],data['B6_6_3'],data['B6_7_3'],data['B6_8_3'],data['B6_9_3'],data['B6_10_3'],data['B6_11_3']

    ])
fuck["B6_4_"]=pd.concat([data['B6_1_4'],data['B6_2_4'],data['B6_3_4'],data['B6_4_4'],data['B6_5_4'],data['B6_6_4'],data['B6_7_4'],data['B6_8_4'],data['B6_9_4'],data['B6_10_4'],data['B6_11_4']

    ])
fuck["B6_5_"]=pd.concat([data['B6_1_5'],data['B6_2_5'],data['B6_3_5'],data['B6_4_5'],data['B6_5_5'],data['B6_6_5'],data['B6_7_5'],data['B6_8_5'],data['B6_9_5'],data['B6_10_5'],data['B6_11_5']

    ])
fuck["B6_6_"]=pd.concat([data['B6_1_6'],data['B6_2_6'],data['B6_3_6'],data['B6_4_6'],data['B6_5_6'],data['B6_6_6'],data['B6_7_6'],data['B6_8_6'],data['B6_9_6'],data['B6_10_6'],data['B6_11_6']

    ])
fuck["B6_7_"]=pd.concat([data['B6_1_7'],data['B6_2_7'],data['B6_3_7'],data['B6_4_7'],data['B6_5_7'],data['B6_6_7'],data['B6_7_7'],data['B6_8_7'],data['B6_9_7'],data['B6_10_7'],data['B6_11_7']

    ])
fuck["B6_8_"]=pd.concat([data['B6_1_8'],data['B6_2_8'],data['B6_3_8'],data['B6_4_8'],data['B6_5_8'],data['B6_6_8'],data['B6_7_8'],data['B6_8_8'],data['B6_9_8'],data['B6_10_8'],data['B6_11_8']

    ])
fuck["B6_9_"]=pd.concat([data['B6_1_9'],data['B6_2_9'],data['B6_3_9'],data['B6_4_9'],data['B6_5_9'],data['B6_6_9'],data['B6_7_9'],data['B6_8_9'],data['B6_9_9'],data['B6_10_9'],data['B6_11_9']

    ])
fuck["B6_10_"]=pd.concat([data['B6_1_10'],data['B6_2_10'],data['B6_3_10'],data['B6_4_10'],data['B6_5_10'],data['B6_6_10'],data['B6_7_10'],data['B6_8_10'],data['B6_9_10'],data['B6_10_10'],data['B6_11_10']

    ])
fuck["B6_11_"]=pd.concat([data['B6_1_11'],data['B6_2_11'],data['B6_3_11'],data['B6_4_11'],data['B6_5_11'],data['B6_6_11'],data['B6_7_11'],data['B6_8_11'],data['B6_9_11'],data['B6_10_11'],data['B6_11_11']

    ])
fuck["B6_12_"]=pd.concat([data['B6_1_12'],data['B6_2_12'],data['B6_3_12'],data['B6_4_12'],data['B6_5_12'],data['B6_6_12'],data['B6_7_12'],data['B6_8_12'],data['B6_9_12'],data['B6_10_12'],data['B6_11_12']

    ])
fuck["B6_13_"]=pd.concat([data['B6_1_13'],data['B6_2_13'],data['B6_3_13'],data['B6_4_13'],data['B6_5_13'],data['B6_6_13'],data['B6_7_13'],data['B6_8_13'],data['B6_9_13'],data['B6_10_13'],data['B6_11_13']

    ])
fuck["B6_14_"]=pd.concat([data['B6_1_14'],data['B6_2_14'],data['B6_3_14'],data['B6_4_14'],data['B6_5_14'],data['B6_6_14'],data['B6_7_14'],data['B6_8_14'],data['B6_9_14'],data['B6_10_14'],data['B6_11_14']

    ])
fuck["B6_15_"]=pd.concat([data['B6_1_15'],data['B6_2_15'],data['B6_3_15'],data['B6_4_15'],data['B6_5_15'],data['B6_6_15'],data['B6_7_15'],data['B6_8_15'],data['B6_9_15'],data['B6_10_15'],data['B6_11_15']

    ])
fuck["B6_16_"]=pd.concat([data['B6_1_16'],data['B6_2_16'],data['B6_3_16'],data['B6_4_16'],data['B6_5_16'],data['B6_6_16'],data['B6_7_16'],data['B6_8_16'],data['B6_9_16'],data['B6_10_16'],data['B6_11_16']

    ])
fuck["B6_17_"]=pd.concat([data['B6_1_17'],data['B6_2_17'],data['B6_3_17'],data['B6_4_17'],data['B6_5_17'],data['B6_6_17'],data['B6_7_17'],data['B6_8_17'],data['B6_9_17'],data['B6_10_17'],data['B6_11_17']

    ])
fuck["B6_18_"]=pd.concat([data['B6_1_18'],data['B6_2_18'],data['B6_3_18'],data['B6_4_18'],data['B6_5_18'],data['B6_6_18'],data['B6_7_18'],data['B6_8_18'],data['B6_9_18'],data['B6_10_18'],data['B6_11_18']

    ])
fuck["B6_19_"]=pd.concat([data['B6_1_19'],data['B6_2_19'],data['B6_3_19'],data['B6_4_19'],data['B6_5_19'],data['B6_6_19'],data['B6_7_19'],data['B6_8_19'],data['B6_9_19'],data['B6_10_19'],data['B6_11_19']

    ])
fuck["B6_20_"]=pd.concat([data['B6_1_20'],data['B6_2_20'],data['B6_3_20'],data['B6_4_20'],data['B6_5_20'],data['B6_6_20'],data['B6_7_20'],data['B6_8_20'],data['B6_9_20'],data['B6_10_20'],data['B6_11_20']

    ])
fuck["B6_21_"]=pd.concat([data['B6_1_21'],data['B6_2_21'],data['B6_3_21'],data['B6_4_21'],data['B6_5_21'],data['B6_6_21'],data['B6_7_21'],data['B6_8_21'],data['B6_9_21'],data['B6_10_21'],data['B6_11_21']

    ])
fuck["B6_22_"]=pd.concat([data['B6_1_22'],data['B6_2_22'],data['B6_3_22'],data['B6_4_22'],data['B6_5_22'],data['B6_6_22'],data['B6_7_22'],data['B6_8_22'],data['B6_9_22'],data['B6_10_22'],data['B6_11_22']

    ])
fuck["B6_23_"]=pd.concat([data['B6_1_23'],data['B6_2_23'],data['B6_3_23'],data['B6_4_23'],data['B6_5_23'],data['B6_6_23'],data['B6_7_23'],data['B6_8_23'],data['B6_9_23'],data['B6_10_23'],data['B6_11_23']

    ])
fuck["B6_24_"]=pd.concat([data['B6_1_24'],data['B6_2_24'],data['B6_3_24'],data['B6_4_24'],data['B6_5_24'],data['B6_6_24'],data['B6_7_24'],data['B6_8_24'],data['B6_9_24'],data['B6_10_24'],data['B6_11_24']

    ])
fuck["B6_25_"]=pd.concat([data['B6_1_25'],data['B6_2_25'],data['B6_3_25'],data['B6_4_25'],data['B6_5_25'],data['B6_6_25'],data['B6_7_25'],data['B6_8_25'],data['B6_9_25'],data['B6_10_25'],data['B6_11_25']

    ])

fuck.to_csv("final.csv",sep=',') 
