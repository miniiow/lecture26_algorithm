# BOJ 10825: 국영수

class BOJ10825:
    def main(self):
        students = []
        try:
            turn = int(input('학생 수 입력: '))
        except ValueError:
            print('!!! 정수로 입력하세요')
        else:
            for _ in range(turn):
                info = input('이름 국어 영어 수학 입력: ').split()
                student = (info[0], int(info[1]), int(info[2]), int(info[3]))
                students.append(student)

        students = self.score_sort(students)
        for student in students:
            print(student[0])

    def score_sort(self, students):
        students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
        return students

if __name__ == '__main__':
    app = BOJ10825()
    app.main()