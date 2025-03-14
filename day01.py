# 1. 파일 생성하기
# 파일 객체 = open(파일 이름, 파일 열기 모드)

f = open("새파일.txt", 'w', encoding='utf-8')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# https://wikidocs.net/26 여기서부터

"""
ㅁㄴㅇ이것도 주석인가요?
"""

