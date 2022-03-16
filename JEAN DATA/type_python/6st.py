import pickle


"""
6st.py:
이 코드는
분류가 되지 않은 바지를 경게값을 통해 분류하는 단계코드입니다.
그 후, 분류된 데이터들을 하나의 파일로 합치는 코드입니다.
"""



with open("../pickle/Nonclassify.pickle","rb") as f1:
    data1 = pickle.load(f1)

with open("../pickle/boundary.pickle","rb") as f2:
    data2 = pickle.load(f2)


a=data2[0]+0.01
b=data2[1]+0.01


temp=[]
for i in data1:
    if (a<=i[1]):
        temp.append((i[0],"와이드"))
    elif (b<=i[1]<a):
        temp.append((i[0],"테이퍼드"))
    elif (i[1]<b):
        temp.append((i[0],"슬림"))
        
for i in range(10):
    print(temp[i])

with open("../pickle/classify2.pickle","wb") as f3:
    pickle.dump(temp,f3)

with open("../pickle/classify.pickle","rb") as f4:
    data1= pickle.load(f4)

with open("../pickle/classify2.pickle","rb") as f5:
    data2= pickle.load(f5)

temp=[]
for i in data1:
    temp.append(i)
for i in data2:
    temp.append(i)

with open("../pickle/temptype.pickle","wb") as f6:
    pickle.dump(temp,f6)