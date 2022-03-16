import pickle

"""
3st.py:
이 코드는
2st.py 에서 실행하여 저장한
pickle 파일을 가시적으로 보여주는 코드입니다.
"""


with open("../pickle/data.pickle","rb") as f1:
    data1 = pickle.load(f1)
    
with open("../pickle/padding.pickle","rb") as f2:
    data2 = pickle.load(f2)
    
with open("../pickle/maxing.pickle","rb") as f3:
    data3 = pickle.load(f3)
    
with open("../pickle/estimating.pickle","rb") as f4:
    data4 = pickle.load(f4)
    
with open("../pickle/dicting.pickle","rb") as f5:
    data5 = pickle.load(f5)

with open("../pickle/classify.pickle","rb") as f6:
    data6= pickle.load(f6)

with open("../pickle/Nonclassify.pickle","rb") as f7:
    data7= pickle.load(f7)

    
for i in range(1):
    print(data1[i],"data1")
    print(data2[i],"data2")
    print(data3[i],"data3")
    print(data4[i],"data4")
    print(data5[i],"data5")
    
for i in range(1):
    print(data6[i],"data")

for i in range(1):
    print(data7[i],"nondata")
    
print(len(data6)/len(data1))
print(len(data7)/len(data1))