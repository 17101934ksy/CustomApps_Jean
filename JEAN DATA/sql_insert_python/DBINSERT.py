import json
import pickle

with open("../pickle/range/quantile.pickle","rb") as f1:
    data = pickle.load(f1)


f = open("../json/main/product1.json", "r", encoding="utf8")
jeans_json = f.read()
jeans1 = json.loads(jeans_json)
f.close()

f = open("../json/main/review1.json", "r", encoding="utf8")
reviews_json = f.read()
reviews1 = json.loads(reviews_json)
f.close()


f = open("../json/main/product2.json", "r", encoding="utf8")
jeans_json = f.read()
jeans2 = json.loads(jeans_json)
f.close()

f = open("../json/main/review2.json", "r", encoding="utf8")
reviews_json = f.read()
reviews2 = json.loads(reviews_json)
f.close()

f = open("run.sql", "w+", encoding="utf-8")
f.write('''SET DEFINE OFF;
        
CREATE SEQUENCE A_SEQ
  START WITH 100000
  INCREMENT BY 1
  MAXVALUE 999999;

CREATE TABLE "AGE"(
    "AGEGROUP" NUMBER(1) PRIMARY KEY
);


CREATE TABLE "PRODUCTS"(
    "PRODUCT_ID" NUMBER(10,0) PRIMARY KEY,
    "NAME" VARCHAR2(100),
    "HASHTAG" VARCHAR2(200),
    "RATING" NUMBER(2,1),
    "IMAGE" VARCHAR2(200),
    "XS_SIZE" VARCHAR2(10),
    "PURCHASE_TOTAL" VARCHAR2(100),
    "VEIW_TOTAL" VARCHAR2(100),
    "PURCHASE_AGE" VARCHAR2(100),
    "VEIW_AGE" VARCHAR2(100),
    "PRICE" NUMBER(10,0),
    "HEART" NUMBER(7,0),
    "RATEW" NUMBER(2,1),
    "TPW" NUMBER(2,1)D
    );
    
create table "PRODUCTS_AGE"(
    "PRODUCT_ID" NUMBER(10,0),
    "AGEGROUP" NUMBER(1),
    "APW" NUMBER(2,1),
    CONSTRAINT PID PRIMARY KEY("PRODUCT_ID","AGEGROUP"),
    FOREIGN KEY("PRODUCT_ID") REFERENCES PRODUCTS("PRODUCT_ID"),
    FOREIGN KEY("AGEGROUP") REFERENCES AGE("AGEGROUP")
    );
    

CREATE TABLE "REVIEWS"(
    "REVIEW_ID" NUMBER(7,0) PRIMARY KEY,
    "PRODUCT_ID" NUMBER(10,0),
    "NAME" VARCHAR2(100),
    "GENDER" VARCHAR2(10),
    "HEIGHT" NUMBER(4,1),
    "WEIGHT" NUMBER(4,1),
    "RATING" NUMBER(2,1),
    "FIT_SIZE" VARCHAR2(4),
    "EVLS" NUMBER(3,0),
    "EVLB" NUMBER(3,0),
    "EVLC" NUMBER(3,0),
    "EVLT" NUMBER(3,0),
    "LINK" VARCHAR2(1000),
    FOREIGN KEY("PRODUCT_ID") REFERENCES PRODUCTS("PRODUCT_ID")
    );

CREATE TABLE "REVIEWED_OF"(
    "PRODUCT_ID" NUMBER(10,0),
    "REVIEW_ID" NUMBER(7,0),
    FOREIGN KEY("PRODUCT_ID") REFERENCES "PRODUCTS",
    FOREIGN KEY("REVIEW_ID") REFERENCES "REVIEWS"
    );\n''')


def testf(x,listy):
    
    result=0
    if x=='NULL':
        result=0.1
    else:
        x=float(x)
        if x<=listy[0]:
            result=0.1
        elif listy[0]<x<=listy[1]:
            result=0.2
        elif listy[1]<=x<listy[2]:
            result=0.3
        elif listy[2]<=x:
            result=0.4
    return result


f.write(
    f"INSERT INTO AGE (AGEGROUP) VALUES(1);\n")
f.write(
    f"INSERT INTO AGE (AGEGROUP) VALUES(2);\n")
