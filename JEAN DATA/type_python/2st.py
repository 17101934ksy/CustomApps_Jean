import pickle


"""
2st.py:
이 코드는 바지를 분류하기 위해 
해시태그 인덱스화, 분류된 데이터와 분류할 데이터를 
pickle로 저장하기 위한 코드입니다
"""

def padding(list):
    newlist=[0,0,0,0]
    for i in list:
        if ("부츠컷" in i) or ("와이드" in i)or ("루즈" in i) or ("통" in i) or ("캐주얼" in i) or ("스탠다드" in i) or ("스텐다드" in i) or ("오버" in i) or ("벌룬" in i) or("빅" in i) or ("셀비지" in i) or ("미니멀위크" in i) or ("베이식위크" in i) or ("워시드" in i):
            newlist[0]+=1
        if ("스트레이트" in i) or ("테이퍼드" in i) or ("세미" in i) or ("일자" in i) or ("레귤러" in i) or ("테이퍼드" in i) or ("래귤러" in i) or("스탠다드" in i):
            newlist[1]+=1
        if ("슬림" in i) or ("스키니" in i):
            newlist[2]+=1   
        if ("크롭" in i) or ("커팅" in i) or ("컷팅" in i ) or ("앵클" in i) or ("롤업" in i):
            newlist[3]+=1
    return newlist

def maxing(x):
    y=max(x)
    ylist=[]
    for i in x:
        if(y!=0):
            if(i<y):
                ylist.append(0)
            else:
                ylist.append(1)
        else:
            ylist.append(0)
    return ylist

def estimating(x):
    if (x[0]+x[1]+x[2]+x[3])==1:
        if x[0]==1:
            return 1
        elif x[1]==1:
            return 2
        elif x[2]==1:
            return 3
        else:
            return 4
    else:
        return 5
    
if __name__ == '__main__':
    
    temp1=[]
    temp2=[]
    temp3=[]
    temp4=[]
    temp5=[]
    temp6=[]
    with open("../pickle/data.pickle","rb") as fr:
        data = pickle.load(fr)
        
    for i in range(len(data)):
        result1=padding(data[i][1])
        result2=maxing(result1)
        result3=estimating(result2)
        
        temp1.append(result1)
        temp2.append(result2)
        temp3.append(result3)
        if((result3!=4) and(result3!=5)):
            temp4.append((data[i][0],result3,data[i][2]))
            
        if(result3!=5):
            tmp= {1:"와이드", 2:"테이퍼드", 3:"슬림"}.get(result3, "크롭")
            temp5.append((data[i][0],tmp))
        else:
            temp6.append((data[i][0],data[i][2]))
        
    with open('../pickle/padding.pickle','wb') as f1:
        pickle.dump(temp1,f1)
        
    with open('../pickle/maxing.pickle','wb') as f2:
        pickle.dump(temp2,f2)
        
    with open('../pickle/estimating.pickle','wb') as f3:
        pickle.dump(temp3,f3)
        
    with open('../pickle/dicting.pickle','wb') as f4:
        pickle.dump(temp4,f4)
    
    with open('../pickle/classify.pickle','wb') as f5:
        pickle.dump(temp5,f5)
    
    with open('../pickle/Nonclassify.pickle','wb') as f6:
        pickle.dump(temp6,f6)