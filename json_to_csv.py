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
#以下为适应的数据结构
 """{
    "schema":{
        "fields":[
            {
                "name":"index",
                "type":"integer"
            },
            {
                "name":"fascia_anagrafica",
                "type":"string"
            },
            {
                "name":"totale",
                "type":"integer"
            },
            {
                "name":"sesso_maschile",
                "type":"integer"
            },
            {
                "name":"sesso_femminile",
                "type":"integer"
            },
            {
                "name":"categoria_operatori_sanitari_sociosanitari",
                "type":"integer"
            },
            {
                "name":"categoria_personale_non_sanitario",
                "type":"integer"
            },
            {
                "name":"categoria_ospiti_rsa",
                "type":"integer"
            },
            {
                "name":"categoria_over80",
                "type":"integer"
            },
            {
                "name":"prima_dose",
                "type":"integer"
            },
            {
                "name":"seconda_dose",
                "type":"integer"
            },
            {
                "name":"ultimo_aggiornamento",
                "type":"datetime"
            }
        ],
        "primaryKey":[
            "index"
        ],
        "pandas_version":"0.20.0"
    },
    "data":[
        {
            "index":0,
            "fascia_anagrafica":"16-19",
            "totale":3545,
            "sesso_maschile":1571,
            "sesso_femminile":1974,
            "categoria_operatori_sanitari_sociosanitari":2202,
            "categoria_personale_non_sanitario":974,
            "categoria_ospiti_rsa":369,
            "categoria_over80":0,
            "prima_dose":2249,
            "seconda_dose":1296,
            "ultimo_aggiornamento":"2021-02-19T00:00:00.000Z"
        },
        {
            "index":1,
            "fascia_anagrafica":"20-29",
            "totale":339723,
            "sesso_maschile":114831,
            "sesso_femminile":224892,
            "categoria_operatori_sanitari_sociosanitari":273992,
            "categoria_personale_non_sanitario":62255,
            "categoria_ospiti_rsa":3476,
            "categoria_over80":0,
            "prima_dose":205210,
            "seconda_dose":134513,
            "ultimo_aggiornamento":"2021-02-19T00:00:00.000Z"
        },
        {
            "index":2,
            "fascia_anagrafica":"30-39",
            "totale":491485,
            "sesso_maschile":189950,
            "sesso_femminile":301535,
            "categoria_operatori_sanitari_sociosanitari":390160,
            "categoria_personale_non_sanitario":96474,
            "categoria_ospiti_rsa":4851,
            "categoria_over80":0,
            "prima_dose":288452,
            "seconda_dose":203033,
            "ultimo_aggiornamento":"2021-02-19T00:00:00.000Z"
        },
        {
            "index":3,
            "fascia_anagrafica":"40-49",
            "totale":613123,
            "sesso_maschile":201308,
            "sesso_femminile":411815,
            "categoria_operatori_sanitari_sociosanitari":458554,
            "categoria_personale_non_sanitario":146472,
            "categoria_ospiti_rsa":8097,
            "categoria_over80":0,
            "prima_dose":359185,
            "seconda_dose":253938,
            "ultimo_aggiornamento":"2021-02-19T00:00:00.000Z"
        },
        {
            "index":4,
            "fascia_anagrafica":"50-59",
            "totale":797109,
            "sesso_maschile":262131,
            "sesso_femminile":534978,
            "categoria_operatori_sanitari_sociosanitari":586495,
            "categoria_personale_non_sanitario":194615,
            "categoria_ospiti_rsa":15999,
            "categoria_over80":0,
            "prima_dose":455191,
            "seconda_dose":341918,
            "ultimo_aggiornamento":"2021-02-19T00:00:00.000Z"
        },
        {
            "index":5,
            "fascia_anagrafica":"60-69",
            "totale":491402,
            "sesso_maschile":248198,
            "sesso_femminile":243204,
            "categoria_operatori_sanitari_sociosanitari":370836,
            "categoria_personale_non_sanitario":95876,
            "categoria_ospiti_rsa":24690,
            "categoria_over80":0,
            "prima_dose":278496,
            "seconda_dose":212906,
            "ultimo_aggiornamento":"2021-02-19T00:00:00.000Z"
        },
        {
            "index":6,
            "fascia_anagrafica":"70-79",
            "totale":126479,
            "sesso_maschile":78842,
            "sesso_femminile":47637,
            "categoria_operatori_sanitari_sociosanitari":56301,
            "categoria_personale_non_sanitario":20561,
            "categoria_ospiti_rsa":49617,
            "categoria_over80":0,
            "prima_dose":78087,
            "seconda_dose":48392,
            "ultimo_aggiornamento":"2021-02-19T00:00:00.000Z"
        },
        {
            "index":7,
            "fascia_anagrafica":"80-89",
            "totale":286612,
            "sesso_maschile":106653,
            "sesso_femminile":179959,
            "categoria_operatori_sanitari_sociosanitari":7620,
            "categoria_personale_non_sanitario":12944,
            "categoria_ospiti_rsa":129655,
            "categoria_over80":136393,
            "prima_dose":218497,
            "seconda_dose":68115,
            "ultimo_aggiornamento":"2021-02-19T00:00:00.000Z"
        },
        {
            "index":8,
            "fascia_anagrafica":"90+",
            "totale":149235,
            "sesso_maschile":28023,
            "sesso_femminile":121212,
            "categoria_operatori_sanitari_sociosanitari":1148,
            "categoria_personale_non_sanitario":4897,
            "categoria_ospiti_rsa":117614,
            "categoria_over80":25576,
            "prima_dose":96116,
            "seconda_dose":53119,
            "ultimo_aggiornamento":"2021-02-19T00:00:00.000Z"
        }
    ]
}"""
