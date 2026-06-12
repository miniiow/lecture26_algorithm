# BOJ 10814: 나이순 정렬

class BOJ10814:
    def main(self):
        members = []
        try:
            turn = int(input('입력횟수 정수로 입력: '))
        except ValueError:
            print('!!! 정수로 입력하세요')
        else:
            human = []
            for _ in range(turn):
                human = input('인간정보 입력: ').split()
                info = (int(human[0]), human[1])
                members.append(info)
        self.age_sort(members)
        for member in members:
            print(member[0], member[1])

    def age_sort(self, members):
        members.sort(key=lambda x: x[0])
        return members
    
if __name__ == '__main__':
    app = BOJ10814()
    app.main()