f.write(
    f"INSERT INTO AGE (AGEGROUP) VALUES(3);\n")
f.write(
    f"INSERT INTO AGE (AGEGROUP) VALUES(4);\n")
f.write(
    f"INSERT INTO AGE (AGEGROUP) VALUES(5);\n")
f.write(
    f"INSERT INTO AGE (AGEGROUP) VALUES(6);\n")


jeans = jeans1+jeans2
print(len(jeans1))
print(len(jeans2))
print(len(jeans))

for jean in jeans:
    ap=jean['ap'][1:-1].split(',')
    rate = jean['rate'] if jean['rate'] else 'NULL'
    age1w = testf(ap[0],data[0])
    age2w = testf(ap[1],data[1])
    age3w = testf(ap[2],data[2])
    age4w = testf(ap[3],data[3])
    age5w = testf(ap[4],data[4])
    age6w = testf(ap[5],data[5])
    ratew= testf(rate,data[6])
    tpw = testf(jean['tp'],data[7])
    
    f.write(
        f"INSERT INTO PRODUCTS (PRODUCT_ID,NAME,HASHTAG,RATING,IMAGE,XS_SIZE,PURCHASE_TOTAL,VEIW_TOTAL,PURCHASE_AGE,VEIW_AGE,PRICE,HEART,RATEW,TPW) VALUES({jean['num']},'{jean['name']}','{jean['tag']}',{rate},'{jean['img']}','{jean['xs']}','{jean['tp']}','{jean['tv']}','{jean['ap']}','{jean['av']}',{jean['price']},{jean['heart']},{ratew},{tpw});\n")
    f.write(
        f"INSERT INTO PRODUCTS_AGE (PRODUCT_ID,AGEGROUP,APW) VALUES({jean['num']},{1},{age1w});\n")
    f.write(
        f"INSERT INTO PRODUCTS_AGE (PRODUCT_ID,AGEGROUP,APW) VALUES({jean['num']},{2},{age2w});\n")
    f.write(
        f"INSERT INTO PRODUCTS_AGE (PRODUCT_ID,AGEGROUP,APW) VALUES({jean['num']},{3},{age3w});\n")
    f.write(
        f"INSERT INTO PRODUCTS_AGE (PRODUCT_ID,AGEGROUP,APW) VALUES({jean['num']},{4},{age4w});\n")
    f.write(
        f"INSERT INTO PRODUCTS_AGE (PRODUCT_ID,AGEGROUP,APW) VALUES({jean['num']},{5},{age5w});\n")
    f.write(
        f"INSERT INTO PRODUCTS_AGE (PRODUCT_ID,AGEGROUP,APW) VALUES({jean['num']},{6},{age6w});\n")
    


for review in reviews1:
    f.write(
        f"INSERT INTO REVIEWS (REVIEW_ID,PRODUCT_ID,NAME,GENDER,HEIGHT,WEIGHT,RATING,FIT_SIZE,EVLS,EVLB,EVLC,EVLT,LINK) VALUES(A_SEQ.NEXTVAL,{review['num']},'{review['name']}','{review['gender']}',{review['height']},{review['weight']},{review['rating']},'{review['size']}',{review['evls']},{review['evlb']},{review['evlc']},{review['evlt']},'{'https:'+review['link']}');\n")
    f.write(
        f"INSERT INTO REVIEWED_OF (PRODUCT_ID,REVIEW_ID) VALUES({review['num']},A_SEQ.CURRVAL);\n")



for review in reviews2:
    f.write(
        f"INSERT INTO REVIEWS (REVIEW_ID,PRODUCT_ID,NAME,GENDER,HEIGHT,WEIGHT,RATING,FIT_SIZE,EVLS,EVLB,EVLC,EVLT,LINK) VALUES(A_SEQ.NEXTVAL,{review['num']},'{review['name']}','{review['gender']}',{review['height']},{review['weight']},{review['rating']},'{review['size']}',{review['evls']},{review['evlb']},{review['evlc']},{review['evlt']},'{'https:'+review['link']}');\n")
    f.write(
        f"INSERT INTO REVIEWED_OF (PRODUCT_ID,REVIEW_ID) VALUES({review['num']},A_SEQ.CURRVAL);\n")

f.write('commit;\n')
f.close()

    
