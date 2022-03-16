import pickle
import json

def checking(x):
    temp=[]
    for i in range(len(x)):
        w=x[i]["tag"][1:].split('#')
        y=x[i]["num"]
        if x[i]["xs"]=='null':
            z=0
        else:
            z=float(x[i]["xs"])
            
        if(w==[''] or (z<=10 or z>=30)):
            if(w==['']):
                result=(y,'',z)
            elif(z<=10):
                result=(y,w,10)
            elif(z>=30):
                result=(y,w,20)
        else:
            result = (y,w,z)
        temp.append(result)
    return temp
        
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
    
    for i in range(1,3): 
        with open('../json/main/product'+str(i)+'.json', 'r', encoding='utf-8') as f1:
            jean=json.load(f1)  
        with open('../pickle/main/pro'+str(i)+'.pickle', 'wb') as f2:
            temp=checking(jean)
            pickle.dump(temp,f2)
        
        with open('../pickle/main/pro'+str(i)+'.pickle','rb') as f3:
            data = pickle.load(f3)
        temp1,temp2,temp3,temp4=[],[],[],[]
        
            
        for ja in range(len(data)):
            result1=padding(data[ja][1])
            result2=maxing(result1)
            result3=estimating(result2)
 
            temp1.append(result3)
            if((result3!=4) and(result3!=5)):
                temp2.append((data[ja][0],result3,data[ja][2]))
                
            if(result3!=5):
                tmp= {1:"와이드", 2:"테이퍼드", 3:"슬림"}.get(result3, "크롭")
                temp3.append((data[ja][0],tmp))
            else:
                temp4.append((data[ja][0],data[ja][2]))
  
            
        with open('../pickle/main/dict'+str(i)+'.pickle','wb') as f4:
            pickle.dump(temp2,f4)
        
        with open('../pickle/main/sort'+str(i)+'.pickle','wb') as f5:
            pickle.dump(temp3,f5)
        
        with open('../pickle/main/unsort'+str(i)+'.pickle','wb') as f6:
            pickle.dump(temp4,f6)
        
        
        
        with open('../pickle/main/unsort'+str(i)+'.pickle','rb') as f1:
            data1 = pickle.load(f1)

        with open('../pickle/boundary.pickle','rb') as f2:
            data2 = pickle.load(f2)

        a,b=data2[0]+0.01 , data2[1]+0.01

        temp=[]
        for jb in data1:
            if (a<=jb[1]):
                temp.append((jb[0],"와이드"))
            elif (b<=jb[1]<a):
                temp.append((jb[0],"테이퍼드"))
            elif (jb[1]<b):
                temp.append((jb[0],"슬림"))

        with open("../pickle/main/addsort"+str(i)+".pickle","wb") as f3:
            pickle.dump(temp,f3)

        with open("../pickle/main/sort"+str(i)+".pickle","rb") as f4:
            data1= pickle.load(f4)

        with open("../pickle/main/addsort"+str(i)+".pickle","rb") as f5:
            data2= pickle.load(f5)

        temp=[]
        for jd in data1:
            temp.append(jd)
        for je in data2:
            temp.append(je)

        with open("../pickle/main/type"+str(i)+".pickle","wb") as f6:
            pickle.dump(temp,f6)
            
    with open("../pickle/main/type1.pickle","rb") as f5:
        data1= pickle.load(f5)
    with open("../pickle/main/type2.pickle","rb") as f5:
        data2= pickle.load(f5)    
        
    for i in range(1,2):
        print(data1[i], "type1 분류 확인")
        
    print("*******************")

    for i in range(1,2):
        print(data2[i], "type2 분류 확인")
        
    print("*******************")

    temp= (data1,data2)
    t=len(data1)+len(data2)
    a,b,c,d=0,0,0,0
    for data in temp:    
        for i in data:
            if i[1]=='와이드':
                a+=1
            elif i[1]=='테이퍼드':
                b+=1
            elif i[1]=='슬림':
                c+=1
            else:
                d+=1

    print("바지분류가 완료되었습니다.")
    print("총바지 개수는",t)
    print("와이드의 개수는:",a)
    print("와이드의 비율은:",a/t)
    print("테이퍼드의 개수는:",b)
    print("테이퍼드의 비율은:",b/t)
    print("슬림의 개수는:",c)
    print("슬림의 비율은:",c/t)
    print("크롭의 개수는:",d)
    print("크롭의 비율은:",d/t)
    
    