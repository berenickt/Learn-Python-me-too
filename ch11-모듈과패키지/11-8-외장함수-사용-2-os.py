# os : 운영체제에서 제공하는 기본 기능
import os

print(os.getcwd())  # 현재 작업 폴더 위치(경로)

folder = "sample_dir"

if os.path.exists(folder):  # 같은 이름의 폴더가 존재한다면
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)  # 폴더 삭제
    print(folder, "폴더를 삭제했습니다.")  # 삭제 문구 출력
else:  # 폴더가 존재하지 않으면
    os.makedirs(folder)  # 폴더 생성
    print(folder, "폴더를 생성했습니다.")

print(os.listdir())  # 현재 작업 폴더 안의 폴더와 파일 목록 출력
