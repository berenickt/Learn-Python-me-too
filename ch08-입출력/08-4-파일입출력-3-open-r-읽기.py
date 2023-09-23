score_file = open("score.txt", "r", encoding="utf8")  # score.txt 파일을 읽기 모드로 열기
print(score_file.read())  # 파일 전체 읽어 오기
score_file.close()


score_file = open("score.txt", "r", encoding="utf8")

while True:
    line = score_file.readline()
    if not line:  # 더 이상 읽어 올 내용이 없을 때
        break  # 반복문 탈출
    print(line, end="")  # 읽어 온 내용 출력

score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # 파일에서 모든 줄을 읽어와 리스트 형태로 저장

for line in lines:  # lines에 내용이 있을 때까지
    print(line, end="")  # 읽어 온 내용 출력

score_file.close()


score_file = open("score.txt", "r", encoding="utf8")  # score.txt 파일을 읽기 모드로 열기
print(score_file.readline(), end="")  # 한 줄씩 읽어 오고 커서는 다음 줄로 이동
print(score_file.readline(), end="")  # end 값을 설정해 줄 바꿈 중복 수행 방지
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
