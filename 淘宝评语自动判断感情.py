

unknown_list=[]
while True:
    a=input("输入评价：")
    p=["好用","好看","好","棒","夸","完美","喜欢","吹爆","强","喜欢","支持","满意","高端"]
    c=["他妈的","没谁了","全世界也是没谁了"]
    n=["妈的","狗屎","我吐了","傻","破","垃圾","不好","我服了","草","死","去死吧","cao","md","劳资","lz","滚","日","你妈","肏","退钱","无良商家","老母","dnmd"]
    degree=["很","太","超级","非常","最","相当","极","真是"]
    pnum=0
    nnum=0
    judge="中性或无法判断"
    for i in p:
        for b in c:
            for m in n:
                if  m in a:
                    for d in degree:
                        if d in a:
                            judge="强负面评价"
                            nnum+=2
                            break
                        else:
                            judge="负面评价"
                            nnum+=1
                else:
                    if i in a:
                        
                        if b in a:
                            judge="强负面评价"
                            nnum+=1                   
                        else:
                            for d in degree:
                                if d in a:
                                    judge="强正面评价"
                                    pnum+=2
                                    break
                                else:
                                    judge="正面评价"
                                    pnum+=1
                            
            
                    
                
                          
    print(judge)
    if judge=="中性或无法判断" :
        if a not in unknown_list:
            unknown_list.append(a)
            print(unknown_list)

    #print("正面指数",pnum)
    #print("负面指数",nnum)

