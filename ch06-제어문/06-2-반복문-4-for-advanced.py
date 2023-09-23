# 👉 6.2.4 1줄 for문
students = [1, 2, 3, 4, 5]
print(students)

# 한 줄 for 문으로 각 항목에 100 더하기
students = [i + 100 for i in students]
# students = [students[0] + 100, students[1] + 100, students[2] + 100, students[3] + 100, students[4] + 100]
# students = [1 + 100, 2 + 100, 3 + 100, 4 + 100, 5 + 100]
print(students)


students = ["Iron man", "Thor", "Spider Man"]
print(students)

# 한 줄 for 문으로 각 이름을 이름의 길이 정보로 변환
students = [len(i) for i in students]
# students = [len(students[0]), len(students[1]), len(students[2])]
# students = [len("Iron man"), len("Thor"), len("Spider Man")]
print(students)


students = ["Iron man", "Thor", "Spider Man"]
print(students)

# 한 줄 for 문으로 각 이름을 모두 대문자로 변경
students = [i.upper() for i in students]
print(students)
