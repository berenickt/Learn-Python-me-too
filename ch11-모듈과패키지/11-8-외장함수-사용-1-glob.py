# 파이썬 외장함수 리스트 https://docs.python.org/3/py-modindex.html
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob

print(glob.glob("*.py"))  # 확장자가 py인 모든 파일 출력
