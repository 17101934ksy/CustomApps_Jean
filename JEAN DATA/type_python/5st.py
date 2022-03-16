import pickle


"""
5st.py:
이 코드는
와이드 , 테이퍼드 , 슬림을 구분해주는 경계값을 해시태그로 구분된 데이터로 검증하는 단계입니다.
len(해시태그로 구분한 분류값 == 바지 사이즈로 구분한 분류값) / len(해시태그로 구분한 분류값) : 정확도
"""



with open("../pickle/dicting.pickle","rb") as f5:
    data1 = pickle.load(f5)

with open("../pickle/boundary.pickle","rb") as f1:
    data2 = pickle.load(f1)

a=data2[0]+0.01
b=data2[1]+0.01


count=0
for i in data1:
    if ((a<=i[2]) and (i[1]==1)):
        count+=1
    elif ((b<=i[2]<a) and (i[1]==2)):
        count+=1
    elif ((i[2]<b) and (i[1]==3)):
        count +=1
        
print("정확도는 :" , count/len(data1))
        