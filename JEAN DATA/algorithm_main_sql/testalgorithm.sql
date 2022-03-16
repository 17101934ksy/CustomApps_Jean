drop table age;
drop table product;
drop table product_age;
drop table preference;
drop table review;
drop table userinfo;

drop sequence a_seq;
drop table reviewed_of;
drop table reviews;
drop table products_age;
drop table products; 
drop table age;
drop table products_age;
drop table preference;
@C:\Users\USER\Documents\run.sql



create table preference (
"ui" number,
"age" number
);

insert into preference values (10,20);
insert into preference values (11,25);
insert into preference values (12,29);
insert into preference values (13,31);
insert into preference values (14,22);
insert into preference values (15,39);
insert into preference values (16,40);
insert into preference values (17,15);
insert into preference values (18,26);
insert into preference values (19,29);



select p.product_id, 
p.rating w * (select pre.rating from preference )
+ (select pre age 
when          pre. age <= 18 then age1w
when 19 <= pre.age <= 23 then age2w
when 24<= pre.age <= 28 then age3w
when 29<= pre.age <= 33 then age4w
when 34<= pre.age <= 39 then age5w
END AS age6w) * (select 연령별 from preference) 
+p. tpw * (select trend from preference) as total sum 
from products p, preference pre 
where product
order by total sum desc limit 250;


x=나이
if x <18:
result=1
elfi x<24:
result=2
elif x<28:
result=3
elif x<33:
result=4
elif x<39:
result=5
else:
result=6

result 값을 agegroup의 튜플로 넣기


drop table age;
drop table product;
drop table product_age;
drop table preference;
drop table review;
drop table userinfo;
commit;


create table age(
agegroup number(1) primary key
);

create table product(
id number(4) primary key,
ratew number(2,1),
tpw number(2,1)
);

create table userinfo(
ui number primary key,
age number,
agegroup number,
h number,
w number,
foreign key(agegroup) references age(agegroup));



create table preference(
ui number,
agegroup number,
pratew number,
ptpw number,
papw number,
foreign key(ui) references userinfo(ui),
foreign key(agegroup) references age(agegroup),
constraint pk primary key(ui,agegroup)
);

create table product_age(
id number,
agegroup number,
apw number,
constraint p1 primary key(id,agegroup),
foreign key(id) references product(id),
foreign key(agegroup) references age(agegroup));


create table "PRODUCTS_AGE"(
    "PRODUCT_ID" NUMBER(10,0),
    "AGEGROUP" NUMBER(1),
    "APW" NUMBER(2,1),
    CONSTRAINT PID PRIMARY KEY("PRODUCT_ID","AGEGROUP"),
    FOREIGN KEY("PRODUCT_ID") REFERENCES PRODUCTS("PRODUCT_ID"),
    FOREIGN KEY("AGEGROUP") REFERENCES AGE("AGEGROUP")
    );




create table review (
ui number primary key,
id number,
h number,
w number,
rate number,
foreign key(id) references product(id));


commit;

insert into age values (1);
insert into age values (2);
insert into age values (3);
insert into age values (4);
insert into age values (5);
insert into age values (6);
insert into product values (123,0.4,0.2);
insert into product values (124,0.3,0.3);
insert into product values (125,0.3,0.2);
insert into product values (126,0.3,0.4);
insert into product values (127,0.3,0.4);
insert into product values (128,0.2,0.1);


insert into userinfo values (331,26,3,170,50);
insert into userinfo values (332,25,3,170,50);
insert into userinfo values (333,28,3,160,70);
insert into userinfo values (334,28,3,180,50);
insert into userinfo values (335,29,4,190,65);
insert into userinfo values (336,31,4,175,55);
insert into userinfo values (330,21,2,165,60);
insert into userinfo values (319,16,1,160,70);





insert into preference values (331,3,0.5,0.3,0.2);
insert into preference values (330,2,0.3,0.5,0.2);
insert into preference values (319,1,0.2,0.3,0.5);




insert into product_age values(123,1,0.4);
insert into product_age values(123,2,0.3);
insert into product_age values(123,3,0.3);
insert into product_age values(124,4,0.2);
insert into product_age values(124,1,0.2);
insert into product_age values(125,2,0.2);
insert into product_age values(125,3,0.3);
insert into product_age values(126,1,0.3);
insert into product_age values(127,2,0.2);
insert into product_age values(128,3,0.1);




insert into review values (12,128,160,50,4.7);
insert into review values (11,128,170,70,4.8);
insert into review values (13,123,183,70,4.4);
insert into review values (14,123,193,80,4.4);
insert into review values (15,123,185,70,4.3);
insert into review values (1,124,175,60,4.3);
insert into review values (2,124,165,60,4.4);
insert into review values (3,124,170,60,4.5);
insert into review values (4,126,160,70,4.4);
insert into review values (5,125,180,70,4.4);
insert into review values (6,126,180,60,4.5);
insert into review values (7,127,170,80,4.9);
insert into review values (9,128,170,50,4.9);
insert into review values (10,123,165,73,4.9);






select p.ui,p.agegroup from preference p
join age a
on p.agegroup = a.agegroup
join product_age p1
on p1.agegroup=a.agegroup;

select distinct(p.id) from product_age p
join age a
on a.agegroup = p.agegroup
join preference p1
on a.agegroup = p1.agegroup and p1.agegroup=3;


select distinct(p.id) from product_age p
join age a
on a.agegroup = p.agegroup
join preference p1
on a.agegroup = p1.agegroup and p1.agegroup=3;


