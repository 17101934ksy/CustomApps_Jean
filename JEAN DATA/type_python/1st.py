import json
import pickle

"""
1st.py:
이 코드는 크롤링한 json 파일을 
jean 고유번호, hashtag, jean_xs 사이즈 순서로
pickle 형태로 저장하기 위한 코드입니다.

"""


def checking(x):
    temp=[]
    with open('../pickle/data.pickle', 'wb') as f:
        for i in range(len(x)):
            w=x[i]["jean_hashtag"][1:].split('#')
            y=x[i]["jean_num"]
            z=float(x[i]["jean_xs"])
            if(w==[''] or (z<=10 or z>=30)):
                continue
            else:
                result = (y,w,z)
            temp.append(result)
        pickle.dump(temp,f)
            


if __name__ == '__main__':
        
    with open('../json/jean.json', 'r', encoding='utf-8') as f:
        jean=json.load(f)  
         
    checking(jean)
    
    with open("../pickle/data.pickle","rb") as fr:
        data = pickle.load(fr)
        print(data[3])