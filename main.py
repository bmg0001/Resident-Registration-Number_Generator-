import re
import os

dic = {"서울":"00-08", "부산":"09-12", "인천":"13-15", "경기도":"16-25", "강원도":"26-34", "충북":"35-39", "대전":"40-40", "세종":"44-44",
       "충남":"41-43", "전북":"48-54", "전남":"55-56", "대구":"67-70", "경상북도":"71-81", "경상남도":"82-90", "울산":"85-85", "제주":"91-95"}

print("=" * 50)
print("{0:^40}".format("주민번호 생성 프로그램"))
print("=" * 50)

gender = input("성별 (남, 여) > ")
code = input("생년월일 (ex>980803) > ")
print("-" * 50)
print("서울 부산 인천 경기도 강원도 충북 대전 세종 충남 전북")
print("{0:^40}".format("전남 대구 경상남도 경상북도 울산 제주"))
print("{0:^50}".format("출생지역 목록"))
print("-" * 50)
loc = input("출생지역 > ")

chk = re.compile("\d{6}")
if not chk.match(code):
    print("생년월일 입력이 잘못 되었습니다.")
    exit(-1)

data = code + "-"
if gender == "남":
    if int(code[:2]) >= 0 and int(code[:2]) <= 18:
        data = data + "3"
    else:
        data = data + "1"
else:
    if int(code[:2]) >= 0 and int(code[:2]) <= 18:
        data = data + "4"
    else:
        data = data + "2"

fp = open("LIST.txt", "w")
fp.write("="*50+"\n")
fp.write("{0:^40}\n".format("주민번호 생성 프로그램"))
fp.write("="*50+"\n")
fp.write("성별 (남, 여) > "+gender+"\n")
fp.write("생년월일 (ex>980803) > "+code+"\n")
fp.write("출생지역 > "+loc+"\n")
fp.write("="*50+"\n")

cnt=0
for i in list(range(int(dic.get(loc).split("-")[0]), int(dic.get(loc).split("-")[1])+1)):
    newdata = data
    newdata = data+str(i)
    tmp = newdata
    for j in list(range(0, 10000)):
        tmp = newdata + str("{0:0>4}".format(j))
        front = tmp.split("-")[0]
        end = tmp.split("-")[1]
        M = 11 - (((int(front[:1])*2 + int(front[1:2])*3 + int(front[2:3])*4 + int(front[3:4])*5 + int(front[4:5])*6 + int(front[5:6])*7
                    +int(end[:1])*8 + int(end[1:2])*9 + int(end[2:3])*2 + int(end[3:4])*3 + int(end[4:5])*4 + int(end[5:6])*5)%11)%10)
        if str(M) == end[6:7]:
            cnt = cnt+1
            print(tmp)
            fp.write(tmp+"\n")

fp.close()
print("%d 개의 정보가 생성됨." % cnt)
print("%d 개의 정보가 %s 의 위치에 LIST.txt 라는 이름으로 저장됨." % (cnt, os.getcwd()))