select distinct(p.id), pa.agegroup, (p.ratew*pr.pratew + p.tpw*pr.ptpw + pa.apw*pr.papw) as weight  from product p
join product_age pa
on pa.id= p.id
join age a
on pa.agegroup = a.agegroup
join preference pr
on pr.agegroup = a.agegroup and pr.ui=331
and rownum<=250 order by weight desc;





select id from product


(select avg(rating) from reviews where height<(select height from uinfo)+5 and height>(selec



select u.ui,u.h,u.w,pa.id , r.h, r.w as s  from userinfo u
join preference pr
on u.ui=pr.ui
join age a
on u.agegroup=a.agegroup
join product_age pa
on pa.agegroup=u.agegroup
join product p
on pa.id=p.id
join review r
on pa.id=r.id and r.h-5<=u.h and u.h<=r.h+5  and r.w-5<=u.w and u.w<=r.w+5;




select avg(1- abs(r.h/r.w)) as np from userinfo u
join preference pr
on u.ui=pr.ui
join age a
on u.agegroup=a.agegroup
join product_age pa
on pa.agegroup=u.agegroup
join product p
on pa.id=p.id
join review r
on pa.id=r.id and r.h-5<=u.h and u.h<=r.h+5  and r.w-5<=u.w and u.w<=r.w+5;




avg(1- abs((r.h/r.w)-(u.h/u.w)))




select distinct(p.id), pa.agegroup, (p.ratew*pr.pratew + p.tpw*pr.ptpw + pa.apw*pr.papw) as weight  from product p
join product_age pa
on pa.id= p.id
join age a
on pa.agegroup = a.agegroup
join preference pr
on pr.agegroup = a.agegroup and pr.ui=331
and rownum<=250 order by weight desc;




select distinct(p.id), pa.agegroup, (p.ratew*pr.pratew + p.tpw*pr.ptpw + pa.apw*pr.papw) as weight  from product p
join product_age pa
on pa.id= p.id
join age a
on pa.agegroup = a.agegroup
join preference pr
on pr.agegroup = a.agegroup and pr.ui=319
and rownum<=250 order by weight desc;

select pa.id, avg(1- abs((r.h/r.w)-(u.h/u.w))) as np from userinfo u
join preference pr
on u.ui=pr.ui
join age a
on u.agegroup=a.agegroup
join product_age pa
on pa.agegroup=u.agegroup
join product p
on pa.id=p.id
join review r
on pa.id=r.id and r.h-5<=u.h and u.h<=r.h+5  and r.w-5<=u.w and u.w<=r.w+5 and u.ui=319
group by pa.id;





select pa.id, avg(1- abs((r.h/r.w)-(u.h/u.w))) as np from userinfo u
p.id in (select distinct(p.id), pa.agegroup, (p.ratew*pr.pratew + p.tpw*pr.ptpw + pa.apw*pr.papw) as weight  from product p
join product_age pa
on pa.id= p.id
join age a
on pa.agegroup = a.agegroup
join preference pr
on pr.agegroup = a.agegroup and pr.ui=331
and rownum<=250 order by weight desc)
join preference pr
on u.ui=pr.ui
join age a
on u.agegroup=a.agegroup
join product_age pa
on pa.agegroup=u.agegroup
join product p
on pa.id=p.id
join review r
on pa.id=r.id and r.h-5<=u.h and u.h<=r.h+5  and r.w-5<=u.w and u.w<=r.w+5 and u.ui=319 
group by pa.id;





create table ex as select distinct(p.id), (p.ratew*pr.pratew + p.tpw*pr.ptpw + pa.apw*pr.papw) as weight  from product p
join product_age pa
on pa.id= p.id
join age a
on pa.agegroup = a.agegroup
join preference pr
on pr.agegroup = a.agegroup and pr.ui=319
and rownum<=250 order by weight desc;
select pa.id, avg(1- abs((r.h/r.w)-(u.h/u.w))) as np from userinfo u
join preference pr
on u.ui=pr.ui
join age a
on u.agegroup=a.agegroup
join product_age pa
on pa.agegroup=u.agegroup
join product p
on pa.id=p.id
join review r
on pa.id=r.id and r.h-5<=u.h and u.h<=r.h+5  and r.w-5<=u.w and u.w<=r.w+5 and u.ui=319
join ex e
on p.id = e.id
group by pa.id;
drop table ex;


create table ex as select distinct(p.id), (p.ratew*pr.pratew + p.tpw*pr.ptpw + pa.apw*pr.papw) as weight  from product p
join product_age pa
on pa.id= p.id
join age a
on pa.agegroup = a.agegroup
join preference pr
on pr.agegroup = a.agegroup and pr.ui=319
and rownum<=250 order by weight desc;






create table ex as select distinct(p.id), (p.ratew*pr.pratew + p.tpw*pr.ptpw + pa.apw*pr.papw) as weight  from product p
join product_age pa
on pa.id= p.id
join age a
on pa.agegroup = a.agegroup
join preference pr
on pr.agegroup = a.agegroup and pr.ui=319
and rownum<=250 order by weight desc;
select pa.id, avg(1- abs((r.h/r.w)-(u.h/u.w))) as np from userinfo u
join preference pr
on u.ui=pr.ui
join age a
on u.agegroup=a.agegroup
join product_age pa
on pa.agegroup=u.agegroup
join product p
on pa.id=p.id
join review r
on pa.id=r.id and r.h-5<=u.h and u.h<=r.h+5  and r.w-5<=u.w and u.w<=r.w+5 and u.ui=319
join ex e
on p.id = e.id
group by pa.id;
drop table ex;