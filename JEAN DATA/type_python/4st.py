import pickle


"""
4st.py:
이 코드는
pickle 파일을 받아서 바지 밑단 사이즈로 바지를 분류하기 위해
경계점을 찾는 코드입니다.
"""




def divisioning(data,x1,x2,x3):
    if data[1]==1:
        x1.append(data[2])
    elif data[1]==2:
        x2.append(data[2])
    elif data[1]==3:
        x3.append(data[2])
    


if __name__ == '__main__':
    with open("../pickle/dicting.pickle","rb") as f:
        data = pickle.load(f)
    
    t1,t2,t3=[],[],[]
    for i in range(len(data)):
            divisioning(data[i],t1,t2,t3)
        
    a1=sorted(t1)
    b1=int(round(len(a1)*0.05))
    
    a2=sorted(t2)
    b2=int(round(len(a2)*0.05))
    a3=sorted(t3)
    b3=int(round(len(a3)*0.05))

    t1,t2,t3=[],[],[]
    
    print(b1,b2,b3)
    for i in range(b1,len(a1)-b1):
        t1.append(a1[i])
    for i in range(b2,len(a2)-b2):
        t2.append(a2[i])
    for i in range(b3,len(a3)-b3):
        t3.append(a3[i])
        
    a1=min(t1)
    a2=max(t2)
    b1=min(t2)
    b2=max(t3)
    tmp1,tmp2,tmp3,tmp4=[],[],[],[]
    for i in t1:
        if i<a2:
            tmp1.append(i)
            tmp3.append(i)
    for i in t2:
        if i>a1:
            tmp2.append(i)
            tmp3.append(i)
    
    tep3=sorted(tmp3)
    count1,count=0,0
    for i in tep3:
        for j in tmp1:
            if j<i+0.01:
                count+=1
        for k in tmp2:
            if i+0.01<k:
                count+=1
        if count1>=count:
            tmp4.append((i,count))
        count1=count
        count=0
    
    tmp4.sort(key=lambda x:x[1])
    print("와이드와 테이퍼드 경계:",tmp4[0][0])
    storage1 = tmp4[0][0]
    
    tmp1,tmp2,tmp3,tmp4=[],[],[],[]
    for i in t2:
        if i<b2:
            tmp1.append(i)
            tmp3.append(i)
    for i in t3:
        if i>b1:
            tmp2.append(i)
            tmp3.append(i)
    
    tep3=sorted(tmp3)
    count1,count=0,0
    for i in tep3:
        for j in tmp1:
            if j<i+0.01:
                count+=1
        for k in tmp2:
            if i+0.01<k:
                count+=1
        if count1>=count:
            tmp4.append((i,count))
        count1=count
        count=0
    
    tmp4.sort(key=lambda x:x[1])
    print("테이퍼드와 슬림의 경계:",tmp4[0][0])
    
    storage2 = tmp4[0][0]
    result = (storage1, storage2)
    with open('../pickle/boundary.pickle','wb') as f1:
        pickle.dump(result,f1)
    